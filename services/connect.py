import json
import socket
import queue
import threading
import time
import traceback
from PyQt5 import QtCore

from services.worker import Worker

class SocketClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None
        self.workers = []
        self.lock = threading.Lock()
        self.task_queue = queue.Queue()
        self.is_processing = False
        self.max_concurrent_tasks = 2
        
        # Iniciar hilo para procesar tareas en cola
        self.queue_thread = threading.Thread(target=self._process_queue, daemon=True)
        self.queue_thread.start()
    
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Configurar timeout para evitar bloqueos indefinidos
            self.socket.settimeout(30)
            self.socket.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")
            return True
        except ConnectionRefusedError:
            print(f"Could not connect to {self.host}:{self.port}. The server might not be running.")
            return False
        except Exception as e:
            print(f"An error occurred while trying to connect: {e}")
            return False
    
    def reconnect(self):
        """Intenta reconectar al servidor"""
        print("Intentando reconectar al servidor...")
        try:
            if self.socket:
                self.socket.close()
            return self.connect()
        except Exception as e:
            print(f"Error al reconectar: {e}")
            return False
    
    def _process_queue(self):
        """Procesa las tareas en la cola de manera secuencial"""
        while True:
            try:
                if not self.task_queue.empty():
                    with self.lock:
                        if len(self.active_workers()) < self.max_concurrent_tasks:
                            task = self.task_queue.get()
                            self._execute_task(task)
                            self.task_queue.task_done()
                time.sleep(0.1)
            except Exception as e:
                print(f"Error en el procesamiento de la cola: {e}")
                print(traceback.format_exc())
    
    def _execute_task(self, task):
        """Ejecuta una tarea específica"""
        hmi, json_data, handle, handle_videos, callback = task
        self._create_worker(hmi, json_data, handle, handle_videos, callback)
    
    def active_workers(self):
        """Retorna los workers activos actuales"""
        return [w for w in self.workers if w.isRunning()]
    
    def cleanup_workers(self):
        """Limpia los workers finalizados"""
        with self.lock:
            active_workers = []
            for worker in self.workers:
                if worker.isRunning():
                    active_workers.append(worker)
                else:
                    worker.wait()
            self.workers = active_workers
    
    def send_message(self, message: str):
        try:
            if not self.socket:
                if not self.reconnect():
                    raise ConnectionError("No se pudo establecer conexión con el servidor")
            
            self.socket.sendall(message.encode("utf-8"))
        except socket.error as e:
            print(f"Error de socket al enviar mensaje: {e}")
            if self.reconnect():
                # Reintentar una vez después de reconectar
                self.socket.sendall(message.encode("utf-8"))
            else:
                raise
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
            raise
    
    def receive_message(self) -> str:
        try:
            if not self.socket:
                if not self.reconnect():
                    raise ConnectionError("No se pudo establecer conexión con el servidor")
            
            response = self.socket.recv(4096)  # Buffer más grande
            if not response:
                raise ConnectionError("Conexión cerrada por el servidor")
                
            response_str = response.decode("utf-8")
            return response_str
        except socket.timeout:
            print("Timeout esperando respuesta del servidor")
            raise
        except socket.error as e:
            print(f"Error de socket al recibir mensaje: {e}")
            if self.reconnect():
                # Reintentar una vez después de reconectar
                return self.receive_message()
            else:
                raise
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            raise
    
    def receive_file(self, file_path: str):
        try:
            if not self.socket:
                if not self.reconnect():
                    raise ConnectionError("No se pudo establecer conexión con el servidor")
            
            with open(file_path, "wb") as file:
                while True:
                    data = self.socket.recv(8192)  # Buffer más grande
                    if not data:
                        break
                    if data.endswith(b"EOF"):
                        file.write(data[:-3])
                        break
                    file.write(data)
            
            print(f"Archivo recibido y guardado en {file_path}")
            return True
        except Exception as e:
            print(f"Error al recibir archivo: {e}")
            return False
    
    def send_json(self, data: dict) -> str:
        try:
            json_message = json.dumps(data)
            self.send_message(json_message)
            return self.receive_message()
        except Exception as e:
            print(f"Error al enviar JSON: {e}")
            return f"Error: {str(e)}"
    
    def send_json_async(self, hmi, json_data, handle=None, handle_videos=False, callback=None):
        """
        Envía datos JSON de forma asíncrona, poniendo la tarea en cola si hay otras en proceso
        
        Args:
            hmi: Referencia a la interfaz del usuario
            json_data: Datos a enviar en formato JSON
            handle: Tipo de manejador para la respuesta
            handle_videos: Indica si se deben manejar videos
            callback: Función a llamar cuando se complete la operación
        """
        try:
            # Añadir tarea a la cola
            self.task_queue.put((hmi, json_data, handle, handle_videos, callback))
            print(f"Tarea añadida a la cola. Tareas pendientes: {self.task_queue.qsize()}")
        except Exception as e:
            print(f"Error al encolar tarea asíncrona: {e}")
            print(traceback.format_exc())
            if callback:
                callback(f"Error: {str(e)}")
    
    def _create_worker(self, hmi, json_data, handle=None, handle_videos=False, callback=None):
        """Crea y configura un worker para procesar una tarea específica"""
        try:
            # Crear worker
            worker = Worker(self, json_data, handle_videos, callback)
            
            # Conectar señales según el tipo de operación
            if handle:
                if handle == "stop_video":
                    worker.response_received.connect(hmi.handle_video_response)
                elif handle == "start_video":
                    worker.response_received.connect(hmi.handle_video_response)
                elif handle == "start_realtime":
                    worker.response_received.connect(hmi.handle_realtime_response)
                elif handle == "cycle":
                    worker.response_received.connect(hmi.handle_cycle_response)
                elif handle == "stop_system":
                    worker.response_received.connect(hmi.handle_ose_response)
            
            # Conectar señal de finalización para limpieza
            worker.finished.connect(lambda: self.cleanup_worker(worker))
            
            # Almacenar y comenzar el worker
            with self.lock:
                self.workers.append(worker)
                worker.start()
                
            return worker
            
        except Exception as e:
            print(f"Error al crear worker: {e}")
            print(traceback.format_exc())
            if callback:
                callback(f"Error: {str(e)}")
            return None
    
    def cleanup_worker(self, worker):
        """Limpia un worker específico al finalizar"""
        try:
            worker.wait()
            with self.lock:
                if worker in self.workers:
                    self.workers.remove(worker)
        except Exception as e:
            print(f"Error al limpiar worker: {e}")
    
    def cancel_all_tasks(self):
        """Cancela todas las tareas en proceso y en cola"""
        try:
            print("Cancelando todas las tareas...")
            
            # Vaciar la cola de tareas pendientes
            while not self.task_queue.empty():
                try:
                    self.task_queue.get_nowait()
                    self.task_queue.task_done()
                except queue.Empty:
                    break
            
            # Cancelar workers activos
            with self.lock:
                for worker in self.active_workers():
                    worker.cancel()
                    
            print("Todas las tareas canceladas")
        except Exception as e:
            print(f"Error al cancelar tareas: {e}")
    
    def close_connection(self):
        """Cierra la conexión y limpia los recursos"""
        try:
            self.cancel_all_tasks()
            
            if self.socket:
                self.socket.close()
                self.socket = None
                print("Conexión cerrada.")
        except Exception as e:
            print(f"Error al cerrar conexión: {e}")
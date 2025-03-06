from PyQt5 import QtCore
import time
import traceback

class Worker(QtCore.QThread):
    response_received = QtCore.pyqtSignal(str)
    progress_update = QtCore.pyqtSignal(int)
    operation_complete = QtCore.pyqtSignal(bool)
    cancel_requested = QtCore.pyqtSignal()
    
    def __init__(self, client, json_data, handle_videos=False, callback=None):
        super().__init__()
        self.client = client
        self.json_data = json_data
        self.handle_videos = handle_videos
        self._cancelled = False
        self.callback = callback
        self.max_retries = 3
        self.retry_delay = 1  # segundos
    
    def run(self):
        try:
            retries = 0
            success = False
            
            while retries < self.max_retries and not success and not self._cancelled:
                try:
                    if self.handle_videos:
                        self.run_videos()
                    else:
                        response = self.client.send_json(self.json_data)
                        self.response_received.emit(response)
                        
                        # Si llegamos aquí, la operación fue exitosa
                        if self.callback:
                            self.callback(response)
                    
                    success = True
                    
                except Exception as e:
                    retries += 1
                    print(f"Error en intento {retries}/{self.max_retries}: {e}")
                    print(traceback.format_exc())
                    
                    if retries < self.max_retries and not self._cancelled:
                        print(f"Reintentando en {self.retry_delay} segundos...")
                        time.sleep(self.retry_delay)
                    else:
                        error_msg = f"Error después de {retries} intentos: {str(e)}"
                        self.response_received.emit(error_msg)
                        if self.callback:
                            self.callback(error_msg)
            
            self.operation_complete.emit(success)
            
        except Exception as e:
            print(f"Error crítico en el hilo worker: {e}")
            print(traceback.format_exc())
            self.response_received.emit(f"Error crítico: {str(e)}")
            if self.callback:
                self.callback(f"Error crítico: {str(e)}")
            self.operation_complete.emit(False)
    
    def receive_file(self, client_socket, file_path):
        try:
            bytes_received = 0
            file_size = 1  # Valor predeterminado, idealmente se obtendría del servidor
            
            with open(file_path, "wb") as f:
                while not self._cancelled:
                    data = client_socket.recv(8192)  # Usar buffer más grande
                    if not data:
                        break
                        
                    bytes_received += len(data)
                    
                    # Actualizar progreso si se conoce el tamaño del archivo
                    if file_size > 0:
                        progress = int((bytes_received / file_size) * 100)
                        self.progress_update.emit(progress)
                    
                    if data.endswith(b"EOF"):
                        f.write(data[:-3])
                        break
                    f.write(data)
                    
            if not self._cancelled:
                client_socket.sendall(b"NEXT")
                return True
            return False
            
        except Exception as e:
            print(f"Error recibiendo archivo {file_path}: {e}")
            print(traceback.format_exc())
            raise
    
    def run_videos(self):
        try:
            # Informar del inicio de la descarga
            self.response_received.emit("Iniciando descarga de videos...")
            
            # Obtener las rutas de los videos del servidor
            success1 = self.receive_file(self.client.socket, "src/videos/camara_recived_1.mp4")
            if self._cancelled:
                self.response_received.emit("Descarga cancelada por el usuario")
                return
                
            if success1:
                self.response_received.emit("Primer video descargado correctamente")
            
            success2 = self.receive_file(self.client.socket, "src/videos/camara_recived_2.mp4")
            if self._cancelled:
                self.response_received.emit("Descarga cancelada por el usuario")
                return
                
            if success2:
                self.response_received.emit("Segundo video descargado correctamente")
            
            # Recibir confirmación del servidor
            data = self.client.socket.recv(4096)
            response = data.decode("utf-8")
            self.response_received.emit(response)
            
            # Llamar al callback si existe
            if self.callback:
                self.callback(response)
                
        except Exception as e:
            error_msg = f"Error en run_videos: {e}"
            print(error_msg)
            print(traceback.format_exc())
            self.response_received.emit(error_msg)
            if self.callback:
                self.callback(error_msg)
    
    def cancel(self):
        self._cancelled = True
        self.cancel_requested.emit()
        print("Operación cancelada por el usuario")
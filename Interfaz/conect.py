import socket
import json

class SocketCliente:
    def __init__(self, host: str, port: int):
        """
        Inicializa el cliente socket con la IP y el puerto del servidor.
        :host: Dirección IP del servidor.
        :puerto: Puerto del servidor.
        """
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """
        Conecta al servidor.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Conectado a {self.host}:{self.port}")
        except ConnectionRefusedError:
            print(f"No se pudo conectar a {self.host}:{self.port}. El servidor podría no estar en ejecución.")
        except Exception as e:
            print(f"Ocurrió un error al intentar conectar: {e}")

    def envio_Mensaje(self, mensaje: str):
        """
        Envía un mensaje al servidor.
        :mensaje: Mensaje en formato de texto a enviar.
        """
        try:
            if self.socket:
                self.socket.sendall(mensaje.encode('utf-8'))
                # print(mensaje)
                response = self.socket.recv(1024)
                print(f"Mensaje del servidor: {response.decode('utf-8')}")
            else:
                print("Error: No se está conectado al servidor.")
        except Exception as e:
            print(f"Ocurrió un error al enviar el mensaje: {e}")

    def envio_json(self, data: dict):
        """
        Envía un mensaje en formato JSON.
        :data: Diccionario de datos a enviar como JSON.
        """
        try:
            json_mensaje = json.dumps(data)
            self.envio_Mensaje(json_mensaje)
        except Exception as e:
            print(f"Ocurrió un error al enviar el JSON: {e}")

    def cierra_coneccion(self):
        """
        Cierra la conexión con el servidor.
        """
        if self.socket:
            self.socket.close()
            print("Conexión cerrada.")

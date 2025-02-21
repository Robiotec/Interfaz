import socket
import json
import os

class SocketClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")
        except ConnectionRefusedError:
            print(f"Could not connect to {self.host}:{self.port}. The server might not be running.")
        except Exception as e:
            print(f"An error occurred while trying to connect: {e}")

    def send_message(self, message: str):
        try:
            if self.socket:
                self.socket.sendall(message.encode('utf-8'))
            else:
                print("Error: Not connected to the server.")
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")

    def receive_message(self) -> str:
        try:
            if self.socket:
                response = self.socket.recv(1024)
                response_str = response.decode('utf-8')
                return response_str
            else:
                print("Error: Not connected to the server.")
                return ""
        except Exception as e:
            print(f"An error occurred while receiving the message: {e}")
            return ""

    def receive_file(self, file_path: str):
        try:
            if self.socket:
                with open(file_path, 'wb') as file:
                    while True:
                        data = self.socket.recv(1024)
                        if not data:
                            break
                        file.write(data)
                print(f"File received and saved to {file_path}")
            else:
                print("Error: Not connected to the server.")
        except Exception as e:
            print(f"An error occurred while receiving the file: {e}")

    def send_json(self, data: dict) -> str:
        try:
            json_message = json.dumps(data)
            self.send_message(json_message)
            response = self.receive_message()
            return response
        except Exception as e:
            print(f"An error occurred while sending the JSON: {e}")
            return ""

    def close_connection(self):
        if self.socket:
            self.socket.close()
            print("Connection closed.")

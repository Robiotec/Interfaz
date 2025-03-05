from PyQt5 import QtCore


class Worker(QtCore.QThread):
    response_received = QtCore.pyqtSignal(str)

    def __init__(self, client, json_data, handle_videos=False):
        super().__init__()
        self.client = client
        self.json_data = json_data
        self.handle_videos = handle_videos

    def run(self):
        try:
            if self.handle_videos:
                self.run_videos()
            else:
                response = self.client.send_json(self.json_data)
                self.response_received.emit(response)
        except Exception as e:
            print(f"An error occurred while running the worker thread: {e}")
            self.response_received.emit(f"Error: {str(e)}")

    def receive_file(self, client_socket, file_path):
        try:
            with open(file_path, "wb") as f:
                while True:
                    data = client_socket.recv(4096)
                    if not data:
                        break
                    if data.endswith(b"EOF"):
                        f.write(data[:-3])
                        break
                    f.write(data)
            client_socket.sendall(b"NEXT")
        except Exception as e:
            print(f"Error receiving file {file_path}: {e}")
            raise

    def run_videos(self):
        try:
            self.receive_file(self.client.socket, "src/videos/camara_recived_1.mp4")
            self.receive_file(self.client.socket, "src/videos/camara_recived_2.mp4")

            data = self.client.socket.recv(4096)
            self.response_received.emit(data.decode("utf-8"))
        except Exception as e:
            print(f"Error in run_videos: {e}")
            self.response_received.emit(f"Error: {str(e)}")

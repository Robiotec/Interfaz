from PyQt5 import QtCore

class Worker(QtCore.QThread):
    response_received = QtCore.pyqtSignal(str)

    def __init__(self, client, json, handle_videos=False):
        super().__init__()
        self.client = client
        self.json = json
        self.handle_videos = handle_videos

    def run(self):
        if self.handle_videos:
            self.run_videos()
        else:
            response = self.client.send_json(self.json)
            self.response_received.emit(response)

    def receive_file(self, client_socket, file_path):
        with open(file_path, "wb") as f:
            while True:
                data = client_socket.recv(4096)
                if data.endswith(b"EOF"):
                    f.write(data[:-3])
                    break
                f.write(data)
        client_socket.sendall(b"NEXT")

    def run_videos(self):
        self.receive_file(self.client.socket, "videos/camara_recived_1.mp4")
        self.receive_file(self.client.socket, "videos/camara_recived_2.mp4")

        data = self.client.socket.recv(4096)
        self.response_received.emit(data.decode("utf-8"))


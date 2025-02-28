import threading

from PyQt5.QtCore import QObject, pyqtSignal


class Worker(QObject, threading.Thread):
    response_received = pyqtSignal(str)

    def __init__(self, client, json_data, handle_videos=False):
        QObject.__init__(self)
        threading.Thread.__init__(self)
        self.client = client
        self.json_data = json_data
        self.handle_videos = handle_videos

    def run(self):
        try:
            if self.handle_videos:
                self.run_videos()
            else:
                response = self.client.send_json(self.json)
                self.response_received.emit(response)
        except Exception as e:
            print(f"An error occurred while running the worker thread: {e}")
            self.response_received.emit("Error")

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

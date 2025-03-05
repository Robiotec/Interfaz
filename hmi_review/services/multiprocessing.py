from services.connect import SocketClient

class Multiprocesos:
    super().__init__()
    def __init__(self, data_json):
        self.data_json = data_json
        self.client = SocketClient("192.168.1.100", 5000)
        self.client.connect()
    
    def run_process(self):
        try:
            send_process_servidor = self.client.send_json(self.data_json)
            return send_process_servidor
        except Exception as e:
            print(f"An error occurred while running the process: {e}")
    
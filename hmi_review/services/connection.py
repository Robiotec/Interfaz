import socket

HOST = '192.168.1.100'   # IP fija del servidor Asiganada
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print(f"Conectado a {HOST}:{PORT}")
        while True:
            mensaje_a_enviar = input("Escribe un mensaje: ")
            s.sendall(mensaje_a_enviar.encode('utf-8'))
            mensaje = s.recv(1024) #Recibe la respuesta del servidor
            if not mensaje:
                break
            print(f"Mensaje del servidor: {mensaje.decode('utf-8')}")
    except ConnectionRefusedError:
        print(f"No se pudo conectar a {HOST}:{PORT}. El servidor podría no estar en ejecu")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

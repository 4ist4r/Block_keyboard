import socket

SERVER_IP = "192.168.1.100"  # Reemplaza con la IP de la máquina remota
PORT = 65432

def enviar_comando(comando):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        s.sendall(comando.encode())

# Bloquear teclado
enviar_comando("bloquear")

# Desbloquear teclado
enviar_comando("desbloquear")

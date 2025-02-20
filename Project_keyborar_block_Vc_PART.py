import socket
import keyboard

# Configurar servidor
HOST = "0.0.0.0"  # Escucha en todas las interfaces de red
PORT = 65432

def bloquear_teclado():
    keyboard.block_key("all")  # Bloquea todas las teclas
    print("Teclado bloqueado")

def desbloquear_teclado():
    keyboard.unhook_all()  # Desbloquea el teclado
    print("Teclado desbloqueado")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Esperando conexión...")

    conn, addr = server.accept()
    with conn:
        print(f"Conectado desde {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            if data == "bloquear":
                bloquear_teclado()
            elif data == "desbloquear":
                desbloquear_teclado()

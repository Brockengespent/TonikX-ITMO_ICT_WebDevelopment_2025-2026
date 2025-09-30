import socket
import threading

# Поток для приёма сообщений от сервера
def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break  # На всякий случай — если сервер отвалился, просто выходим

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))

# Отдельный поток — чтобы сообщения других пользователей отображались сразу
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Основной цикл — отправка сообщений в чат
while True:
    msg = input()
    if msg == '/quit':  # Можно выйти из чата этой командой
        break
    client_socket.send(msg.encode())

client_socket.close()

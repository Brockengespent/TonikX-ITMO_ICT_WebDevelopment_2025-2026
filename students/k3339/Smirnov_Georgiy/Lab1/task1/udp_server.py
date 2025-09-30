import socket  # Модуль для работы с сетями

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8080))
print('UDP сервер запущен…')

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f'Получено сообщение от {addr}:', data.decode())  # Показываем адрес клиента и сам текст
    server_socket.sendto(b'Hello, client', addr)

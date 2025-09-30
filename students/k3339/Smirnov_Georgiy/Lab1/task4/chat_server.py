import socket
import threading

clients = []  # Здесь будем хранить все подключённые клиенты

# Функция для обработки конкретного клиента в отдельном потоке
def handle_client(client_socket, addr):
    while True:
        try:
            msg = client_socket.recv(1024).decode()  # Ждём сообщение от клиента
            if not msg:
                break  # Если пусто — клиент отключился
            print(f'[{addr}] {msg}')  # Выводим сообщение в консоль сервера
            # Рассылаем это сообщение всем остальным участникам чата
            for c in clients:
                if c != client_socket:
                    c.send(f'[{addr}] {msg}'.encode())
        except:
            break
    client_socket.close()
    clients.remove(client_socket)  # Удаляем клиента из списка, если он вышел

# Запуск сервера: создаём сокет, вешаемся на порт 8888
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen()
print('Сервер чата запущен…')

# Основной цикл: ждём новых клиентов и стартуем для них потоки
while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    print(f'Новый клиент: {addr}')
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()

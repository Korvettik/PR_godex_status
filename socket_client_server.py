import socket

# --------------------- TCP/IP сервер. ---------------------------
def server():
    # создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к порту
    server_address = ('localhost', 42000)
    print('Старт сервера на {} порт {}'.format(*server_address))
    sock.bind(server_address)

    # Слушаем входящие подключения
    sock.listen(1)

    while True:
        # ждем соединения
        print('Ожидание соединения...')
        connection, client_address = sock.accept()
        try:
            print('Подключено к:', client_address)
            # Принимаем данные порциями и ретранслируем их
            while True:
                data = connection.recv(16)
                print(f'Получено: {data.decode()}')
                if data:
                    print('Обработка данных...')
                    data = data.upper()
                    print('Отправка обратно клиенту.')
                    connection.sendall(data)
                else:
                    print('Нет данных от:', client_address)
                    break

        finally:
            # Очищаем соединение
            connection.close()








# --------------------- TCP/IP клиент. ---------------------------

def client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаем сокет к порту, через который прослушивается сервер
    server_address = ('localhost', 10000)
    print('Подключено к {} порт {}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Отправка данных
        mess = 'Hello Wоrld!'
        print(f'Отправка: {mess}')
        message = mess.encode('utf-16')
        sock.sendall(message)

        # Смотрим ответ
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(2048)
            print('hello')
            amount_received += len(data)
            mess = data.decode()
            print(f'Получено: {data.decode()}')

    finally:
        print('Закрываем сокет')
        sock.close()




# server()
client()
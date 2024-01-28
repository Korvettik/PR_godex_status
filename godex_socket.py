import socket

def client():
    # Создаем TCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаем сокет к порту, через который прослушивается сервер
    # server_address = ('192.168.100.164', 9100)  # Godex
    server_address = ('192.168.100.184', 9100)  # Gogex G500 (Узнать IP: нажать на кнопку, включить. моргает красным и желтым, отпустить кнопку)
    print('Подключаюсь к {} порт {}'.format(*server_address))


    try:
        sock.connect(server_address)
        print('Подключение установлено')
    except Exception as e:
        print(e)
        print('Нет связи с принтером')
        return

    try:
        # Отправка данных

        mess1 = ''

        mess2 = ('~S,STATUS\r\n')  # узнать статус

        mess3 = ('^Q20,3\r'   # печать пробного кода
                '^W20\r'
                '^H6\r'
                '^P1\r'
                '^S2\r'
                '^L\r'
                'XRB105,140,8,0,10\r'
                '0123456789\r'
                'E\r\n')

        mess4 = (
                 '^XSETCUT, DOUBLECUT, 0\r'
                 '^Q25,3\r'
                 '^W25\r'
                 '^H8\r'
                 '^P1\r'
                 '^S4\r'
                 '^AT\r'
                 '^C1\r'
                 '^R0\r'
                 '~Q+0\r'
                 '^O0\r'
                 '^D0\r'
                 '^E18\r'
                 '~R255\r'
                 '^L\r'
                 'Dy2-me-dd\r'
                 'Th:m:s\r'
                 'XRB70,75,5,0,12\r'
                 '~10123456789\r'
                 'E\r\n'
                 )


        mess5 = (
                '^XSETCUT, DOUBLECUT, 0\r'
                '^Q20,4\r'
                '^W20\r'
                '^H8\r'
                '^P1\r'
                '^S4\r'
                '^AT\r'
                '^C1\r'
                '^R0\r'
                '~Q+0\r'
                '^O0\r'
                '^D0\r'
                '^E30\r'
                '~R255\r'
                '^L\r'
                'Dy2-me-dd\r'
                'h:m:s\r'
                'Dy2-me-dd\r'
                'Th:m:s\r'
                'XRB50,55,5,0,12\r'
                '~10123456789\r'
                'E\r\n'
                )


        print(f'Отправка: {mess5}')
        message = mess5.encode('utf-8')
        sock.sendall(message)

        # Смотрим ответ
        answer_buffer = ''
        while '\r\n' not in answer_buffer:
            data = sock.recv(2048)
            mess = data.decode()
            answer_buffer += mess
            print(f'Получено: {data}')




    finally:
        print('Закрываем сокет')
        sock.shutdown(2)
        sock.close()

client()
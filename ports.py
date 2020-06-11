import socket
import threading

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Создаем сокет
    s.settimeout(0.5) #выставим тайм аут
    try:
        con = s.connect((host, port)) #пробуем подключиться
        print(host +": " + str(port) + " OPEN ") 
        con.close()
    except:
        pass
host = input("Введите IP адресс или имя сайта: ")
for i in range(9999): # проверим от 1 до 9999 порты
    p = threading.Thread(target=scan_port, args=(host,i)) #Потоки
    p.start()


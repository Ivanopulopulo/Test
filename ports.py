import socket
import threading

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) 
    try:
        con = s.connect((host, port))
        print(host +": " + str(port) + " OPEN ")
        con.close()
    except:
        pass
host = input("Введите IP адресс или имя сайта: ")
for i in range(9999):
    p = threading.Thread(target=scan_port, args=(host,i)) #Потоки
    p.start()


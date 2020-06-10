import socket
import threading

def domain_in(name):
    i = socket.gethostbyname(name)
    print(i)
domen = input("Введите адресс сайта оригинала без доменной зоны: ")

s1 = '0123456789qwertyuioplkjhgfdsazxcvbnm'
s2 = ['com','ru','net','org','info','cn','es','top','au','pl','it','uk','tk','ml','ga','cf','us','xyz','top','site','win','bid'] 
i=0
n=0
m=0
success = []
while n < len(s1):
    n += 1
    if (n == len(s1)):
        m+=1
        n=0
        i=0
        continue
    if (m == len(s2)):
        m=0
        break
    name = domen + s1[n] + "." + s2[m]
    print(name)
    try:
        domain_in(name)
        success.append(name)
    except:
        print("NOT FOUND")
        pass
    name = domen
while i < len(domen):
    i+=1
    if(i == len(domen)):
        i=0
        m+=1
    if (m == len(s2)):
        m=0
        break
    name = domen[:i] + domen[i+1:]
    name = name + "." + s2[m]
    print(name)
    try:
        domain_in(name)
        success.append(name)
    except:
        print("NOT FOUND")
        pass
    name = domen
    
while i < len(domen):
    i+=1
    if(i == len(domen)):
        i=1
        m+=1
    if (m == len(s2)):
        break
    name = domen[:i] + "." + domen[i:]
    name = name + "." + s2[m]
    print(name)
    try:
        domain_in(name)
        success.append(name)
    except:
        print("NOT FOUND")
        pass
    name = domen
print("Домены к которым получилось подключиться: ")
print(success)

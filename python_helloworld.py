import datetime
import socket

now = datetime.datetime.now()
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

ascii_art = '''
#########################################################################################################
          ____        __      ______    __                  ____                                __      
         /\  _`\     /\ \    /\__  _\  /\ \                /\  _`\                             /\ \__   
         \ \ \L\_\   \_\ \   \/_/\ \/  \ \ \___       __   \ \ \L\_\   _ __     __      __     \ \ ,_\  
          \ \  _\    /'_` \     \ \ \   \ \  _ `\   /'__`\  \ \ \L_L  /\`'__\ /'__`\  /'__`\    \ \ \/  
           \ \ \L\ \/\ \L\ \     \ \ \   \ \ \ \ \ /\  __/   \ \ \/, \\ \ \/ /\  __/ /\ \L\.\_   \ \ \_ 
            \ \____/\ \___,_\     \ \_\   \ \_\ \_\\ \____\   \ \____/ \ \_\ \ \____\\ \__/.\_\   \ \__\
             \/___/  \/__,_ /      \/_/    \/_/\/_/ \/____/    \/___/   \/_/  \/____/ \/__/\/_/    \/__/
#########################################################################################################
'''

print(ascii_art)
print(f'\n')

print(f'Hello world, Written in python\n')
print(f"Date and time: {now}\n")
print(f"You're running on host: {hostname}\n")
print(f"Your host IP Address is: {ipaddr}\n")




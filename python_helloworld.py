import datetime
import socket

now = datetime.datetime.now()
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)


print(f'Hello world, Written in python\n')
print(f"It is currently: {now}\n")
print(f"Youre running on host: {hostname}\n")
print(f"Your Computer IP Address is: {ipaddr}\n")




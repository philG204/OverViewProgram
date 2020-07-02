import subprocess as sub
import socket
import time
import sys

def send_command(command):
        #Here is the part were the command is called
        p_1 = sub.check_output(command)
        #The command will be printed out and gets send over network
        print(type(sys.getsizeof(p_1)), sys.getsizeof(p_1))
        conn.send(bytes(sys.getsizeof(p_1)))
        time.sleep(0.05)
        #after that the command himself gets send before it will printed out
        print(p_1.decode('utf-8'))
        conn.send(p_1)
        time.sleep(0.05)
        


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(socket.gethostbyname("nas.local"),  420))
s.listen(1)
print("Server is running...")
conn, addr = s.accept()
print("connected")

while True:
        send_command("w")
        

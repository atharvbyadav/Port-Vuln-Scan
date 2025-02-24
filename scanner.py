#!/usr/bin/python3

import socket
import os
import sys

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print("[-] File Doesn't Exist!")
			exit(0)
		if not os.access(filename, os.R_OK):
			print("[-] Access Denied!")
	else:
		print("[-] Usage: " + str(str.argv[0]) + "<vuln filename>")
		exit(0)
	portlist = [21, 22, 25, 80, 110, 443,445]
	for x in range(4,6):
		ip = "10.0.2." + str(x)
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print("[+] " + ip + "/" + str(port) + " : " + banner)
				checkVulns(banner, filename)

main()

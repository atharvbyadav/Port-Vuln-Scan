#!/usr/bin/python

from socket import *
import optparse
from threading import Thread

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((tgtHost, tgtPort))
        print(f'[+] {tgtPort}/tcp Open')
    except (timeout, error):
        print(f'[-] {tgtPort}/tcp Closed')
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
        print(f'[+] Scan Result for: {tgtHost} ({tgtIP})')
    except gaierror:
        print(f'[-] Unknown Host {tgtHost}')
        return

    setdefaulttimeout(1)
    threads = []

    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def main():
    parser = optparse.OptionParser('Usage: -H <target host> -p <target port(s)>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target ports (comma-separated)')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort.split(',') if options.tgtPort else []

    if not tgtHost or not tgtPorts:
        print(parser.usage)
        exit(0)

    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

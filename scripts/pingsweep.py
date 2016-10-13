#!/usr/bin/python
import sys, os, argparse, re, subprocess
from multiprocessing import Pool

def ping(ip):
    pingit = subprocess.Popen(["ping", "-c1", ip], stdout=subprocess.PIPE).communicate()[0]
    if "bytes from" in pingit:
 
    	print(re.findall( r'[0-9]+(?:\.[0-9]+){3}', pingit )[0])
    
    

if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--iprange', default='10.11.1.', help='IP range, i.e 10.11.1.')
    parser.add_argument('-t', '--threads', default=200, help='threads')
    
    args = parser.parse_args()
    iprange = args.iprange
    MAXPROCESSES=int(args.threads)

    print("Generating IPs...")
    pool = Pool(processes=MAXPROCESSES)
    ips = []
    for i in range (0,255):
	ips.append(iprange+str(i))
        
    

    pool.map(ping, ips)
    #print("Finished")

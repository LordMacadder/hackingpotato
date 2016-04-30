#NMAP Basics

##Basic Scan first 1,000 ports
`nmap 10.11.1.220`

##Find hosts in range
`nmap -sn 10.11.1.0-254`

##Output to file
`nmap -sn 10.11.1.0-254 -oG ping-sweep-nmap.txt`

##Search for a port on multiple hosts
`nmap -p 80 10.11.1.0-254 -oG web-sweep.txt`

##Scan for top 20 ports
`nmap -sT --top-ports 20 10.11.1.0-254 -oG web-sweep.txt`

##OS Fingerprinting
`nmap -A 10.11.1.220`
However -A doubles traffic (100kb)


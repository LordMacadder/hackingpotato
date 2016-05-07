#SNMP

##Scanning
`nmap -sU --open -p 161 xx.xx.x.1-254`

## Enumeration
`onesixtyone -c community.txt -i valid-addresses.txt`
* valid-addresses.txt is a line by line list of ips
* community.txt is a line by line of community values `public, private, manager`

## Probing using snmp walk
* get everything `snmpwalk -c public -v1 xx.xx.x.227`

### Target somewhere better
1. Create a file with the following lines

   ```
   1.3.6.1.2.1.25.1.6.0 System Processes
   1.3.6.1.2.1.25.4.2.1.2 Running Programs
   1.3.6.1.2.1.25.4.2.1.4 Processes Path
   1.3.6.1.2.1.25.2.3.1.4 Storage Unitys
   1.3.6.1.2.1.25.6.3.1.2 Software Name
   1.3.6.1.2.1.77.1.2.25  User Accounts
   1.3.6.1.2.1.6.13.1.3 TCP Local Ports
   ```

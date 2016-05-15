#SMB
Common vulnerable service on older Windows Server 2003/xp machines, used in later machines but service has less holes.

##Scanning
`nmap -oG smb-sweep.txt -p 139,445 xx.xx.x.1-254 --open`

`nbtscan 10.11.1.1-254`

##Null Sessions (enabled by default in 2003/xp)
1. Connect using `rpcclient -U "" xx.xx.x.202`
2. Enter blank password
3. You can now enumerate

##Enumeration
###Manual
* Give specific os version `srvinfo`
* List usernames on server `enumdomusers`
* Get password rules `getdompwinfo`

###enum4linux
Will gather a wealth of information from null session `enum4linux -v xx.xx.x.202`

###Nmap SME scripts
* nmap has a number of scripts a full list can be found using `ls -l /usr/share/nmap/scripts/ | grep "smb"`
* Get OS `nmap -p 139,445 --script smb-os-discovery xx.xx.x.220`
* Enumerate users `nmap -p 139,445 --script smb-enum-users xx.xx.x.202 -oN nmap-enum-users.txt`
* Check for vulns `nmap -p 139,445 --script smb-check-vulns --script-args=unsafe=1 10.11.1.229 -oN nmap-smb-vuln.txt`



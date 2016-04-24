#Basic DNS Enumeration

1. Find NS records 

   ```
   root@kali:~# host -t ns xyz.com
   xyz.com name server ns3.xyz.com.
   xyz.com name server ns1.xyz.com.
   xyz.com name server ns2.xyz.com.
   ```

2. Find MX records

   ```
   root@kali:~# host -t mx xyz.com
   xyz.com mail is handled by 20 spool.mail.abc.net.
   xyz.com mail is handled by 50 mail.xyz.com.
   xyz.com mail is handled by 60 mail2.xyz.com.
   xyz.com mail is handled by 10 fb.mail.abc.net.
   ```

3. Get IP Address for web server (assuming it's called www) `host www.xyz.com`

## Forward DNS Lookup

1. populate a text file with a list of potential subdomains

    ```
    www
    ftp
    mx
    mail
    admin
    portal
    owa
    proxy
    router
    www2
    firewall
    pop3
    imap
    ```
2. Then create a shell to loop through and run the host command outputting valid results

    ```
    #!/bin/bash
    for name in $(cat list.txt); do
	   host $name.xyz.com|grep "has address"|cut -d" " -f1,4
    done
    ```
## Reverse DNS lookup

1. From the forward lookup we can take the minimum ip range (72) and the maximum (91) and run host against those inbetween to discover any hosts we might of missed using the below bash

   ```
   #!/bin/bash
   for ip in $(seq  72 91); do
      host 38.100.193.$ip | grep "domain name pointer" | cut -d" " -f1,5
   done
   ```

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


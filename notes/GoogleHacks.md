# Google Hacks

1. Get subdomain pages
   `site:apple.com -site:www.apple.com`

2. Get PPT files from domain
   `site:apple.com filetype:ppt`

3. Exposed VNC Viewer
   `intitle:"VNC viewer for Java"`

4. Get exposed webcams
   `inurl:"/control/userimage.html"`

5. Get exposed phpmyadmin
   `inurl:".php?" intext:CHARACTER_SETS,COLLATIONS intitle:phpmyadmin`

6. Find comped sites (from a known php backdoor)
   `intitle:"-N3T" filetype:php undetectable`

[Google Hacking DB](https://www.exploit-db.com/google-hacking-database/)

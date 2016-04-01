# Puppylizer

Explore visible site, whilst running a OWASP and DIRB scans.

*Flag 1: donate.php setting monetary value to "-1", I have seen this error before on eCommerce sites I used to run.*

DIRB and OWASP complete

*Flag 2: found in robots.txt*

*Flag 4: found in crossdomain*

*Flag 5: found in document in uploads folder*

OWASP highlighted a potential SQL vulnerability with the username field on the homepage

Crafted an attack that allowed me to login  which was as below

`' or '1'='1' -- `

Through various error messages crafting this attack, I was able to conclude there is a password column, the table is `users` and the database is `pupmulch_01`

I then used additions to my attack to establish what other typical columns I could find, resulting in establishing the below

`id, username, password, email, admin`

I then used id enumeration to login to each account and find the account that could get into `/Adm1nPan3l/`

I found that the below injection allows me to get into the second password screen

`' or '1'='1' AND id = 5 -- `

At this point I restarted the puppylizer VM and noticed it allowed me to engage single user mode. I engaged this and got access to root.

I then moved over to `/var/www` the web root

*Flag 6: found in Y0uN3verwou1dHav3foundTh15With0u7ASh3ll.txt*

I then nanoed into the config.php file, and got the sql login creds. This allowed access to /phpmyadmin/ 

*Flag 3: User fakeaccount row in table*

Back in root I checked the `/adm1nPan3l/` index, and changed it to echo the comparisons. This gave me the MD5 which I could then reverse.

I then logged into the admin panel using my injection and the reversed md5

*Flag 8: Found in admin panel*

I found the SSH details for a user rdizzle and logged in

*Flag 9: welcome message for ssh rdizzle*

Back in root, I looked around the file structure and found, a flag in \root\

*Flag 10: \root\flag.txt*

At this point I started the quiz, and found the first three digits of the missing flag along with it's rough position in the order of flags.

I concluded that it must be to do with the website and grepped for the first three digits, exposing the location in the sql.

I then nanoed into the sql file and found that it was hidden in a secret table.

*Flag 7: Secret Table hidden in database*

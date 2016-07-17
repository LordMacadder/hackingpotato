#Bandit: Level 15 -> 16

##Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

##Solution
1. SSH onto the server with the username bandit15

2. Then connect using openssl onto the port entering the password recovered from level 14

   ```
   bandit14@melinda:~$ openssl s_client -connect localhost:30001 -ign_eof
   ...loads of ssl stuff...
   BfMYroe26WYalil77FoDi9qh59eK5xNr
   Correct!
   cluFn7wTiGryunymYOu4RcffSxQluehd
   ```

Flag: cluFn7wTiGryunymYOu4RcffSxQluehd

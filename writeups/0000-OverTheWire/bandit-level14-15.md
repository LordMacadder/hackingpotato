#Bandit: Level 14 -> 15

##Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

##Solution
1. SSH onto the server with the username bandit14

2. Then netcat onto the port entering the password recovered from the file

   ```
   bandit14@melinda:~$ nc localhost 30000
   4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
   Correct!
   BfMYroe26WYalil77FoDi9qh59eK5xNr
   ```

Flag: BfMYroe26WYalil77FoDi9qh59eK5xNr

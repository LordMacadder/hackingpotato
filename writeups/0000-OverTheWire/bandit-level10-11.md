#Bandit: Level 10 -> 11

##Goal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

##Solution
1. SSH onto the server with the username bandit10

2. list the folder contents

   ```
   bandit10@melinda:~$ ls
   data.txt
   ```

3. We can use `base64` to decode

   ```
   bandit10@melinda:~$ cat data.txt | base64 --decode
   The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
   ```

Flag: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

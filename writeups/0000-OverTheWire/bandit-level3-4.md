#Bandit: Level 3 -> 4

##Goal
The password for the next level is stored in a hidden file in the inhere directory.

##Solution
1. SSH onto the server with the username bandit3

2. List the home directory using `ls -a`, then access the folder inhere and do the same

   ```
   bandit3@melinda:~$ ls -a
   .  ..  .bash_logout  .bashrc  .profile  inhere
   bandit3@melinda:~$ cd inhere
   bandit3@melinda:~/inhere$ ls -a
   .  ..  .hidden
   ```

3. Then cat the hidden file to give us the flag

   ```
   bandit3@melinda:~/inhere$ cat .hidden
   pIwrPrtPN36QITSp3EQaw936yaFoFgAB
   ```

4. Flag: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

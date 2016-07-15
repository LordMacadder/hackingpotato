#Bandit: Level 1 -> 2

##Goal
The password for the next level is stored in a file called - located in the home directory

##Solution
1. SSH onto the server with the username bandit1

2. List the home directory using `ls`

   ```
   bandit1@melinda:~$ ls
   -
   ```

3. Then cat the - file using the relative path to give us the flag

   ```
   bandit1@melinda:~$ cat ./-
   CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
   ```

4. Flag: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

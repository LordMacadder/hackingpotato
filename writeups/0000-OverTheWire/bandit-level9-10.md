#Bandit: Level 9 -> 10

##Goal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters.

##Solution
1. SSH onto the server with the username bandit9

2. list the contents and head the file (to show us the first few lines)

   ```
   bandit9@melinda:~$ ls
   data.txt
   bandit9@melinda:~$ head data.txt 
   **LOTS OF UNPRINTABLE CHARACTERS**
   ```

3. We can use `strings` and `grep` to grab matching lines

   ```
   bandit9@melinda:~$ strings data.txt | grep "==="
   I========== the6
   ========== password
   ========== ism
   ========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
   ```

Flag: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

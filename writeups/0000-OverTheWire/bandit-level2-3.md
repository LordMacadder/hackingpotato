#Bandit: Level 2 -> 3

##Goal
The password for the next level is stored in a file called spaces in this filename located in the home directory

##Solution
1. SSH onto the server with the username bandit2

2. List the home directory using `ls`

   ```
   bandit2@melinda:~$ ls
   spaces in this filename
   ```

3. Then cat the file escaping the spaces to give us the flag

   ```
   bandit2@melinda:~$ cat spaces\ in\ this\ filename 
   UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
   ```

4. Flag: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

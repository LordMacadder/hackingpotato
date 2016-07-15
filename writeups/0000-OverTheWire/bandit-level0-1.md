#Bandit: Level 0 -> 1

##Goal
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

##Solution
1. SSH onto the server with the username bandit

2. List the home directory using `ls`

   ```
   bandit0@melinda:~$ ls
   readme
   ```

3. Then cat the readme file to give us the flag

   ```
   bandit0@melinda:~$ cat readme
   boJ9jbbUNNfktd78OOpsqOltutMc3MY1
   ```

4. Flag: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

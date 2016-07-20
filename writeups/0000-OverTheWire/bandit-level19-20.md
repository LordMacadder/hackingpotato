#Bandit: Level 19 -> 20

##Goal
o gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used to setuid binary.

##Solution
1. SSH onto the server with the username bandit19

2. The binary executes as if it was being run by bandit20 so we just need to cat the correct password file

   ```
   bandit19@melinda:~$ ./bandit20-do 
     Run a command as another user.
     Example: ./bandit20-do id
   bandit19@melinda:~$ ./bandit20-do cat test
     cat: test: No such file or directory
   bandit19@melinda:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
     GbKksEFF4yrVs6il55v6gwY5aVje5f0j
   ```

Flag: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

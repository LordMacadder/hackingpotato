#Bandit: Level 4 -> 5

##Goal
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

##Solution
1. SSH onto the server with the username bandit4

2. List the home directory using `ls -a`

   ```
   bandit4@melinda:~$ ls
   inhere
   bandit4@melinda:~$ cd inhere/
  bandit4@melinda:~/inhere$ ls
   -file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
   ```

3. Using a bash one liner we can check the type of these files at once

   ```
   bandit4@melinda:~/inhere$ find ~/inhere -type f -exec file {} \;
   /home/bandit4/inhere/-file08: data
   /home/bandit4/inhere/-file05: data
   /home/bandit4/inhere/-file07: ASCII text
   /home/bandit4/inhere/-file04: data
   /home/bandit4/inhere/-file00: data
   /home/bandit4/inhere/-file01: data
   /home/bandit4/inhere/-file06: data
   /home/bandit4/inhere/-file03: data
   /home/bandit4/inhere/-file09: data
   /home/bandit4/inhere/-file02: data
   ```

4. There's our human readable text highlighted by the `ASCII text` output of the file command

   ```
   bandit4@melinda:~/inhere$ cat ./-file07
   koReBOKuIDDepwhWk7jZC0RTdopnAYKh
   ```

Flag: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

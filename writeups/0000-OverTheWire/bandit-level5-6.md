#Bandit: Level 5 -> 6

##Goal
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties: 

* human-readable 
* 1033 bytes in size 
* not executable

##Solution
1. SSH onto the server with the username bandit4

2. List the home directory using `ls -a`

   ```
   bandit5@melinda:~$ ls
   inhere
   bandit5@melinda:~$ cd inhere
   bandit5@melinda:~/inhere$ ls
   maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18
   maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19
   ```

3. Hmm so many folders/files, Using a bash one liner we should be able to do this in bulk

   ```
   bandit5@melinda:~/inhere$ find ~/inhere -type f -size 1033c -exec file {} \; | grep "text"
   /home/bandit5/inhere/maybehere07/.file2: ASCII text, with very long lines
   bandit5@melinda:~/inhere$ cat /home/bandit5/inhere/maybehere07/.file2
   DXjZPULLxYr17uwoI01bNLQbtFemEgo7
   ```

Flag: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

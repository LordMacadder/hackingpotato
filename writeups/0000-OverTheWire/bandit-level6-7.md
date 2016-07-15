#Bandit: Level 6 -> 7

##Goal
The password for the next level is stored somewhere on the server and has all of the following properties: 

* owned by user bandit7 
* owned by group bandit6 
* 33 bytes in size

##Solution
1. SSH onto the server with the username bandit6

2. Using a bash one liner we should be able to find matching files

   ```
   bandit6@melinda:~$ find / -type f -size 33c -user bandit7 -group bandit6 -readable 2>&1 | grep -v "Permission denied"
   find: `/proc/28377/task/28377/fd/5': No such file or directory
   find: `/proc/28377/task/28377/fdinfo/5': No such file or directory
   find: `/proc/28377/fd/5': No such file or directory
   find: `/proc/28377/fdinfo/5': No such file or directory
   /var/lib/dpkg/info/bandit7.password
   ```

3. Looks like we've found our file

   ```
   bandit6@melinda:~$ cat /var/lib/dpkg/info/bandit7.password
   HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
   ```

Flag: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

#Bandit: Level 17 -> 18

##Goal
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

##Solution
1. SSH onto the server with the username bandit17

2. Create a temp directory and concenate both passwords files into a single file

   ```
   bandit17@melinda:~$ mkdir /tmp/mossj
   bandit17@melinda:~$ cat passwords.old > /tmp/mossj/passwords.both
   bandit17@melinda:~$ cat passwords.new >> /tmp/mossj/passwords.both
   ```

3. Using our unique counter we can now find which lines only have one occurance

   ```
   bandit17@melinda:~$ sort /tmp/mossj/passwords.both | uniq -c | sort -bgr
      1 kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
      1 BS8bqB1kqkinKJjuxL6k072Qq9NRwQpR
   ```

4. Now we use grep to find which one is in the new password file

   ```
   bandit17@melinda:~$ grep "kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd" *                  
   passwords.new:kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
   ```

Flag: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

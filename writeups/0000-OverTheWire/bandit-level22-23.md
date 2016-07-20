#Bandit: Level 22 -> 23

##Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

##Solution
1. SSH onto the server with the username bandit22

2. First we take a look at the cron job and shell script

   ```
   bandit22@melinda:/etc/cron.d$ cat cronjob_bandit23
     * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
   bandit22@melinda:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
     #!/bin/bash
     myname=$(whoami)
     mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
     echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
     cat /etc/bandit_pass/$myname > /tmp/$mytarget
   ```

3. So it's generating an MD5 using a string and the username executing the script, then as last time putting the password into a temporary file based on the md5

4. Lets manually work out the hash

   ```
   bandit22@melinda:/etc/cron.d$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1 
   8ca319486bfbbc3663ea0fbe81326349
   ```

5. Then cat the file

   ```
   bandit22@melinda:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
   jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
   ```

Flag: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

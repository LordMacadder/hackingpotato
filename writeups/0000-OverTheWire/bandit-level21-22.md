#Bandit: Level 21 -> 22

##Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

##Solution
1. SSH onto the server with the username bandit21

2. First we cat the cronjob and then when it appears to be running a shell script that as well

   ```
   bandit21@melinda:/etc/cron.d$ cat cronjob_bandit22
     * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
   bandit21@melinda:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
     #!/bin/bash
     chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
     cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   ```

3. So it's putting the password into a tmp file, lets cat that

   ```
   bandit21@melinda:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
   ```

Flag: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

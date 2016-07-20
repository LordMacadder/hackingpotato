#Bandit: Level 18 -> 19

##Goal
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.
##Solution
1. We can tell ssh to execute a command as soon as it logs in (i.e before we are kicked off), so we simple send

   ```
   ssh bandit18@bandit.labs.overthewire.org cat readme
   ```

Flag: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

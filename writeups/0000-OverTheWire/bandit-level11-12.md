#Bandit: Level 11 -> 12

##Goal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

##Solution
1. SSH onto the server with the username bandit11

2. list the folder contents

   ```
   bandit11@melinda:~$ ls
   data.txt
   ```

3. As it's rot-13 we just apply the encode again to decode

   ```
   bandit11@melinda:~$ cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
   The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
   ```

Flag: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

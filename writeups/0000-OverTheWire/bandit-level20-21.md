#Bandit: Level 20 -> 21

##Goal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: To beat this level, you need to login twice: once to run the setuid command, and once to start a network daemon to which the setuid will connect.

NOTE 2: Try connecting to your own network daemon to see if it works as you think

##Solution
1. SSH onto the server with the username bandit20

2. Setup a listener on port 8888 using `nc -lvp 8888`

3. Log into another session and execute the binary `./suconnect 8888`

4. Now interact on the first terminal

   ```
   Listening on [0.0.0.0] (family 0, port 8888)
   Connection from [127.0.0.1] port 8888 [tcp/*] accepted (family 2, sport 51234)
   GbKksEFF4yrVs6il55v6gwY5aVje5f0j
   gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
   ```

Flag: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

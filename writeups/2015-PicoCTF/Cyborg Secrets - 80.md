#Cyborg Secrets - 80
You found a password protected binary on the cyborg relating to its defensive security systems. Find the password and get the shutdown code! You can find it on the shell server at /home/cyborgsecrets/cyborg-defense or you can download it here.

## Solution
1. Run strings against the binary and take a look to see if anything stands out
2. The string `2manyHacks_Debug_Admin_Test` stands out somewhat so lets try that `./cyborg_defense 2manyHacks_Debug_Admin_Test`
3. Yup that gives us the flag `403-shutdown-for-what`

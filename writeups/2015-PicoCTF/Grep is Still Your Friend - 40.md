#Grep is Still Your Friend - 40
The police need help decrypting one of your father's files. Fortunately you know where he wrote down all his backup decryption keys as a backup (probably not the best security practice). You are looking for the key corresponding to daedaluscorp.txt.enc. The file is stored on the shell server at /problems/grepfriend/keys .

## Solution
1. Navigate to the directory indicated in the challenge
2. grep for the key `grep "daedaluscorp.txt.enc" *`
3. which gives us our key `b2bee8664b754d0c85c4c0303134bca6`

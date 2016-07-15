#Bandit: Level 7 -> 8

##Goal
The password for the next level is stored in the file data.txt next to the word millionth

##Solution
1. SSH onto the server with the username bandit7

2. list the contents and head the file (to show us the first few lines)

   ```
   bandit7@melinda:~$ ls
   data.txt
   bandit7@melinda:~$ head data.txt
   Kunming's       0D0KZ3TdLRBXD8lyd7Bj2hAqnxaMInQe
   multitude's     8MFZa8yOjTt6m8PvxteTp7XTDFLiuFAk
   audibility      ZeLj0yAw7ylmEoLxSUEqF4iB43c9DN4h
   unadvised       Pgp8X2LSVdNrmIKcJ7Oe8eqTzEVfhGbR
   Brecht's        uKyKryNUZYFuTQpwRlDqucLLIUbiIMF0
   Alvin   IpQIV6mpjticdB790obqXAvYkAgnDV8E
   insufficient    cgHhWVJahfDqFIe82vOliryQQ8ihGlGN
   Sauterne        UhPBp0A04GkIRfvZnUt1UdwlKU2ViYUd
   cluster 1GeFZ0B6rsEtJ5Sqb5h8Wv7UwG15DQzb
   ember's f2XPIE1iDHW9oHPyodPyfTz87DAbWmXu
   ```

3. Looks like we can just grep for the target

   ```
   bandit7@melinda:~$ cat data.txt | grep "millionth"
   millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
   ```

Flag: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

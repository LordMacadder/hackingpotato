#Injection 1 - 90
Daedalus Corp. has been working on their login service, using a brand new SQL database to store all of the access credentials. Can you figure out how to login?

## Solution
1. On checking the source code this appears to be a fairly simple SQL injection
2. We need to hijack the username/password check so it always returns 1 row, to do this I used `' or 1=1 limit 1 -- `, which turns the query into `SELECT * FROM users WHERE username='' or 1=1 limit 1 -- ' AND password=''`
3. Giving us the flag `flag_vFtTcLf7w2st5FM74b`

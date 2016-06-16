#Function Address - 60
We found this program file on some systems. But we need the address of the 'find_string' function to do anything useful! Can you find it for us?

## Solution
1. Download the file, you can use the hosted terminal and your home directory `cd ~` then `wget https://picoctf.com/problem-static/reversing/function-address/problem`

2. Then dump the objects and grep for the function name `objdump -d problem | grep "find_string"`, which will output

   ```
   08048444 <find_string>:
   8048496:       eb 29                   jmp    80484c1 <find_string+0x7d>
   80484b6:       75 05                   jne    80484bd <find_string+0x79>
   80484bb:       eb 1a                   jmp    80484d7 <find_string+0x93>
   80484d0:       7d c6                   jge    8048498 <find_string+0x54>
   8048511:       e8 2e ff ff ff          call   8048444 <find_string>
   ```

3. There is our answer `08048444`

#Write Right - 50
Can you change the secret? The binary can be found at /home/write_right/ on the shell server. The source can be found here.

## Solution
1. So looking at the source we need to change the varible secret (using the address) to the value stored at the address `0x1337beef`

2. So we fire it up in gdb using `gdb write_right`, set a breakpoint on main using `b main`, then run using `run`

3. print the address of `secret` using `print &secret` which will output something like `$3 = (<data variable, no debug info> *) 0x804a03c <secret>`

4. Giving us the address of secret as `0x804a03c`

5. Type `continue` and enter the address to write to `804a03c`

6. Next enter the address to write there `1337beef`

7. You'll get the message `Woah! You changed my secret!` but then a seg fault caused by it running inside gdb

8. quit gdb and then rerun the programme using `./write_right`, entering the values we found

9. You get the flag `arbitrary_write_is_always_right`

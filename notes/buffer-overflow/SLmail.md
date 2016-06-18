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

9. 



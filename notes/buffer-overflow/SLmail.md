# SLmail Example Overflow

## Getting started
1. On the windows box install SLMail with all the default settings

2. Start your ssh server on your kali machine using `service ssh start` (so we can putty from the windows box to save us flipping backwards and forwards)

3. Connect to the windows box in full screen using the `-f` flag, if you need to minimize use `ctrl + alt + enter`

4. Using putty connect back to your kali box

5. Start the SLMail programme with administrator privs

6. Start Immunity Debugger and attach the SLMail process to it `File > Attach > Select from the list`

7. The debugger starts paused, so click the `play` icon in the top left

8. We can now run a fuzzer which just throws increasing amounts of capital `A` charaters at an particular input, see `pop3-sl-fuzzing.py`

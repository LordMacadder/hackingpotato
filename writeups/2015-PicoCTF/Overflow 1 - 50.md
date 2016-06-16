#Overflow 1 - 50
This problem has a buffer overflow vulnerability! Can you get a shell, then use that shell to read flag.txt? You can solve this problem interactively here, and the source can be found here.

## Solution (using the interactive solver)
1. Reviewing the source code we need to make `secret` equal `0xc0deface`

2. We start by creating the address (remember little edian so back to front) `\xce\xfa\xde\xc0`

3. This gives us our address and now we need to overflow the buffer until the address is in the correct place, we do this using `A` characters

4. Eventually we end up with `AAAAAAAAAAAAAAAA\xce\xfa\xde\xc0`

5. Running that overflows the buffer and gives us shell, after that we just run `ls` and then then `cat flag.txt`

6. Giving us the flag `ooh_so_critical`

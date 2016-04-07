#Bitwise: 55
You see the doors to the loading bay of the hangar, but they are locked. However, you are able to extract the password verification program from the control panel... Can you find the password to gain access to the loading bay?

Available in Python or Java 

## Solution
1. I chose the python route and after downloading the file I was unable to extract the meaning of `(((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 ` 
2. I then decided to work around this problem another way and wrote a quick python to bruteforce the equation and print out the values, the script is saved in this folder as `bitDecoder.py`
3. This gave me a list of ASCII characters and their values when the equation was run against them
4. After getting this table I then matched each character to the `verify_arr` inside the original python
5. This gave me the output `ub3rs3cr3t`

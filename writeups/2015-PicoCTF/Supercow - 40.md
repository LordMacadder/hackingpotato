# Supercow - 40
Daedalus Corp. has a special utility for printing .cow files at `/home/daedalus/supercow`. Can you figure out how to get it to print out the flag?

## Solution
1. On reading the source code we can see that we need to supply the name of a file ending in the extension `.cow`
2. Our flag file is `flag.txt` and we can't rename it, so maybe there is another way to refer to it...
3. Using symlinks of course! I can't create symlinks in the folder but found I have write permissions to `/tmp/`
4. I created the symlink `ln -s /home/daedalus/flag.txt /tmp/test.cow`
5. Then ran the programme `/home/daedalus/supercow /tmp/test.cow`
6. Giving me the flag `cows_drive_mooooving_vans`

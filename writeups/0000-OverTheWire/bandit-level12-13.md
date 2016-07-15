#Bandit: Level 12 -> 13

##Goal
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)
##Solution
1. SSH onto the server with the username bandit12

2. list the folder contents

   ```
   bandit11@melinda:~$ ls
   data.txt
   ```

3. Move the file over to a temporary place to work on it using `mkdir`, `cp` and `mv`

4. convert the hexdump back to a file

   ```
   bandit12@melinda:/tmp/working$ cat hexdump.txt | xxd -r > data.txt
   ```

5. Run `file` on this to see what we have

   ```
   bandit12@melinda:/tmp/working$ file data.txt
   data.txt: gzip compressed data, was "data2.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
   ```

6. Uncompress and then run file on the output, rinse and repeat until you get the output `data: ASCII text` from your file command

   For gzip
   ```
   bandit12@melinda:/tmp/working$ file data.txt
   data.txt: gzip compressed data, was "data2.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
   bandit12@melinda:/tmp/working$ mv data.txt data.gz
   bandit12@melinda:/tmp/working$ gzip -d data.gz
   ```
   
   For bzip
   ```
   bandit12@melinda:/tmp/working$ file data
   data: bzip2 compressed data, block size = 900k
   bandit12@melinda:/tmp/working$ bzip2 -d data     
   bzip2: Can't guess original name for data -- using data.out
   ```
   
   For tars
   ```
   bandit12@melinda:/tmp/working$ file data5.bin
   data5.bin: POSIX tar archive (GNU)
   bandit12@melinda:/tmp/working$ tar xvf data5.bin
   data6.bin
   ```

7. Once you have the ASCII output from a `file` command, just cat the file

   ```
   bandit12@melinda:/tmp/working$ cat data
   The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
   ```

Flag: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

#Bandit: Level 8 -> 9

##Goal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

##Solution
1. SSH onto the server with the username bandit8

2. list the contents and head the file (to show us the first few lines)

   ```
   bandit8@melinda:~$ ls
   data.txt
   bandit8@melinda:~$ head data.txt 
   yqtqjt2cJPMU6AEataMQSNmPtZuV7nX9
   vNPSh3f523D5gBq227a61BmWVMzKR0LP
   Rq22gxopbeTo3Rvb6UVDJFE6ws5r48fW
   wFSn4EAFCPktbfuvOAC0WaY0dARe2OF2
   Y6yngc3n7QWCaya5Qc90GGpBHHdXU41U
   3z96iN7exS00f8VyOYIOeEueZOVn631B
   4rzOkBIxrbWAmuEmhxn7tY4v1RvtdPbh
   SEWC4sWourdK3B7bBkfsipjsZu845VWV
   aFq7s4y4XgeQ6PY28YG2PftaUX9H9uJB
   qOeTH00nEaDkZwq16eg2i4Zx95zsiNe8
   ```

3. Quick bash one liner will count occurances and sort them for us

   ```
   bandit8@melinda:~$ sort data.txt | uniq -c | sort -bgr
     10 yuFfSTNzXeACMYRXVcxIbXVUvMk1cMKl
     10 yqtqjt2cJPMU6AEataMQSNmPtZuV7nX9
     ...cont...
     10 1JF4GVFmFLq7XT2mYPpCzEl2aT33zxfh
     10 0dJUVh7xSLq6OkSLaxUydzRBVVJlc78x
      1 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
   ```

Flag: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

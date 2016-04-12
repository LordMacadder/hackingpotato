#Locate, Which, Find

## Locate
Locate allows you to find files, when using it you should always run `updatedb` first

```
root@kali:~# updatedb
root@kali:~# locate plink.exe
/usr/share/windows-binaries/plink.exe
```

## Which
Which will search through folders specified in the $PATH enviroment varible and returns the full path to the file.

```
root@kali:~# which sbd
/usr/bin/sbd
```

## Find 
Find is a far more agressive search tool that can be used to recursively search a folder for subfolders or files.

```
root@kali:~# find / -name plink*
/usr/share/windows-binaries/plink.exe
/usr/share/doc/texlive-latex-extra-doc/latex/program/plink.tex
/usr/share/doc/texlive-doc/latex/program/plink.tex
```

## Using your new knowledge find documentation for DNSENUM

```
root@kali:/# find / -name dnsenum*
/usr/bin/dnsenum
/usr/share/doc/dnsenum
/usr/share/dnsenum
/var/lib/dpkg/info/dnsenum.list
/var/lib/dpkg/info/dnsenum.md5sums
root@kali:/# cd /usr/share/doc/dnsenum/
root@kali:/usr/share/doc/dnsenum# ls
changelog.Debian.gz  copyright  README.md
root@kali:/usr/share/doc/dnsenum# nano README.md 
```

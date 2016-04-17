#Netcat Basics

## Banner Grabbing
Netcat can be used to grab banners by simply initializing a connection, for examples for IMAP port 143

```nc IP.AD.DR.ESS 143````

## Intializing a chat client

### Server side (windows box)
make sure the netcat executable is in the windows directory then use the following to create a listening server on port 8080

```nc -nlvp 8080```

### Client side (kali box)
With the sever listening you can initialize a connection using

```nc -nv IP.AD.DR.ESS 8080```

## Transfering files
You can also use netcat to transfer files to and from boxes

### Server side (windows box)
Create a listener on 8080 and put any input into a file

```nc -nlvp 8080 > wget.exe```

### Client side (kali box)
With the sever listening send the file

```nc -nv IP.AD.DR.ESS 8080 < /usr/share/windows-binaries/wget.exe```



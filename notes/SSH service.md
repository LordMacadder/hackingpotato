# SSH

## To start SSH in your Kali VM
Run `service ssh start`

## Veryify that it's running
Use the netstat command as follows
```
root@kali:/# netstat -antp|grep sshd
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      4084/sshd       
tcp6       0      0 :::22                   :::*                    LISTEN      4084/sshd 
```

## To stop SSH
Run `service ssh stop`

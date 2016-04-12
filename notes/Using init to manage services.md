#Init.d to manage services
The `service` command is just a wrapper around init.d strings

You can also use these commands to start/stop services directly

```
root@kali:/# /etc/init.d/ssh start
[ ok ] Starting OpenBSD Secure Shell server: sshd.
root@kali:/# /etc/init.d/ssh stop
[ ok ] Stopping OpenBSD Secure Shell server: sshd.

```

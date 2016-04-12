#Boot Persistence
Boot persistence is managed by the update-rc.d command

To enable services to start on boot use the following
```
root@kali:/# update-rc.d ssh enable
update-rc.d: using dependency based boot sequencing
root@kali:/# update-rc.d apache2 enable
update-rc.d: using dependency based boot sequencing
```

To disable services to start on boot use the following
```
root@kali:/# update-rc.d ssh disable
update-rc.d: using dependency based boot sequencing
root@kali:/# update-rc.d apache2 disable
update-rc.d: using dependency based boot sequencing
```

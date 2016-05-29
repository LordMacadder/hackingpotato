# Linux Buffer Overflow

## Setup

1. Setup your IPTABLE rules as below, this stops traffic from other hosts and only allows localhost traffic
   ```
   root@kali:~# iptables -A INPUT -p TCP --destination-port 13327 \! -d 127.0.0.1 -j DROP
   root@kali:~# iptables -A INPUT -p TCP --destination-port 4444 \! -d 127.0.0.1 -j DROP
   ```

2. Load the vunerable application (crossfire) using edb (Evans DB) `root@kali:~# edb --run /usr/games/crossfire/bin/crossfire` 

3. The application is loaded in a paused state, so hit the run button twice

4. 

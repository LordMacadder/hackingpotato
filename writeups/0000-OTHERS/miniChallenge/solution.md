# Minichallenge Solution

1. On opening the file you can see we have a pcap file, two python scripts and a .crypt file

2. We start by taking a look at what we have by analysing the pyhon scripts we can see that decrypt.py is expecting some sort of key, and that trash.py was used to encrypt the original file

3. So we need to understand just how the key was generated, a closer inspection of trash.py reveals a few key lines.

   ```python
def transmit_key(key):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 1234))
    s.sendto('START', ('192.168.1.201', 1234))
    for ch in key:
        delay = 5.0 if ch == 'A' else 10.0
        time.sleep(delay)
        s.sendto('SOMETHING', ('192.168.1.201', 1234))
    s.sendto('END', ('192.168.1.201', 1234))
```

   So from this it looks like the key was sent to 192.168.1.201, starting with `START` and ending with `END` with the key (A OR B) in the middle being dictated by the `SOMETHING` frames and the timing

4. Most likely this is what the pcap file was for so lets open that up in wireshark and take a look at the individual timing of frames

5. After looking at the UDP packets between frames 1-48 (specifically looking at the timing column and the teme between each frame) we can work out the key is `BABAAAAABABBAABB`

6. Put that into our decrypt.py and run it, gives us the original pdf document which we can now open

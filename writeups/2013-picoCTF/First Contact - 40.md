#First Contact: 40
You notice that the indicator light near the robot’s antenna begins to blink. Perhaps the robot is connecting to a network? Using a wireless card and the network protocol analyzer Wireshark, you are able to create a PCAP file containing the packets sent over the network.

You suspect that the robot is communicating with the crashed ship. Your goal is to find the location of the ship by inspecting the network traffic.

You can perform the analysis online on Cloudshark or you can download the PCAP file.

##Write up
1. So open up the PCAP in Cloudshark (or Wireshark), I used Cloudshark in this instance (as I'd used Wireshark before)
2. Highlight one of the TCP packets, then follow the stream `Analysis Tools > Follow Stream`
3. This will give you the text sent in the packets

```
ROBOT BOOTUP INITIALIZING
SPACE SHIP READY
BOOTUP BEGIN
FIRMWARE STATUS.... COMPLETE
LOCATION STATUS.... ERROR
****BOOT ERROR****
COULD NOT READ FROM DISK ID 0xEF982DA0
INITIALIZE RECOVERY PROCEDURE 0xCD950422
PROCEDURE 0xCD950422 STATUS.... COMPLETE
AWAITING NEW LOCATION STATUS
NEW LOCATION STATUS: 302
NEW LOCATION COORDINATES: 37 14'06"N 115 48'40"W
NEW LOCATION INFO: LOCKED
NEW LOCATION UPDATE COMPLETE
NEW LOCATION UPDATE SUCCESS
```

4. There's our answer `37 14'06"N 115 48'40"W`

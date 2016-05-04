#Spoof Proof - 60
The police have retrieved a network trace of some suspicious activity. Most of the traffic is users viewing their own profiles on a social networking website, but one of the users on the network downloaded a file from the Thyrin Labs VPN and spoofed their IP address in order to hide their identity. Can you figure out the last name of person that accessed the Thyrin files, and the two source IP addresses they used?
[Example valid flag format: "davis,192.168.50.6,192.168.50.7"]

PCAP file available here. You can also view it on CloudShark

##Solution
1. Looking in cloud shark we can see a get request for `secretfile.txt` in frame 58, made by ip `192.168.50.4` with the mac address `08:00:27:2b:f7:02`
2. We can then look through the frames and find another request using that mac address with a new ip `192.168.50.3`
3. This ip address accesses the social media site of `John Johnson`
4. Giving us the key `Johnson,192.168.50.3,192.168.50.4`

#TCP Connect Scan
Using `nc -nvv -w 1 -z IP.AD.D.RES 3385-3395`

#UDP Scan
`netcat -unvv -w 1 -z 10.11.1.227 160-165`

UDP is considered unrealible due to a relience on returned ICMP packets which can get dropped

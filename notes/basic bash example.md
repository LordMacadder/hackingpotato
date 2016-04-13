#Basic Bash
This script was written simple to pull out all the subdomains from the cisco.com homepage

1. Download the homepage using `wget http://www.cisco.com`

2. You can find all the href links using `cat index.html | grep "href="` but it's still to messy

3. Okay well let's cut the line and extract the information between the third slash `cat index.html | grep "href=" | cut -d "/" -f3 | more
`

4. This is giving us odd domains so lets grep for cisco.com instead `cat index.html|grep "cisco\.com" | cut -d "/" -f3 | more`

5. Still getting odd quote marks at the end, lets cut those out `cat index.html|grep "cisco.com" | cut -d "/" -f3 | cut -d '"' -f1
`

6. Lets use the sort command to dedup our list `cat index.html|grep "cisco.com" | cut -d "/" -f3 | cut -d '"' -f1 | sort -u`

## Of course we could further simplify this by using regex, so the above can become
1. `grep -o '[A-Za-z0-9_\.-]*\.*cisco.com' index.html | sort -u`

2. Now it's nice and neat lets pipe the output `grep -o '[A-Za-z0-9_\.-]*\.*cisco.com' index.html | sort -u > cisco.txt`

## Now that we have a list lets pull the IPs
1. Looking at the `host` command we see that we need the following to extract the ip `host www.cisco.com | grep "has address" | cut -d " " -f4
`
2. Using bash lets look up all the host ips in bulk from our cisco.txt file, create an executable `.sh` file with the below and run it

   ```
   #!/bin/bash
   for url in $(cat cisco.txt);do
    host $url | grep "has address" | cut -d " " -f4
   done
   ```

3. Of course we could of just used a one liner to do ALL of this `for url in $(grep -o '[A-Za-z0-9_\.-]*\.*cisco.com' index.html | sort -u);do host $url | grep "has address" | cut -d " " -f4; done`





#Natas: Level 7 -> 8

##Goal
Username: natas7
URL:      http://natas7.natas.labs.overthewire.org/index.php

##Solution
1. Visit the page and you are given pages to view, on clicking though we notice it's appending a parameter to the URL

2. If we view the source we are given the path to a file containing secret

3. So all we need to do is include it in the url `/index.php?page=/etc/natas_webpass/natas8`, giving us the password `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`

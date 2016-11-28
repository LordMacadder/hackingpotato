#Natas: Level 4 -> 5

##Goal
Username: natas4
URL:      http://natas4.natas.labs.overthewire.org/index.php

##Solution
1. Start up burp and configure your proxy

2. Visit the page, forward the request, then click the refresh link

3. In this request modify the referrer to `Referer: http://natas5.natas.labs.overthewire.org/index.php`

4. You should now see the password `iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`

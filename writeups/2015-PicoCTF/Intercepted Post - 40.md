#Intercepted Post - 40 
We intercepted some of your Dad's web activity. Can you get a password from his traffic?. You can also view the traffic on CloudShark. 

## Solution
1. Opening the cloudshark we see loads of wikipedia which we can safely assume is fluff, scrolling through frame 125 jumps out at me as it's a login form
2. Scrolling slightly beyond we see a post to `/login/`, follow that TCP stream and we see `username=claudio&password=password` giving us the flag `password`
3. But it doesn't work a bit more scrolling and we see another post to the `/login/` page, which gives us `username=claudio&password=flag%7Bpl%24_%24%24l_y0ur_l0g1n_form%24%7D`
4. Not done yet we need to [decode the password](http://meyerweb.com/eric/tools/dencoder/) `flag%7Bpl%24_%24%24l_y0ur_l0g1n_form%24%7D` to give us the flag `flag{pl$_$$l_y0ur_l0g1n_form$}`

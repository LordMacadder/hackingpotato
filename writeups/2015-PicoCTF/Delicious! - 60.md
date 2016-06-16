# Delicious! - 60
You have found the administrative control panel for the Daedalus Coperation Website: https://web2014.picoctf.com/delicious-5850932/login.php. Unfortunately, it requires that you be logged in. Can you find a way to convince the web site that you are, in fact, logged in?

## Solution
1. We note we are given a session number (in my case 67)

2. It appears this session id is stored as a cookie in the browser

3. We can modify this cookie to steal another session, in Google Chrome this involves using `document.cookie = "session_id=66"` in the console

4. Refresh the page and we get our flag `session_cookies_are_the_most_delicious`

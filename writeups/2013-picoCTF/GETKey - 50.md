#GETKey: 50
There's bound to be a key on the spaceport's hidden website

##Answer
1. On visiting the site we can see a button labeled `Get Key` lets push it!
2. Shame looks like we didn't get the key but we did get the message `Either you aren't admin or wrong competition`
3. On checking the URL we can see a get request was sent adding the following to the end of the url `?admin=false&competition=ccdc`
4. Lets alter this to `?admin=true&competition=picoctf` and go to that url
5. Viola our key is revealed `9fa449c061d64f58de600dfacaa6bd5d`

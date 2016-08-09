#Leviathan: Level 0

##Goal
Username: leviathan0
Password: leviathan0

##Solution
1. Looks like an empty directory until we do `ls -a` which highlights a few files/directories including `.backup`

2. On inspecting `.backup` we can see a html file that seems to be a list of links

3. After inspecting the file (either by hand or by grep) we can find the line `<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" A
DD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>`

4. Giving us the password: rioGegei8m

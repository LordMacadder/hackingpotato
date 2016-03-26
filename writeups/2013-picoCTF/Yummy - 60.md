#Yummy: 60
You want to find out the docking bay numbers for space ships that are ready to launch. Luckily for you, the website for the docking bay ship status page doesn't seem so secure....

Enter the docking bay for any of the ships that are awaiting launch.

##Answer
1. We go to the website in a normal browser and all seems like you would expect
2. However right click on the webpage and click "view source" which gives us access to comments "hidden" on the page 

   ```
<!-- DEBUG: Expected Cookie: "authorization=administrator"
received Cookie: "SNIP" -->
```

3. Lets give it what it's expecting and change our cookie using the developer tools console on Google Chrome (press F12, go to the console tab), the specific command we need is `document.cookie="authorization=administrator"`
4. We refresh the page and are given a table of waiting ships, I used `DX6-7` as the flag

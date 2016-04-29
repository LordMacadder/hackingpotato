#Toaster Control - 50
Daedalus Corp. uses a web interface to control some of their toaster bots. It looks like they removed the command 'Shutdown & Turn Off' from the control panel. Maybe the functionality is still there...

##Solution
1. Access the website and click one of the buttons, we can see that it points to `http://web2014.picoctf.com/toaster-control-1040194/handler.php?action=Blink%20Lights`
2. So the key is to turn that into `http://web2014.picoctf.com/toaster-control-1040194/handler.php?action=*SHUTDOWNCOMMANDHERE*`
3. After some trial and error we find that the correct url is `http://web2014.picoctf.com/toaster-control-1040194/handler.php?action=Shutdown%20%26%20Turn%20Off`
4. Which gives us the flag `flag_c49bdkeekr5zqgvc20vc`

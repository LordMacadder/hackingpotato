#Natas: Level 8 -> 9

##Goal
Username: natas8
URL:      http://natas8.natas.labs.overthewire.org/index.php

##Solution
1. Visit the page and you are prompted to enter a secret

2. On inspecting the source code we can see the input is encoded before being compared to the secret

3. We create a php page to reverse this

    ```
    <?php
    
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";

    function decodeSecret($secret) {
        //return bin2hex(strrev(base64_encode($secret)));
        return base64_decode(strrev(hex2bin($secret)));
     }

     echo decodeSecret($encodedSecret);
     ```

3. Which gives us the secret, which we then enter on the index to reveal the password `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`

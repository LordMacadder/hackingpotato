#Javascrypt - 40
Tyrin Robotics Lab uses a special web site to encode their secret messages. Can you determine the value of the secret key?

## Solution
1. Using your browser tools inspect the button which is coded as follows `<a href="#" onclick="encode()">Encode</a>`

2. From this we can see it calls a javascript function called `encode` which looks like this

   ```
    // Encode the message using the 'key'
    function encode() {                                                        
        var input = $("#inputmessage").val();
        var output = CryptoJS.AES.encrypt(input, key);
        $("#outputmessage").val(output);
    }
  ```

3. We can see it accesses a varible called `key` so we run `alert(key)` in our console to get the key outputted in this case `flag_300`

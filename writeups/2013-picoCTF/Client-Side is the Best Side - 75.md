#Client-Side is the Best Side: 75
Luckily the ship has a web-based authentication system! Hmm…even though you don't know the password, I bet you can still get in!

## Solution
1. Right click and view source of our login page

2. By examining the code we can see

   ```
   <script type="text/javascript">
   function verify() {
       checkpass = document.getElementById("pass").value;
       if (md5(checkpass) == "03318769a5ee1354f7479acc69755e7c") {
         alert("Correct!");
         document.location="./aebe515f7c62b96ad7de047c11aa3228.html";
        }
        else {
         alert("Incorrect password");
        }
    }
   </script>
   ```

3. The key line is not the MD5 but `document.location="./aebe515f7c62b96ad7de047c11aa3228.html";`, on password validation the js will redirect to this page.

4. Lets just go to that page through our browser and there is our key `Key: cl13nt_s1d3_1s_w0rst_s1d3`

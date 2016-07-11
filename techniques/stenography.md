# Images
* Open file and look
* Run `file`
* Run `binwalk`, if anything extract it using `binwalk -e`
* Run `exiftool`
* Open in text editor check start/end for markers
* If .gif run `convert`
* Run stegsolve.jar
* Check LSB

**Interesting CTF Challenges**
* https://github.com/ctfs/write-ups-2015/tree/master/th3jackers-ctf-2015/stegano/steg300 (lots of different steg techniques png/jpg/gif)
* 

# Sound
* Open file and listen
* Run `file`
* Run `binwalk`, if anything extract it using `binwalk -e`
* Check metadata
* Check LSB
* Check for multiple channels
* Open in Audacity and check spectogram
* Slow down file 
* Analyze waveform to see if it's binary

**Interesting CTF Challenges**
* https://shrikantadhikarla.wordpress.com/2016/03/08/lily-flac-writeup-boston-key-party-ctf/ (Found executable in .wav)
* https://ethackal.github.io/2015/10/05/derbycon-ctf-wav-steganography/ (LSB with .wav)
* https://ctfcrew.org/writeup/91 (Flag hidden in channel differences of .wav)
* https://eindbazen.net/2012/05/plaid-ctf-2012-debit-or-credit/ (binary data hidden in waveform of .wav)
* https://travisroyer.wordpress.com/2015/03/14/n00bs-ctf-labs-level-10-solution/ (data hidden in high pitch noise, found by slowing down .wav)
* Recover a phone number from audio recording of it being dialed (http://nopsr.us/ctf2006prequal/walk-forensics.html)
* 

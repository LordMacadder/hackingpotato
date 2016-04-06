# Hidden file in png

Download the image thatNoMoonImage.png

## Solution

1. Download the image
2. Run `binwalk moon.png -e`
3. In the extraction directory there will be a zip file (64885.zip).
4. This contains a file flag.txt, but is password protected.
5. Crack password using `fcrackzip -b -c a -l 1-12 -u '64885.zip'`
6. Extract `flag.txt` using the password ('moon')

## Other Writeups
* https://github.com/d0tslashpwn/write-ups/blob/master/Sunshine-CTF-2016/write-ups/thats_no_moon.md - Used strings/unzip
* https://github.com/tsunnyday/ctf-writeups/blob/master/SunshineCTF_2016/moon/writeup.txt - Used Foremost
* http://err0r-451.ru/2016-sunctf-forensics-thats-no-moon-50-pts/ - Used John The Ripper to break password
* https://0day.work/sunshine-ctf-2016-writeups/#thatsnomoon - Used DD to extract the zip

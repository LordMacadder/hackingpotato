#!/usr/bin/python
import wave
from scipy.io.wavfile import read

# Built from https://ctfcrew.org/writeup/91
# sudo apt-get install python-scipy < if you get library error


if len(sys.argv) != 1:
	print "Usage smtp-enum.py <wavfile>"
	sys.exit(0)

file = sys.argv[1];

w = wave.open(file, 'r')
print 'n of channels:'
print w.getnchannels()
 
n = w.getnframes()
print 'n of frames:'
print n
frames = w.readframes(n)
print 'len(frames):'
print len(frames)
 
(fs, x) = read(file)
print fs
print len(x.shape)
print x[:,0]
print x[:,1]
 
c1 = x[:,0]
c2 = x[:,1]
d = []
for a, b in zip(c1, c2):
    d.append(b - a)
print d[0:100]

# if it all appears to be printable, uncomment and this will attempt to write it to file
#out = open('result.txt', 'wb')
#for t in d: out.write(chr(t))
#out.close()

# coding: utf-8 
import sys 
import re 

def get_zlib_data(filepath): 
    f = file(filepath,"rb") 
    d = f.read() 
    f.close() 
    return d 

if __name__ == '__main__': 
    if len(sys.argv) > 1: 
        print sys.argv[1] 
        g = get_zlib_data(sys.argv[1]) 
        s = re.search('\x78\x9c',g,re.MULTILINE) 
        if s: 
            d = g[s.start():len(g)] 
            data = d.decode("zlib") 
            f = file(sys.argv[1]+".dec","wb") 
            f.write(data) 
            f.close() 
            print "Success! Decode Zlib Data To " + sys.argv[1]+ ".dec" 
        if not s: 
            print "No Zlib Data Found" 
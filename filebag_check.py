#!/usr/bin/env python

import os,sys

def parseManifest(path):
    with open(path,'r') as f:
        lines = [s.split("  ",1) for s in f.readlines()]
    (hashes,paths,fnames) = ([],[],[])
    for line in lines:
        hashes.append(line[0])
        paths.append(line[1])
        fnames.append(os.path.basename(line[1]).rstrip("\n"))
    return (hashes,paths,fnames)

(h1,p1,f1) = parseManifest(sys.argv[1])

print("entries: {}".format(len(h1)))
print("unique fcontents: {}".format(len(set(h1))))
print("unique fnames: {}".format(len(set(f1))))
print("unique paths: {}".format(len(set(p1))))



    

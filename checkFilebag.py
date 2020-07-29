#!/usr/bin/env python

import os,sys

with open(sys.argv[1],'r') as f:
    lines = [s.split("\t") for s in f.readlines()]


(hashes,paths,fnames) = ([],[],[])
for line in lines:
    hashes.append(line[0])
    paths.append(line[1])
    fnames.append(line[2])

print("entries: {}".format(len(lines)))
print("unique fcontents: {}".format(len(set(hashes))))
print("unique fnames: {}".format(len(set(fnames))))
print("unique paths: {}".format(len(set(paths))))



    

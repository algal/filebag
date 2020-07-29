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
(h2,p2,f2) = parseManifest(sys.argv[2])

hs1 = set(h1)
fs1 = set(f1)

hs2 = set(h2)
fs2 = set(f2)

fsint = fs1.intersection(fs2)
fs12 = fs1.issubset(fs2)
fs21 = fs2.issubset(fs1)

if len(fsint) == 0:
    print("A and B have no file names in common")
elif fs12 and fs21:
    print("A and B have identical file names")
elif fs12:
    print("A's file names is a subset of B's file names")
elif fs21:
    print("B's file names is a subset of A's file names")
else:
    print("No containment relationship between A and B's file names.\n Intersction: {}\n Items: {}".format(len(fsint),sorted(list(fsint))))

print("")

hsint = hs1.intersection(hs2)
hs12 = hs1.issubset(hs2)
hs21 = hs2.issubset(hs1)

if len(hsint) == 0:
    print("A and B have no file contents in common")
elif hs12 and hs21:
    print("A and B have identical file contents")
elif hs12:
    print("A's file contents is a subset of B's file contents")
elif hs21:
    print("B's file contents is a subset of A's file contents")
else:
    print("No containment relationship between A and B's file contents.\n Intersction: {}\n Items: {}".format(len(hsint),sorted(list(hsint))))


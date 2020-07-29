#!/usr/bin/env/python

import os,sys

def parseManifest(path):
    with open(path,'r') as f:
        lines = [s.split("\t") for s in f.readlines()]
    (hashes,paths,fnames) = ([],[],[])
    for line in lines:
        hashes.append(line[0])
        paths.append(line[1])
        fnames.append(line[2])
    return (hashes,paths,fnames)

(h1,p1,f1) = parseManifest(sys.argv[1])
(h2,p2,f2) = parseManifest(sys.argv[2])

hs1 = set(h1)
fs1 = set(f1)

hs2 = set(hs2)
fs2 = set(f2)

hs12 = hs1.issubset(hs2)
hs21 = hs2.issubset(hs1)

if hs12 and hs21:
    print("A and B have identical file contents")
else if hs12:
    print("A's file contents is a subset of B's file contents")
else if hs21:
    print("B's file contents is a subset of A's file contents")
else:
    print("No simple relationship between A and B's file conents")

fs12 = fs1.issubset(fs2)
fs21 = fs2.issubset(fs1)




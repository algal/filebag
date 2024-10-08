#!/usr/bin/env python3

import os,sys

def parseManifest(path):
    with open(path,'r') as f:
        lines = [s.split("  ",1) for s in f.readlines()]
    (hashes,paths,fnames) = ([],[],[])
    for line in lines:
        hashes.append(line[0])
        paths.append(line[1].rstrip("\n"))
        fnames.append(os.path.basename(line[1].rstrip("\n")))
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
    print("The file names in A ({}) are a subset of the file names in B ({})".format(sys.argv[1],sys.argv[2]))
elif fs21:
    print("The file names in B ({}) are a subset of the file names in A ({})".format(sys.argv[2],sys.argv[1]))
else:
    print("No containment relationship between A and B's file names.\n Intersection: {}\n Items: {}".format(len(fsint),sorted(list(fsint))))

print("")

hsint = hs1.intersection(hs2)
hs12 = hs1.issubset(hs2)
hs21 = hs2.issubset(hs1)

if len(hsint) == 0:
    print("A and B have no file contents in common")
elif hs12 and hs21:
    print("A and B have identical file contents")
elif hs12:
    print("The file contents in A ({}) are a subset of the file contents in B ({})".format(sys.argv[1],sys.argv[2]))
elif hs21:
    print("The file contents in B ({}) are a subset of the file contents in A ({})".format(sys.argv[2],sys.argv[1]))
else:
    print("No containment relationship between A and B's file contents.\n Interesction: {}\n Items: {}".format(len(hsint),sorted(list(hsint))))


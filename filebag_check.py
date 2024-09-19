#!/usr/bin/env python3

import os,sys

def makeKeyDict(items):
    "Gives a list of tuples (A,B), returns a dict mapping A to a set of Bs"
    d = {}
    for (a,b) in items:
        d[a] = set([b]).union(d.get(a,set()))
    return d
    
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

print("entries: {}".format(len(h1)))
print("unique fcontents: {}".format(len(set(h1))))
print("unique fnames: {}".format(len(set(f1))))
print("unique paths: {}".format(len(set(p1))))
print("")

kdpf = makeKeyDict(zip(f1,p1))
kdpfd = {k:v for k,v in kdpf.items() if len(v) > 1}
if len(kdpfd.items()) > 0:
    print("Some filenames are appearing repeatedly at different paths:\n {}\n".format(kdpfd))

kdfh = makeKeyDict(zip(h1,f1))
kdfhd = {k:v for k,v in kdfh.items() if len(v) > 1}
if len(kdfhd.items()) > 0:
    print("Different filenames are being used to refer to the same file contents:\n {}\n".format(kdfhd))


    

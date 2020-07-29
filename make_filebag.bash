#!/bin/bash
find "$1" -iname '*jpg' -print0 | xargs -0 -n 100 md5sum | python -c '
import sys,os
for line in sys.stdin:
 ss = line.strip().split(maxsplit=1)
 print( "\t".join(ss + [os.path.basename(ss[1])]))
'
# the python part is slow. how to fix?



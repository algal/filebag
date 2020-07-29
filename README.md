# Filebag tools

A "file bag" is a manifest describing a collection of paths to jpg files on disk.

You create a filebag manifest by running:

    ./filebag_make.bash /path/to/root/of/images

Once you have a file bag, you can perform the following operations by running `filebag_check.py`:

1. Check if every fname (file name) uniquely identifies fcontents (file contents). If not, then the same fname is used to identify different file contents.

2. Check if every fname uniquely identifies its path. If not, then the same fname appears repeatedly at different paths.

Once you have two manifests for file bags A and B, you run `filebag_compare.py` to answer the following questions regarding the file names and regarding file contents in A and B? 

2. Does B contain all of A? A

3. Are A and B entirely disjoint?





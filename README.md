# Filebag tools


A "file bag" is a manifest describing a collection of paths to jpg files on disk.

You create a *filebag manifest* by running:

    ./filebag.bash /path/to/root/of/images

Once you have one manifest representing a file bag, you can perform the following operations by running `check_filebag`:

1. Check if every fname (file name) uniquely identifies fcontents (file contents). If not, then the same fname is used to identify different file contents.


2. Check if every fname uniquely identifies its path. If not, then the same fname appears repeatedly at different paths.

Once you have two manifests for file bags A and B, you run `compare_filebags.py` to answer the following questions about the file names in A and B and the file conents in A and B:

1. Does A contain all of B? 

2. Does B contain all of A? A

3. Are A and B entirely disjoint?





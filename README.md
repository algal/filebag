# Filebag tools

The file bag scripts are for managing large quantities of image files, by helping you to verify if files are unnecessarily duplicated within a directory or across different sets of directories, or if the same images appears repeatedly under different file names.

## How to use

A "file bag" is a manifest describing a collection of paths to jpg files on disk.

You create a filebag manifest by running:

    ./filebag_make.bash /path/to/root/of/images > mypath.filebag

Once you have a file bag, you can perform the following operations by running `filebag_check.py`:

1. Check if every file name uniquely identifies its path. If not, then the same file name appears repeatedly at different paths.

2. Check if every file name uniquely identifies file contents. If not, then the same file name is being used to identify different file contents at different paths.

However, beware: these file contents checks are done only by looking at MD5 hashes, so they will occasionally (but rarely) fail when different files yield the same hash value.

Once you have two manifests for file bags A and B, you run `filebag_compare.py` to answer the following questions regarding the file names and regarding file contents in A and B? 

2. Does A contain all of B? (That is, is B a subset of A?)

3. Are A and B entirely disjoint? (That is, do they have zero intersection?)

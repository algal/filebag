# Filebag tools


A "file bag" is a collection of paths to jpg files on disk.

You create a *filebag manifest* by running:

    ./filebagManifest.bash /path/to/root/of/images

Once you have one manifest representing a file bag, you can perform the following operations:

1. Check if every fname (file name) uniquely identifies fcontents (file contents). If not, then the same fname is used to identify different file contents.

   ./checkFilebag.py /path/to/manifest   

2. Check if every fname uniquely identifies its path. If not, then the same fname appears repeatedly at different paths.

Once you have two manifests for file bags A and B, you can answer the following questions:

1. Does B contain any fnames that exist in A?

2. Does B contain any fcontents that exist in A?



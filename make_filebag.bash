#!/bin/bash
exec find "$1" -iname '*jpg' -print0 | xargs -0 -n 100 md5sum

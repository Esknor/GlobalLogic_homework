#!/bin/bash
path=$1
test -f $path && echo "privet" ||  test -d $path && echo "privet" || echo "poka" 


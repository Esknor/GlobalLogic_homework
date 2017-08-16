#!/bin/bash
path=$1

if cat $path ; then
	echo "hello"
else 
	echo "poka"
fi

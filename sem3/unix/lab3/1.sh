#!/bin/bash

if [ $# -eq 0 ];then
	echo "Error!"
else 
	if [ -d $1 ];then
		ls -l $1
	elif [ -f $1 ];then
		cat $1
	else
		echo "file/dir doeasnt exist"
	fi
fi
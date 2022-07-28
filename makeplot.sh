#!/bin/sh

for i in */; do
        cd $i
	bash operation.sh
        cd ../
done

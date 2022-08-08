#!/bin/sh

for i in *data/; do
        cd $i
	# cp ../operation.sh ./
	bash operation.sh
        cd ../
done

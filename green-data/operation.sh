#!/bin/sh

for i in */; do
        cd $i
	TRIMMED=$(echo $i | sed 's:/*$::')
        str1="${TRIMMED}"
	python3 /Users/zhangzhenzhe/Desktop/Quasicrystal/mols/First-mole/Subs/blue-data/band.py $str1
        cd ../
done

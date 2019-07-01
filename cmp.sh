#!/bin/bash
echo "######################################"
echo "#enter python <file.py> <input.in>   #"
echo "#enter python $1, $2                 #"
echo "######################################"

`cp $2 tmp`
file="$(echo $1 | cut -d'.' -f1)"
input=$2

for i in $(seq 10)
do

  `cp $i.in $2`

  #echo "running python $file.py $input"

  python $file.py $input

  `cp $file.out out.$i`



  `cmp --silent $i.out out.$i` && echo "file $i.out, out.$i are same." || echo "file $i.out, out.$i are different."

done
`mv tmp $2`
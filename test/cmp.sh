#!/bin/bash
echo "######################################"
echo "#enter python <file.py> <input.in>   #"
echo "#enter python $1, $2                 #"
echo "######################################"
file = $1
`cp file tmp.in`

for i in $(seq 10)
do

  `python $1 $2`

done

for i in $(seq 10)
do

  `cmp --silent O.$i output.$i` && echo "file O.$i, output.$i are same." || echo "file O.$i, output.$i are different."
done


for i in $(seq 10)
do
  
  `cmp --silent O.$i output.$i` && echo "file O.$i, output.$i are same." || echo "file O.$i, output.$i are different."
done
`cp tmp.in file`

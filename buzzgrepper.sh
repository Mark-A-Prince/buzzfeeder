#!/bin/bash

#----------------------Run Python Script
python buzzer.py > buzzListRaw.txt #<---- run the python script, output into text file

#----------------------Make New Document with Only Titles-------------------------
grep "rel:data" buzzListRaw.txt |cut -d ':' -f5 > buzzGrep.txt #<---- search the text file for string "rel:data", then use a ':' as a delimiter to extract string for the "name:"

#---------------------Extract and Print Data---------------------------
for((i=0; i < 100; i++)) #<---- For loop to search for numbers 1-100 in the "grepped" buzzGrep.txt
do
  grep -w $i buzzGrep.txt|wc -l > tempy #<---- grep for number = i, put it in temporary item tempy
  if [ $(< tempy) != "0" ] #<---- if tempy is not zero, display the item
  then
    echo "Instances of $i: `cat tempy`" ; #<---- echo phrase, then in same line read tempy
  fi
done

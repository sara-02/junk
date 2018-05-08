#!/bin/bash

# A small script to download all the word_list PDF from http://www.majortests.com/gre/wordlist.php
# Command to run: source word_list_majorprep.sh
    
dir_name=word_list
mkdir -p $dir_name && cd $dir_name
for number in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
do
wget http://www.majortests.com/word-lists/word-list-$number.pdf
done
cd -
zip -r $dir_name.zip $dir_name
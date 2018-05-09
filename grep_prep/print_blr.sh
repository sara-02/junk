#!/bin/bash

# Connect to VPN
# Change the dir_name and printer_name
# Command to run: source print_blr.sh
# NOTE: From command line it alway prints Color. :/

dir_name=foo_dir
printer_name=foo_bar
cd $dir_name
for number in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
do
lpr -P $printer_name -l word-list-$number.pdf
done
cd -
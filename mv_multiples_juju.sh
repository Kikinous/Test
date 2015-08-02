#!/bin/bash 
str=$(ls|cut -f1 -d.);while read -r line;do echo "Substitution: " $line.doc --">" $line.txt ;mv $line.doc $line.txt; done<<<"$str";

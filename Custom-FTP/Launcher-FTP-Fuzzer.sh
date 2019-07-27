#!/bin/bash

i="0"
while [ $i -lt 5000 ]
do
	echo "[+] Fuzzing with..." $i
	python Fuzzer.py $i
	i=$[$i+500]
	read kk
done

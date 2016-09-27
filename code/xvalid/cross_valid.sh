#!/bin/bash

python txt2num.py # change the original form to test form + random_shuffle

cat /dev/null > myansX.txt # clean up testX.txt

for piece in 0 1 2 3 4
do
	python partition.py ${piece} 5 # do partition, 5-fold cross-validation

	# TODO: need to write a script solver.sh with 3 argument: train, test, ans
	# the format of myans${piece}.txt should be 2 number: start<tab>end
	./solver.sh train${piece}.txt test${piece}.txt myans${piece}.txt

	cat myans${piece}.txt >> myansX.txt # myansX.txt store all results
done

python score.py train.btt.txt myansX.txt

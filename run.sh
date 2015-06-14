#!/usr/bin/env bash

# make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/WordCounting.py
chmod a+x ./src/RunningMedian.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./src/WordCounting.py ./wc_input ./wc_output/wc_result.txt
python ./src/RunningMedian.py ./wc_input ./wc_output/med_result.txt
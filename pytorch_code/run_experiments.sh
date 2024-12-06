#!/bin/bash

echo "Launching Experiment 1"
python main.py --dataset diginetica --batchSize 128 --lr 0.001 --step 3 --validation 2>&1 | tee -a experiment1.log sleep 5

echo "Launching Experiment 2"
python main.py --dataset diginetica --batchSize 50 --lr 0.0005 --step 3 --validation 2>&1 | tee -a experiment2.log sleep 5

echo "Launching Experiment 3"
python main.py --dataset diginetica --batchSize 128 --lr 0.0001 --step 3 --validation 2>&1 | tee -a experiment3.log sleep 5

echo "Launching Experiment 4"
python main.py --dataset diginetica --batchSize 256 --lr 0.001 --step 3 --validation 2>&1 | tee -a experiment4.log sleep 5

echo "Launching Experiment 5"
python main.py --dataset diginetica --batchSize 64 --lr 0.001 --step 3 --validation 2>&1 | tee -a experiment5.log sleep 5
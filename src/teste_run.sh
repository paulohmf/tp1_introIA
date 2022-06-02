#!/bin/bash

##for i in "B" "I" "U" "A" "G" "H"; do python3 TP1.py $i 1 2 3 4 0 5 7 8 6 ; done;

### B 
# 0
python3 TP1.py B 1 2 3 4 5 6 7 8 0 >> log.txt 
# 1
python3 TP1.py B 1 2 3 4 5 6 7 0 8 >> log.txt
# 2 
python3 TP1.py B 1 2 3 4 0 5 7 8 6 >> log.txt

### I 
# 0
python3 TP1.py I 1 2 3 4 5 6 7 8 0 >> log.txt 
# 1
python3 TP1.py I 1 2 3 4 5 6 7 0 8 >> log.txt
# 2 
python3 TP1.py I 1 2 3 4 0 5 7 8 6 >> log.txt

### U 
# 0
python3 TP1.py U 1 2 3 4 5 6 7 8 0 >> log.txt 
# 1
python3 TP1.py U 1 2 3 4 5 6 7 0 8 >> log.txt
# 2 
python3 TP1.py U 1 2 3 4 0 5 7 8 6 >> log.txt

### A 
# 0
python3 TP1.py A 1 2 3 4 5 6 7 8 0 >> log.txt 
# 1
python3 TP1.py A 1 2 3 4 5 6 7 0 8 >> log.txt
# 2 
python3 TP1.py A 1 2 3 4 0 5 7 8 6 >> log.txt

### G 
# 0
python3 TP1.py G 1 2 3 4 5 6 7 8 0 >> log.txt 
# 1
python3 TP1.py G 1 2 3 4 5 6 7 0 8 >> log.txt
# 2 
python3 TP1.py G 1 2 3 4 0 5 7 8 6 >> log.txt

### H 
# 0
python3 TP1.py H 1 2 3 4 5 6 7 8 0 >> log.txt 
# 1
python3 TP1.py H 1 2 3 4 5 6 7 0 8 >> log.txt
# 2 
python3 TP1.py H 1 2 3 4 0 5 7 8 6 >> log.txt
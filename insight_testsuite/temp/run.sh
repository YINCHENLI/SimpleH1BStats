#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
echo "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE" > ./output/top_10_occupations.txt

cat ./input/h1b_input.csv | python ./src/mapper1.py | sort -t $'\t' -k1,1 |python ./src/reducer1.py | sort -t $';' -k2rn | awk 'NR <= 10' >> ./output/top_10_occupations.txt

echo "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE" > ./output/top_10_states.txt

cat ./input/h1b_input.csv | python ./src/mapper2.py | sort -t $'\t' -k1,1 | python ./src/reducer2.py | sort -t $';' -k2rn | awk 'NR <= 10' >> ./output/top_10_states.txt



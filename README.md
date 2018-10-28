# Simple H1B Statistics

There are 2 Map Reduce Jobs simulated in Python.

1. One job is to sum up and rank the top 10 certified occupations
 - mapper1.py - clean data, count 1 for each occupation (certified)
 - reducer1.py - sum up for each occupation
2. Second job is to sum up and rank the top 10 certified H1B work states
 - mapper2.py - clean data, count 1 for each work state (certifed)
 - reducer2.py - sum up for each state

### Language
Python 3

### Sorting
I am using pipe simulation, taking advantage of Linux/Unix sorting commands.
The following is the occupation pipe in `./run.sh` file

```
cat ./input/h1b_input.csv | python ./src/mapper1.py | sort -t $'\t' -k1,1 |python ./src/reducer1.py | sort -t $';' -k2rn | awk 'NR <= 10' >> ./output/top_10_occupations.txt
```

The following is the state pipe in `./run.sh` file

```
cat ./input/h1b_input.csv | python ./src/mapper2.py | sort -t $'\t' -k1,1 | python ./src/reducer2.py | sort -t $';' -k2rn | awk 'NR <= 10' >> ./output/top_10_states.txt
```

Feel free to contact me via email: careeryinchenli@gmail.com

 



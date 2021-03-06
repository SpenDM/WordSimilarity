# WordSimilarity
Find the most similar words by surface form (how words appear or how words sound) between given sets of words.

**Bases for similarity:**

* Current version -- English phonetics (very basic guessing from written form)
* Future versions -- IPA/orthography-based, improved guessed English phonetics-based

## Implementation
Uses a dynamic-time-warping-based approach.

Dynamic time warping compares two series of elements, finding how much one series has to be altered to match the other series (in this case, series of letters or sounds). DTW has been utilized for spell checking and speech recognition.

## Execution
*Command line call:*

```WordSim.py real_name [--k (integer)] [--name_file (filename)]```

*Examples:*

```WordSim.py ricardo```
    
Gives the best match to "ricardo" from the default file (pokemon names)
    
```WordSim.py Spencer --k 10```
    
Gives the 10 best matches to "spencer"
    
```WordSim.py "greg fletcher" --k 3 --name_file Data/GreekGodNames.txt```
    
Gives the 3 best matches for each name in "greg fletcher" from the given file (greek god names)

*Arguments:*

real_name is one word or several words within quotation marks

k is an integer which is the number of matches to output (optional, default=1)

name_list is the name of a file containing words to match (optional, default= pokemon name file)

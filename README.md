# WordSim
Find the most similar words by surface form (not meaning) between given sets of words.

**Bases for similarity:**

* English phonetics (simple guessing from written form)
* TODO -- IPA/orthography/Romaji (Japanese)

## Implementation
Uses a dynamic-time-warping-based approach.

## Running
*Command line call:*

PokeName.py real_name [--k (integer)] [--name_file (filename)]

*Examples:*

**WordSim.py ricardo**
    
    * Gives the best match to "ricardo" from the default file (pokemon names)
    
**WordSim.py Spencer --k 10**
    
    * Gives the 10 best matches to "spencer"
    
**WordSim.py "greg fletcher" --k 3 --name_file ../Data/GreekGodNames.txt**
    
    * Gives the 3 best matches for each name in "greg fletcher" from the given file (greek god names)

*Arguments:*

real_name is one word or several words within quotation marks

k is an integer which is the number of matches to output (optional, default=1)

name_list is the name of a file containing words to match (optional, default= pokemon names)

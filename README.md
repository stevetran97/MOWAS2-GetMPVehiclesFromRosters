Can be used to extract all unique vehicles (and properties) from a set of roster files.

## Use
  - Place all of the txt/set files that you want to search in the FilestoEdit Folder
  - The input takes a set of searched regular expression patterns (To be Replaced in set/txt files) 
    - searchPattern is used as a placeholder for the vehicle name
    - outputFilePath is the file to which the hash table of vehicles is written
    - costPattern is the pattern used to find the cost
    - commentTrigger is used to tell the code to ignore the line where this is the first character
  - run main.py to search all roster files and extract a hash table of unique vehicles


## Usecases
  - To consolidate all possible vehicle unit entries in one hashtable for balancing and later: redistribution to the roster files.

## Algorithm
  - Loops through each set (equivalent to txt) file in the Editting Folder
  - Looping through the file will return each line in a string format
  - The algorithm skips any lines which starts with the comment Trigger
  - The algorithm searches for the FIRST ITEM which matches the search pattern
  - If found, the costPattern is extracted from the same line
  - The algorithm checks to see if the searchPattern is already in the hashtable. If not, then it adds an entry.
  - When the double loop is finished, the algorithm loops through the hash table and writes a semi-formatted hash table to output.txt

## Current Intrinsic Issues/Assumptions
  - Assumes that all similar entries between roster files have the same cost. The hash table stores the first one it gets.
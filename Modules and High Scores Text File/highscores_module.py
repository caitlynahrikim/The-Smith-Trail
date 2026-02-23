# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 03:07:27 2024

@author: caitl
"""

"""
Creates a file for the highscores. Has all the input-output functions 
for the files. 
"""


def read_high_scores(filename):
    """ Relatively fancy reader of a high-scores text file
    
    It's fancy because it does not fail if the file does not exist already.
    It uses a try/except to "catch" the error and deal with it ourselves. 
    This is an advanced concept.
    """
    high_scores = {}
    high_scores_list = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Each line is a single string
            # Now split each line into a list with two values
            for line in lines:
                # Skip empty or improperly formatted lines
                if not line.strip():
                    continue
                score_item_pair = line.rstrip().split(",")
                if len(score_item_pair) != 2:  # Ensure it has exactly two parts
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                try:
                    # Make score an integer
                    score_item_pair[1] = int(score_item_pair[1])
                    high_scores_list.append(score_item_pair)
                except ValueError:
                    print(f"Skipping invalid score on line: {line.strip()}")
                    continue
    except IOError:
        print(f"The file {filename} does not exist!")
    
    high_scores = dict(high_scores_list)
    return high_scores


def write_high_scores(filename, high_scores):
    """ Relatively fancy reader of a high-scores to a text file
    
    It's fancy because it does not fail if the file does not exist already.
    It uses a try/except to "catch" the error and deal with it ourselves. 
    This is an advanced concept.
    """
    try:
        # Save updated scores
        # ---------------
        # NOTE this function assumes scores are already sorted
        
        # nos write high_scores_sorted to file
        with open(filename , 'w') as fwrite:  
            for key, value in high_scores.items():  
                fwrite.write(f"{key},{value}\n")
    except IOError:
        print(f"The file {filename} does not Exist!")

    return 

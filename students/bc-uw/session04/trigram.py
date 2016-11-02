"""
Trigram lab attempt.

Version0.I don't understand what this is supposed to do

"""
import sys
import string
import random

def sourceFile_to_list(input_file):
    """
    list comprehension to iterate through source file lines
    and add them to textlist
    """
    with open(input_file) as f:
        textlist = [line.strip().lower() for line in f]
        return textlist

def makeTrigram(sourcelist):
    """
    This function takes a list of words as input
    It then uses zip to merge words together and???
    """
    trigramzip = zip(sourcelist, sourcelist[1:], sourcelist[2:])
    #I can iterate through this zip 




if __name__ == "__main__":
    #from solutions, taking filename as an arg
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    #let's get the source file into a list
    sourceFile_to_list(filename)
    #let's split the list into words?

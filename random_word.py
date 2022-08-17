"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    '''Reads a text file, counts the words with the option to select a random word from the list
    
    >>> word_find = WordFinder("test.txt")
    3 words read

    >>> word_find.random() in ["cat", "dog", "porcupine"]
    True

    >>> word_find.random() in ["cat", "dog", "porcupine"]
    True
    '''

    def __init__(self, path):
        '''Reads dictionary and provides a word count'''

        dict_file = open(path)
        
        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        '''Converts dictionary into a list'''

        return [w.strip() for w in dict_file]

    def random(self):
        '''Chooses a random word from dictionary'''

        return random.choice(self.words)

class SpecialWordFind(WordFinder):
    '''Reads text file and finds a random word excluding commented out sections

    >>> swf = SpecialWordFind("testing.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["fruits", "veggies"]
    False

    >>> swf.random() in ["fruits", "veggies"]
    False
    '''

    def parse(self, dict_file):
        '''Converts dictionary into a list, skipping commented out code'''

        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
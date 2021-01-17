"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self):
        
        with open("words.txt") as self.file:
            self.word_list = []
            for line in self.file:
                self.word_list.append(line.strip())
    def random(self):
        from random import choice
        return choice(self.word_list)

word = WordFinder()
print(word.random())


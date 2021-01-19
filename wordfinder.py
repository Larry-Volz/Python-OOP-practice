"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self):
        self.word_list = []
        
    def read_word_file(self):
        with open("words.txt") as self.file:
            for line in self.file:
                self.word_list.append(line.strip())
            self.num_of_words = len(self.word_list)
            print(f"{self.num_of_words} words read")
            
    def random(self):
        """ finds a random word from a dictionary """
        from random import choice
        self.word = choice(self.word_list)
        return self.word 

word = WordFinder()
word.read_word_file()
print(word.random())

# class SpecialWordFinder(WordFinder):
#     def __init__(self):
#         self.some_variable = 0
#         super().__init__(self, word_list)
#         # print(super().word)


# newWord = SpecialWordFinder()
# newWord.read_word_file()
# print (newWord.random())


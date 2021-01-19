"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self):
        self.word_list = []
        
    def read_word_file(self):
        with open("python-oo-practice\words.txt") as self.file:
            for line in self.file:
                self.word_list.append(line.strip())
            self.num_of_words = len(self.word_list)
            print(f"{self.num_of_words} words read")
            
    def random(self):
        self.read_word_file()

        self.filtered_word_list = [word.strip() for word in self.word_list if word.strip() and not word.startswith("#")]
        """ finds a random word from a dictionary """
        from random import choice
        self.word = choice(self.word_list)
        return self.word


# word = WordFinder()
# word.read_word_file()
# print(word.random())

class SpecialWordFinder(WordFinder):
    def __init__(self):  #instantiates this sub-class
        super().__init__()  #starts up the super-class so I can use it's props/methods.  
        self.read_word_file
        # super().__init__(self, word_list, file)
        # print(super().word)
    
        # for word in self.word_list:
        #     print(word)


newWord = SpecialWordFinder()
# newWord.read_word_file()
print (newWord.random())


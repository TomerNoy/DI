class AnagramChecker():
    def __init__(self, file_name='week5/day5/mini-proj2/sowpods.txt') -> None:
        with open(file_name) as f:
            self.words = [word.strip() for word in f.readlines()]

    def is_valid_word(self, word):
        return word.upper() in self.words

    def get_anagrams(self, word):
        word_sorted = sorted(list(word))


test = AnagramChecker()

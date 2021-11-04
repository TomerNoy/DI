from stopwordsiso import stopwords
import string


class Text():
    val = ''

    @classmethod
    def from_file(self, text):
        text_from_file = ''
        with open(f'week5/day4/{text}', 'r') as f:
            text_from_file = f.read()
        return Text(text_from_file)

    def __init__(self, val):
        self.val = val

    def freq(self, word):
        words_list = self.val.split()
        count = words_list.count(word)
        if count < 1:
            return None
        else:
            return f'found {count} "{word}" in text'

    def most_common_word(self):
        word_list = self.val.split()
        unique_words_list = self.__get_unique_sorted(word_list)

        def how_many(w): return word_list.count(
            w) == word_list.count(unique_words_list[-1])
        most_common = list(filter(how_many, unique_words_list))
        return most_common

    def unique_list(self):
        word_list = self.val.split()
        unique_words_list = self.__get_unique_sorted(word_list)
        # most equally unique words
        def how_many(w): return word_list.count(
            w) == word_list.count(unique_words_list[0])
        most_unique = list(filter(how_many, unique_words_list))
        return most_unique

    def __get_unique_sorted(self, word_list):
        unique_words_list = list(set(word_list))
        unique_words_list.sort(key=lambda word: word_list.count(word))
        return unique_words_list


text1 = Text('val1 val3 val2 val val2')

print(text1.freq('val1'))
print(text1.most_common_word())
print(text1.unique_list())

# text2 = Text.from_file('the_stranger.txt')

# print(len(text2.unique_list()))

# ------------------------------------------------------------


class TextModification(Text):
    def __init__(self, val):
        super().__init__(val)

    # using the parent method will instantiate "Text" instead of "TextModification"
    @classmethod
    def from_file(self, text):
        text_from_file = ''
        with open(f'week5/day4/{text}', 'r') as f:
            text_from_file = f.read()
        return TextModification(text_from_file)

    def rm_punctuation(self):
        punctuationless = [
            char for char in self.val if char not in string.punctuation
        ]

        return ''.join(punctuationless)

    def rm_stop_words(self):
        word_list = self.val.split()

        for word in word_list:
            if word in stopwords("en"):
                word_list.remove(word)
        return ' '.join(word_list)

    def rm_special_char(self):
        print(self.val)
        special_charless = [
            char for char in self.val if char.isalnum() or char == ' '
        ]
        return ''.join(special_charless)


text3 = TextModification('asd asd asks *%*&& $ %J she HG perhaps32!!!')
text3.rm_punctuation()
text3.rm_stop_words()
text3.rm_special_char()

text4 = TextModification.from_file('the_stranger.txt')


# print(text4.rm_punctuation())
# print(text4.rm_stop_words())
# print(text4.rm_special_char())

import json
import random


def get_words_from_file():
    with open('week5/day4/sowpods.txt', 'r') as f:
        return (f.read()).split('\n')


def get_random_sentence(length):
    words_from_file = get_words_from_file()
    ran_words = []
    for i in range(length):
        ran_index = random.randint(0, len(words_from_file))
        ran_words.append(words_from_file[ran_index])

    return ' '.join(ran_words).lower()


def main():
    print('this program takes a number 2-20 and returns random words in a sentence with length of that number')
    length = input('how long would you like the sentence to be:\n')
    if not length.isnumeric:
        print('invalid input')
        exit()
    length = int(length)
    if length < 2 or length > 20:
        print('invalid number')
        exit()
    print(get_random_sentence(length))


# main()

# ------------------------------------

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
from_json = json.loads(sampleJson)
salary = from_json['company']['employee']['payable']['salary']
from_json['company']['employee']['payable']['birth_date'] = '2048/12/30'
sampleJson = json.dumps(from_json, indent=3)

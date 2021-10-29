words = ['without', 'hello', 'bag', 'world']


def option1():
    print(sorted(words))


def option2():
    list = []
    while len(words):
        list.append(words.pop(words.index(min(words))))
    print(list)


def option3():
    list = []
    for i in range(len(words)):
        list.append(words.pop(words.index(min(words))))
    print(list)


def option4():
    '''List Comprehension'''
    list = [words.pop(words.index(min(words))) for i in range(len(words))]
    print(list)


option4()

grid = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]


cols = []

for row in grid:
    for i, char in enumerate(row):
        if len(cols) == i:
            cols.append([])
        cols[i].append(char)


result = ''
lastIsSpace = False

for i in cols:
    for char in i:
        if char.isalpha():
            result += char
            lastIsSpace = False
        elif not char.isdigit() and not lastIsSpace:
            lastIsSpace = True
            result += ' '

print(result)
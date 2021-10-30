# 1
# C = 50
# H = 30

# nums = input('please enter numbers seperated by comma:\n')
# nums = nums.split(',')

# results = []

# for D in nums:
#     if not D.isnumeric:
#         print('invalid number')
#         exit()
#     Q = ((2*C*int(D))/H)**(1/2)
#     results.append(int(Q))

# print(results)


# 2

# listN = []

# while len(listN) < 11:
#     num = input('enter a number between -100 to 100:\n')
#     print(num.isnumeric())
#     if num.isnumeric():
#         num = int(num)
#         if -100 < num < 100:
#             listN.append(num)


# print(listN)
# sortedList = sorted(listN)
# sortedList.reverse()
# print(sortedList)
# print(sum(sortedList))
# print(listN[0], listN[len(listN) - 1])

# greater50 = []
# for n in listN:
#     if n > 50:
#         greater50.append(n)
# print(greater50)

# smaller10 = []
# for n in listN:
#     if n < 10:
#         smaller10.append(n)
# print(smaller10)
# sqrd = []
# for n in listN:
#     sqrd.append(n**2)
# print(sqrd)

# originals = list(set(listN))
# print(originals, f'total of {len(originals)}')
# print(int(sum(listN) / len(listN)))
# print(max(listN), min(listN))

# bonus
# sum = 0
# totalVals = 0
# avarage = 0
# largest = 0
# smallest = 0
# for i in listN:
#     totalVals += 1
#     sum += i
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# avarage = int(sum / totalVals)
# print(sum, avarage, largest, smallest)

# 3
# p = 'Programs were mostly still entered using punched cards or paper tape. By the late 1960s, data storage devices and computer terminals became inexpensive enough that programs could be created by typing directly into the computers. Text editors were also developed that allowed changes and corrections to be made much more easily than with punched cards.'
# sentences = p.split('.')
# words = p.split(' ')
# uniques = []

# for w in words:
#     if p.count(w) == 1:
#         uniques.append(w)

# print(
#     f'this paragraph has {len(p)} characters, {len(sentences)} sentences, {len(words)} words of which {len(uniques)} are unique')
# p2 = p + ' '

# while ' ' in p2:
#     p2 = p2.replace(' ', '')

# print('whitespaces', len(p2))

# avarage = len(words) / len(sentences)
# print('avarage', int(avarage))

# print('non-unique', len(words) - len(uniques))

# 4
# p = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
# words = set(p.split(' '))
# for w in words:
#     print(w + ':', p.count(w))

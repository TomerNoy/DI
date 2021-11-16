# import datetime


# def get_age(year, month, day):
#     today = datetime.date.today()
#     x = datetime.date(year, month, day)
#     diff = (today - x).days / 365.25
#     return diff


# get_age(1979, 8, 9)


# def can_retire(gender, date_of_birth):
#     year = int(date_of_birth[0])
#     month = int(date_of_birth[1])
#     day = int(date_of_birth[2])
#     age = get_age(year, month, day)
#     if gender == 'f':
#         if age >= 62:
#             print('can retire')
#         else:
#             print('too young')

#     elif gender == 'm':
#         if age >= 67:
#             print('can retire')
#         else:
#             print('too young')


# age = input('please enter your birth date using the format “yyyy/mm/dd”:\n')

# while True:
#     date_list = age.split('/')
#     if len(date_list) != 3 or not date_list[0].isnumeric or not date_list[1].isnumeric or not date_list[2].isnumeric:
#         age = input(
#             'invalid input, please enter your birth date using the format “yyyy/mm/dd”:\n')
#     else:
#         break

# gender = input('please enter your gender m/f:\n')

# while True:
#     if gender not in 'mf':
#         gender = input('invalid input, please enter your gender m/f:\n')
#     else:
#         break

# can_retire(gender, age.split('/'))


# ----------------------------------------------------------------------------
# def calc(X):
#     X = str(X)
#     print(int(X)+int(X+X)+int(X+X+X)+int(X+X+X+X))


# calc(3)

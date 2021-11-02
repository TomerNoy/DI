# import datetime

# def display_current_date():
#     print(datetime.datetime.now())

# display_current_date()

# ------------------------------------------------------------------------
# def time_left_until_jan():
#     now = datetime.datetime.now()
#     next_jan = datetime.datetime(now.year + 1, 1, 1)
#     diff = next_jan - datetime.timedelta(
#         hours=now.hour, minutes=now.minute, seconds=now.second
#     )
#     print(
#         f'the 1st of January is in {diff.day} days and {diff.hour}:{diff.minute}:{diff.second} hours')


# time_left_until_jan()

# ------------------------------------------------------------------------
# def alive(*arg):
#     now = datetime.datetime.now()
#     bd = datetime.datetime(*arg)
#     diff = now - bd
#     print(f'you are alive {int(diff.seconds/60)} minutes')


# alive(2000, 1, 1)

# ------------------------------------------------------------------------
# def today():
#     now = datetime.datetime.today()
#     print(now.date())

#     hanukkah = datetime.datetime(2021, 11, 29)

#     diff = hanukkah - datetime.timedelta(
#         hours=now.hour, minutes=now.minute, seconds=now.second
#     )

#     print(
#         f'the next holiday is Hanukkah in 30 days and {diff.hour}:{diff.minute}:{diff.second} hours'
#     )


# today()

# ------------------------------------------------------------------------
# not sure if this is the meaning but...
# def how_old(seconds):
#     print(f'On Earth you\'re {round(seconds/31557600, 2)} Earth-years old')
#     print(
#         f'On Mercury you\'re {round(seconds/(0.2408467 * 31536000), 2)} Earth-years old')
#     print(
#         f'On Venus you\'re {round(seconds/(0.61519726 * 31536000), 2)} Earth-years old')
#     print(
#         f'On Mars you\'re {round(seconds/(1.8808158 * 31536000), 2)} Earth-years old')
#     print(
#         f'On Jupiter you\'re {round(seconds/(11.862615 * 31536000), 2)} Earth-years old')
#     print(
#         f'On Saturn you\'re {round(seconds/(29.447498 * 31536000), 2)} Earth-years old')
#     print(
#         f'On Uranus you\'re {round(seconds/(84.016846 * 31536000), 2)} Earth-years old')
#     print(
#         f'On Neptune you\'re {round(seconds/(164.79132 * 31536000), 2)} Earth-years old')


# how_old(1000000000)

# ------------------------------------------------------------------------
# from faker import Faker
# fake = Faker()

# users = []


# def add_user():
#     fake_usr = {
#         'name': fake.name(),
#         'address': fake.address(),
#         'langage_code': fake.language_code()
#     }
#     users.append(fake_usr)


# print(users)

# for i in range(10):
#     add_user()

# print(users)

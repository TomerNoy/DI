
# class My_class:  # not sure if this is the meaning?!
#     '''
#     this is an exercise in dunder methods
#     '''

#     def __init__(self, v, method):
#         if method == 'abs_method':
#             print(abs(v))

#         if method == 'int_method':
#             print(int(v))

#         if method == 'input_method':
#             input()


# print(My_class.__doc__)


class Currency():
    def __init__(self, currency, val):
        self.currency = currency
        self.val = val

    def __str__(self):
        # print('str used')
        return f'{self.val} {self.currency}'

    def __int__(self):
        # print('int used')
        return self.val

    def __add__(self, other):
        # print('add used', 'other type is:', type(other))
        if type(other) == int:
            return self.val + other
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError(
                    f'Cannot add between Currency type {self.currency} and {other.currency}')
            return self.val + other.val

    def __iadd__(self, other):

        # print('iadd used', 'other type is:', type(other))
        if type(other) == int:
            # print('other type', type(other))
            self.val += other
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError(
                    f'Cannot add between Currency type {self.currency} and {other.currency}')
            self.val += other.val
        return self

    def __repr__(self):
        # print('repr used')
        return (self.__str__())


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))

print(c1 + 5)
print(c1 + c2)

print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c1 + c3

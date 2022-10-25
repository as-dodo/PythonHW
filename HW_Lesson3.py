# 3.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0], my_list[2][1], my_list[2][2])

# 3.2
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0
# for i in list_1:
#     if isinstance(i, int):
#         sum += i
# print(sum)

# for i in list_1:
#     if isinstance(i, str) and i.find('a') != -1:
#         print(i)

# 3.3
# my_tuple = tuple(['cat', 'dog', 'horse', 'cow'])
# print(type(my_tuple))

# 3.4
# family_1 = input('Enter family members')
# family_2 = input('Enter family members')
# if len(family_1) == len(family_2):
#     print('Equal')
# elif len(family_1) > len(family_2):
#     print(family_1)
# else:
#     print(family_2)

# 3.5
# film = {
#     'name': 'Django',
#     'director': 'Tarantino',
#     'year': 2008,
#     'budget': 6000000000,
#     'main_actor': 'Leo Dicaprio',
#     'slogan': 'Django unchained'
# }
# print(film.keys())
# print(film.values())
# print(film.items())

# 3.6
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# 3.7
# print(set([1, 2, 3, 4, 5, 3, 2, 1]))

# 3.8
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))

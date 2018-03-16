# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print('-' * 40)
#
# wild_animals = set(['lion', 'panther', 'tiger', 'elephant', 'hare'])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add('horse')
# wild_animals.add('horse')
# print(farm_animals)
# print(wild_animals)


# even = set(range(0, 40, 2))
# print(even)
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))
#
# print('-' * 20)
#
# print(even.intersection(squares))
# print(even & squares)

# even = set(range(0, 40, 2))
# print(sorted(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print('e - s')
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print('s - e')
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print('-' * 20)
#
# print(sorted(even))
# print(squares)
#
# even.difference_update(squares)
#
# print(sorted(even))


# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# # print('symmetric diff')
# # print(sorted(even.symmetric_difference(squares)))
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  #does nothing
# print(squares)
#
# try:
#     squares.remove(8)
# except KeyError:
#     print("Awesome m8, the 8 is not gr8")
#
#
# fucklist = [x for x in squares]
# print(fucklist)


# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)

# if squares.issubset(even):
#     print("squares is a subsset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")


# even = frozenset(range(0, 100, 2))
# print(even)

# program that takes some text and returns
# a list of all the characters in the text that are not vowels, sorted in alphabetical order

sent = set(input('Text to do stuff on: '))

chars = sorted(list(sent.difference('aeiou')))

print(chars)

















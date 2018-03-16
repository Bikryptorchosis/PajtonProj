#
# try:
#     with open("C:/Users/Frinn/Downloads/sample.txt", 'r') as f:
#         for line in f:
#             if "jab" in line.lower():
#                 print(line, end='')
# except FileNotFoundError:
#     print("No such file or path exists")

# with open("C:/Users/Frinn/Downloads/sample.txt", 'r') as f:
#     line = f.readline()
#     while line:
#         print(line, end='')
#         line = f.readline()

# with open("C:/Users/Frinn/Downloads/sample.txt", 'r') as f:
#     lines = f.readlines()
# print(lines, end='')
#
# for line in lines:
#     print(line, end='')

# with open("C:/Users/Frinn/Downloads/sample.txt", 'r') as f:
#     lines = f.readlines()
# print(lines, end='')
#
# for line in lines[::-1]:
#     print(line, end='')

# cities = ['breslau', 'krakau', 'warszau', 'oppeln']
#
# with open("sample.txt", 'w') as f:
#     for city in cities:
#         print(city, file=f)

# cities = []
#
# with open("sample.txt", "r") as f:
#     for city in f:
#         cities.append(city.strip("\n"))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open('imelda3.txt', 'w') as f:
#     print(imelda, file=f)

# with open('imelda3.txt', 'r') as f:
#     contents = f.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)

# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24

# with open('C:/Users/Frinn/Downloads/sample2.txt', 'a') as f:
#     for i in range(2, 13):
#         for j in range(2, 13):
#             print(f'{j:>2} times {i} is {i*j}', file=f)
#         print('='*20, file=f)

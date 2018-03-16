# coding=utf-8
# import random
#
# lista = []
#
# for i in range(input('davai ile\n')):
#     lista.append(random.choice(range(1, 100)))
#
#
# print(lista)
# #print(len(lista))
#
#
# def sortowanie(list1):
#     for i in range(len(list1)):
#         for j in range(1, len(list1) - i):
#             if list1[j - 1] > list1[j]:
#                 list1[j - 1], list1[j] = list1[j], list1[j - 1]
#     return list1
#
#
# print(sortowanie(lista))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1


# import re
#
# inp = [x for x in raw_input("input passwords pls:\n").split(',')]
# values = []
#
# for passw in inp:
#
#     if 5 < len(passw) < 13:
#         pass
#     else:
#         # print('1')
#         continue
#
#     if not re.search("[a-z]", passw):
#         # print('2')
#         continue
#     if not re.search("[A-Z]", passw):
#         # print('3')
#         continue
#     if not re.search("[0-9]", passw):
#         # print('4')
#         continue
#     if not re.search("[\$#@]", passw):
#         # print('5')
#         continue
#
#     values.append(passw)
#
# print(','.join(values))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.


# from operator import itemgetter
#
# tupes = []
#
# while True:
#     s = raw_input("input: \n")
#
#     if not s:
#         break
#     tupes.append(tuple(s.split(",")))
#
# print sorted(tupes, key=itemgetter(0, 1, 2))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use yield


# def putNumbers(n):
#     i = 0
#     while i < n:
#         j = i
#         i = i+1
#         if j % 7 == 0:
#             yield j
#
#
# for i in putNumbers(100):
#     print i

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# import math
#
# pos = [0, 0]
#
# while True:
#     s = raw_input("Podej: ")
#
#     if not s:
#         break
#
#     movement = s.split(' ')
#     direction = movement[0]
#
#     try:
#         steps = int(movement[1])
#     except ValueError:
#         print "That's not a number you little shit"
#         continue
#
#     if direction == 'UP':
#         pos[1] += steps
#     elif direction == 'DOWN':
#         pos[1] -= steps
#     elif direction == 'LEFT':
#         pos[0] -= steps
#     elif direction == 'RIGHT':
#         pos[0] += steps
#     else:
#         print "No such direction, fakju"
#
# print int(round(math.sqrt(pow(pos[0], 2) + pow(pos[1], 2))))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# freq = {}
# sentence = raw_input('Diupa: ')
#
# for word in sentence.split():
#     freq[word] = freq.get(word, 0) + 1
#
# words = freq.keys()
# words.sort()
#
# for i in words:
#     print("{}:{}".format(i, freq[i]))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#     Write a method which can calculate square value of number


# def square(a):
#     return a ** 2

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Python has many built - in functions, and if you do not know how to use it, you can read document online or find some books.But Python has a built- in document function for every built- in functions.
# Please write a program to print some Python built - in functions documents, such as abs(), int(), raw_input()
# And add document for your own function
#
# Hints:
# The built - in document
# method is __doc__


# print abs.__doc__
# print int.__doc__
# print raw_input.__doc__
#
# def square(num):
#     ''' what is this
#     fucking thing
#     yeah'''
#     return num ** 2
#
#
# print square.__doc__

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later


# class Dupa:
#     name = "tylek"
#
#     def __init__(self, name=None):
#         self.name = name
#
#
# chuj = Dupa("Imie")
# print "{} imie to {}".format(Dupa.name, chuj.name)
#
# cipa = Dupa()
# cipa.name = "blada"
# print "{} imie to {}".format(Dupa.name, cipa.name)

# ---------------------------------------------------------------------------------------------------------------------

# Define a function which can compute the sum of two numbers.


# def suma(num1, num2):
#     return num1 + num2

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Define a function that can convert a integer into a string and print it in console.

# def itos(num):
#     print(str(num))

# ---------------------------------------------------------------------------------------------------------------------

# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = filter(lambda x: x%2==0, li)
# print evenNumbers
#
# print filter.__doc__


# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, li)
# print squaredNumbers
# print li
#
# print map.__doc__

# def multiply(x):
#     return (x*x)
# def add(x):
#     return (x+x)
#
# funcs = [multiply, add]
# for i in range(5):
#     value = list(map(lambda x: x(i), funcs))
#     print(value)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Define a class named American which has a static method called printNationality.
#
# Hints:
#
# Use @staticmethod decorator to define class static method.

# class Murican:
#     @staticmethod
#     def printNationality():
#         print "MURICA, FAK YEA"
#
# anAmerican = Murican()
# anAmerican.printNationality()
# Murican.printNationality()

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Define a class named American and its subclass NewYorker.
#
# Hints:
#
# Use class Subclass(ParentClass) to define a subclass.

# class Murican():
#     def __init__(self):
#         print "MURICA"
#
#     @staticmethod
#     def printNationality():
#         print "Amuricunt"
#
#
# class Alien(Murican):
#     def __init__(self):
#         print("Alien, ivul alien")
#
#     @staticmethod
#     def printNationality():
#         print 'Mars'
#
#
# Alien.printNationality()

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
#
# Hints:
#
# Use def methodName(self) to define a method.

# import math
#
#
# class Circle:
#     def __init__(self, r):
#         self.radius = r
#
#     def compArea(self):
#         return pow(self.radius, 2) * math.pi
#
#
# one = Circle(2)
# print one.compArea()

# ---------------------------------------------------------------------------------------------------------------------

# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
#
# Hints:
#
# Use def methodName(self) to define a method.


# class Rect:
#     def __init__(self, l, w):
#         self.width = w
#         self.long = l
#
#     def compArea(self):
#         return self.long * self.width
#
#
# newrect = Rect(2, 3)
# print newrect.compArea()

# ---------------------------------------------------------------------------------------------------------------------

# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
#
# Hints:
#
# To override a method in super class, we can define a method with the same name in the super class.

# class Shape:
#     def __init__(self):
#         self.length = 0
#
#     def area(self):
#         return pow(self.length, 2)
#
#
# class Square(Shape):
#     def __init__(self, leng):
#         self.length = leng
#
#
# shejp = Square(2)
# skler = Shape()
#
# print shejp.area()
# print skler.area()

# ---------------------------------------------------------------------------------------------------------------------

# def throws():
#     return 5/0
#
# try:
#     throws()
# except ZeroDivisionError:
#     print "division by zero!"
# except Exception, err:
#     print 'Caught an exception'
# finally:
#     print 'In finally block for cleanup'

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
# the user name of a given email address. Both user names and company names are composed of letters only.
#
# Example:
# If the following email address is given as input to the program:
#
# john@google.com
#
# Then, the output of the program should be:
#
# john
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# Use \w to match letters.

# import re
#
# emailAddress = raw_input('djupa')
# pat2 = "(\w+)@((\w+\.)+(com))"
# r2 = re.match(pat2, emailAddress)
# print r2.group(1)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
#
# Example:
# If the following words is given as input to the program:
#
# 2 cats and 3 dogs.
#
# Then, the output of the program should be:
#
# ['2', '3']
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# Use re.findall() to find all substring using regex.

# import re
#
# sent = raw_input("input sentence: ")
# numbers = list(re.findall('\d+', sent))
# print numbers

# ---------------------------------------------------------------------------------------------------------------------

# unistring = u"Heloł duć"
# print unistring

# ---------------------------------------------------------------------------------------------------------------------

# sent = unicode(raw_input("Podej stringi: "), "utf-8")
#
# print sent

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#
# Example:
# If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 3.55
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# Use float() to convert an integer to a float


# n = int(raw_input("Podej inputa: "))
# suma = 0.0
#
# if n > 0:
#     for i in xrange(1, n+1):
#         suma += float(i) / (i + 1)
#         print suma
# else:
#     print("FOKEN BICZ")
#
# print(suma)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
#
# with a given n input by console (n>0).
#
# Example:
# If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 500
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# We can define recursive function in Python.

# def compute(n):
#     if n:
#         return compute(n - 1) + 100
#     else:
#         return 1
#
#
# fuq = int(raw_input("Inpute namba: "))
# print compute(fuq)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
#
# The Fibonacci Sequence is computed based on the following formula:
#
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program to compute the value of f(n) with a given n input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 7
#
# Then, the output of the program should be:
#
# 13
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# We can define recursive function in Python.

# def fibonacci(n):
#
#     if n < 0:
#         print("Fakju")
#     else:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# x = int(raw_input("Podej inpat: "))
#
# print(fibonacci(x))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# The Fibonacci Sequence is computed based on the following formula:
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 7
#
# Then, the output of the program should be:
#
# 0,1,1,2,3,5,8,13
#
# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.
#
# In case of input data being supplied to the question, it should be assumed to be a console input.


# def fibonacci(n):
#
#     if n < 0:
#         print("Fakju")
#     else:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# x = int(raw_input("Podej inpat: "))
#
# seq = [str(fibonacci(i)) for i in xrange(0, x + 1)]
#
# print ','.join(seq)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 10
#
# Then, the output of the program should be:
#
# 0,2,4,6,8,10
#
# Hints:
# Use yield to produce the next value in generator.
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

# def evenNumbers(n):
#
#     i = 0
#     while i <= n:
#         if not i % 2:
#             yield i
#         i += 1
#
#
# n = int(raw_input("Podej inpat: "))
#
# seq = []
# for i in evenNumbers(n):
#     seq.append(str(i))
#
# print ','.join(seq)

# ---------------------------------------------------------------------------------------------------------------------


# Question:
#
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 100
#
# Then, the output of the program should be:
#
# 0,35,70
#
# Hints:
# Use yield to produce the next value in generator.
#
# In case of input data being supplied to the question, it should be assumed to be a console input.


# def evenNumbers(n):
#
#     i = 0
#     while i <= n:
#         if i % 5 == 0 and i % 7 == 0:
#             yield i
#         i += 1
#
#
# n = int(raw_input("Podej inpat: "))
#
# seq = []
# for i in evenNumbers(n):
#     seq.append(str(i))
#
# print ','.join(seq)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.
#
# Hints:
# Use "assert expression" to make assertion.


# li = [2, 4, 6, 8, 9]
# for i in li:
#     try:
#         assert i % 2 == 0       # throws AssertionError if false
#     except AssertionError:
#         print("There are ODD NUMBERS THERE. THAT'S ODD LEL")
#         pass
#
# print li

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Please write a program which accepts basic mathematic expression from console and print the evaluation result.
#
# Example:
# If the following string is given as input to the program:
#
# 35+3
#
# Then, the output of the program should be:
#
# 38
#
# Hints:
# Use eval() to evaluate an expression.


# expression = raw_input("Podej input: ")
# print eval(expression)
# LOL

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
#
# Hints:
# Use if/elif to deal with conditions.


# import math
#
# def bin_search(li, element):
#     bottom = 0
#     top = len(li) - 1
#     index = -1
#     while top >= bottom and index == -1:
#         mid = int(math.floor((top + bottom) / 2.0))
#         if li[mid] == element:
#             index = mid
#         elif li[mid] > element:
#             top = mid - 1
#         else:
#             bottom = mid + 1
#
#     return index
#
#
# li = [2, 5, 7, 9, 11, 17, 222]
#
# print bin_search(li, 11)
# print bin_search(li, 12)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
#
# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.

# import zlib
#
# words = "hello world!hello world!hello world!hello world!"
# compressed = zlib.compress(words)
# print compressed
# print zlib.decompress(compressed)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Please write a program to print the running time of execution of "1+1" for 100 times.
#
# Hints:
# Use timeit() function to measure the running time.

# import timeit
# t = timeit.Timer("for i in range(100):1+1")
#
# print t.timeit()
# print timeit.timeit("for i in range(100):1+1")
#
# if __name__ == '__main__':
#     print(timeit.timeit("fibonacci(30)", setup="from __main__ import fibonacci", number=12))

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
#
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.


# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i % 2]
# li = [x for (i,x) in enumerate(li) if i not in (0,2,4,6)] # lel
# print li

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
#
# Hints:
# Use list comprehension to make an array.

# array = [[[0 for x in range(8)] for y in range(5)] for z in range(3)]
#
# print array

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
#
# Hints:
# Use set() and "&=" to do set intersection operation.

# set1 = set([1, 3, 6, 78, 35, 55])
# set2 = set([12, 24, 35, 24, 88, 120, 155])
# set1 &= set2
# li = list(set1)
# print li

# ---------------------------------------------------------------------------------------------------------------------

# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
#
# Hints:
# Use set() to store a number of values without duplicate.

# def removeDupes(li):
#     newli = []
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add(item)
#             newli.append(item)
#     return newli
#
#
# li = [12,24,35,24,88,120,155,88,120,155]
# print removeDupes(li)

# ---------------------------------------------------------------------------------------------------------------------

# Question:
#
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
#
# Hints:
# Use Subclass(Parentclass) to define a child class.


# class Person:
#     def __init__(self):
#         self.gender = "Agender"
#
#     def getGender(self):
#         return self.gender
#
#
# class Male(Person):
#     def __init__(self):
#         self.gender = "Male"
#
#
# class Female(Person):
#     def __init__(self):
#         self.gender = "Female"
#
#
# aMale = Male()
# aFemale = Female()
# print aMale.getGender()
# print aFemale.getGender()

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example:
# If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
#
# Hints:
# Use dict to store key/value pairs.
# Use dict.get() method to lookup a key with default value.

# dic = {}
# s = raw_input("Podej kierwe: ")
#
# for s in s:
#     dic[s] = dic.get(s, 0) + 1
#
# print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])

# ---------------------------------------------------------------------------------------------------------------------

# Question:
# Please write a program which prints all permutations of [1,2,3]
#
# Hints:
# Use itertools.permutations() to get permutations of list.

# import itertools
# print list(itertools.permutations([1, 2, 3]))

# ---------------------------------------------------------------------------------------------------------------------
#
# Question:
#
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
#
# Hint:
# Use for loop to iterate all possible solutions.


# def solve(numheads, numlegs):
#     ns = "No solvent, no precipitate"
#
#     for i in range(numheads + 1):
#         j = numheads - i
#         if 2*i+4*j == numlegs:
#             return i, j
#
#     return ns, ns
#
#
# numheads = 35
# numlegs = 94
# solutions = solve(numheads, numlegs)
# print solutions

# ---------------------------------------------------------------------------------------------------------------------

# def collatz(num):
#     if num == 1:
#         pass
#     elif not num % 2:
#         print(num // 2)
#         collatz(num // 2)
#     else:
#         print(num * 3 + 1)
#         collatz(num * 3 + 1)
#
#
# try:
#     collatz(int(input("podej inta: ")))
# except ValueError:
#     print("Tychuju")

# ---------------------------------------------------------------------------------------------------------------------

# def fuck(lis):
#     s = ''
#     for word in lis:
#         if spam.index(word) == len(lis) - 1:
#             s += f', and {word}'
#         elif spam.index(word) == 0:
#             s += word
#         else:
#             s += f', {word}'
#
#     return s
#
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
# print(fuck(spam))

# ---------------------------------------------------------------------------------------------------------------------

# def excercise(p, n):
#     a = str(p) + '0'*n + str(p)
#     res = eval(a + '**2')
#     print(res)
#
# excercise(5,1)


# def firstDuplicate(a):
#     """
#
#     :type a: list
#     """
#     mins = -1
#     for i in a:
#         if i in a:
#             if a.index(i) < mins:
#                 mins = a.index(i)
#     return a[min]

# sequence = [1, 2, 5, 3, 5]


# def almostIncreasingSequence(statues):
#     last, mistakes = statues[0], 0
#     for i in range(0, len(statues) - 1):
#         print(f'comparing {last} < {statues[i +1]}')
#         if last < statues[i + 1]:
#             last = statues[i + 1]
#             print(f'last {last}')
#         else:
#             mistakes += 1
#             last = statues[i + 1]
#             print(f'mistake done with {last}')
#     return False if mistakes > 1 else True


# def check_increasing(seq):
#     for i in range(len(seq)-1):
#         if seq[i] >= seq[i+1]:
#             return i
#     return -1
#
#
# def almostIncreasingSequence(sequence):
#     ind = check_increasing(sequence)
#     if check_increasing(sequence) == -1:
#         return True
#     if check_increasing(sequence[ind-1:ind] + sequence[ind+1:]) == -1 \
#             or check_increasing(sequence[ind:ind+1] + sequence[ind+2:]) == -1:
#         return True
#     return False
#
#
# print(almostIncreasingSequence(sequence))


# def matrixElementsSum(matrix):
#     notSuitable = []
#     sumOfCost = 0
#     for i in matrix:
#         for j in range(len(i)):
#             if not (i[j] == 0) and (j not in notSuitable):
#                 sumOfCost += i[j]
#                 print(i[j])
#             else:
#                 notSuitable.append(j)
#     return sumOfCost
#
#
# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]
#
# print(matrixElementsSum(matrix))

# import re

s = ["aba", "aa", "ad", "vcd", "aba"]
# leng = max(len(x) for x in s)
leng = len(max(s, key=len))
# a = ' '.join(s)
# match = re.findall(r'\b\w{%s}\b' % leng, a)
#
# print(match)

match = [x for x in s if len(x) == leng]
print(match)

match = list(filter(lambda x: len(x) == max([len(i) for i in s]), s))
print(match)
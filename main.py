'''
Text type (String)
'''
# st = 'This is a single line string'
# print(st)
# print(type(st))

#==============><==============

# st = '''This is a multiline string example'''
# print(st)
# print(type(st))

#==============><==============

# Find a character by index 
# st = 'String sample'
# print(st[4])

# slicing

# st = 'string sample'
# print(st[1:6])

#==============><==============

#immutable

# st = 'string sample'
# st[2] = 'o'
# print(st)

'''
Numeric type (Integer,  Float, Complex)
'''
# integer
# x = 12134354657687
# print(type(x))

# float
# accurate up to 15-16 decimal places will be printed

# x = 0.1324e65653232345654534356565643
# print(type(x))
# print(x)

# complex
# x = 1 + 2j
# print(type(x))

'''
Sequence Type (List, Tuple, Range)
'''

# homogenous 
# x = []
# #List, an empty one 
# x = [10, 2.5, 'Hello']
# print(x[2])
# print(x[1:3])

# mutable

# x[2] = 'Python'
# print(x)

#Tuple
#heterogeneous

# Tuple =()

#==============><==============

# Both of example below are types of tuples, without comma makes it a string

# tuple = ('Hello')
# tuple = 'Hello',
# print(type(tuple))

#==============><==============

# tuple = ('cat', [4,3,5,], (5,4,1,))
# print(tuple[2])

# # immutable 

# tuple = ('cat', [4,3,5], (5,4,1))
# tuple[2] = 10
# print(tuple)
# #TypeError: 'tuple' object does not support item assignment

#==============><==============

# Range 

# x = range(20)
# for n in x:
#   print(n)

'''
Mapping Type (Dictionary)
'''

# dict = {}   # empty dictionary looklike
# print(type(dict))

#==============><==============
# dict is mutable

# dict = {'name': 'Sarkash', 'age': 25}
# print(dict['age'])
# print(dict.get('name'))

# dict['age'] = 35
# print(dict)

'''
Set Types
'''

# Empty set having set = {} is an empty dict

# # set = {} # type of this is a dict
# set = set() # for makeing an empty set use set()
# print(type(set))

#==============><==============


# mixed data types ( all immutable )

# set = {3.2, 'Hi', (1,2,3,4)}
# print(type(set))
# # TypeError: 'set' object is not subscriptable
# print(set[0])

# No duplicates 

# set = {3.2, 'Hi', (1,2,3,4), 'Hi'}
# print(set)

# # Cannot have mutable (list) in a set
# set = {3.2, 'Hi', (1,2,3), [1,2,3]}
# # TypeError: unhashable type: 'list'
# print(set)

'''
boolean Type (True or False)
'''

# print(type(True))

# # boolean as numbers
# print(True == 1)
# print(False == 0)

# # interesting logic
# print(True + True)

# # not boolean operator
# print(not True)
# print(not False)

# # and boolean operator
# print(True and False)
# print(True and True)
# print(False and False)

# #or boolean operator
# print(True or False)
# print(True or True)
# print(False or False)
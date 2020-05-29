# 1. Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple.
tuple_1 = ('Italy', 'Russia', 'Hungary', 'USA', 'Mexico')
country_1 = input("Tell me any country from the list? ")
print(tuple_1.index(country_1))
# RETURN FUNCTION:


def country_index(tuple, string):
    return tuple.index(string)


print(country_index(tuple_1,country_1))

# 2. Add to the previous program to ask the user to enter a number and display the country in that position.
tuple_2 = ('Italy', 'Russia', 'Hungary', 'USA', 'Mexico')
number_2 = int(input(" Tell me any number between 0 and 4? "))
print(tuple_2[number_2])
# RETURN FUNCTION:


def country_by_index(tuple, number):
    return tuple[number]


print(country_by_index(tuple_2, number_2))

# 3. Write a Python script to add a key to a dictionary.
dict_3 = dict(zero = 10, one = 20 )
dict_3.update({'two':30})
#OR
dict_3.update(two = 30)
print(dict_3)
# RETURN FUNCTION:


def dictionary_key(dict, str_key, value):
    dict.update({str_key : value})
    return dict


print(dictionary_key(dict_3,'two',30))

# 4. Write a Python program to iterate over dictionaries using for loops.
dict_4 = dict(Hungary = 'hungarian', Russia = 'russian', Italy = 'italian')
# To get a pair:
for item in dict_4.items():
    print(item)
# #OR to get key and value:
for key,value in dict_4.items() :
    print(key)
    print(value)
# RETURN FUNCTION. No idea if it is correct. I don't understand what should be the output here :):


def iterate_dict():
    arr_4 = []
    for item in dict_4.items():
        arr_4 += item
    return arr_4


print(iterate_dict())

# 5. Write a Python script to merge two Python dictionaries.
dict_5_1 = { 'one': "1", "two": "2", "three" : "3"}
dict_5_2 = { 'four': "4", "five": "5"}
list_5 = list(dict_5_1.items())+list(dict_5_2.items())
print(dict(list_5))
# # RETURN FUNCTION


def merge_two_dict(dict1,dict2):
    list_5_2 = list(dict1.items())+ list(dict2.items())
    return dict(list_5_2)


print(merge_two_dict(dict_5_1,dict_5_2))

# 6.Write a Python program to remove duplicates from the Dictionary.
dict_6 = { 'one': "1", "two": "2", "three" : "3", 'one': "1", "two": "2", "three" : "3"}
result_6 = dict()
for item in dict_6.items():
    if item not in result_6:
      result_6.update([item])
print(result_6)
# # # RETURN FUNCTION


def remove_duplicates(dict):
    for item in dict.items():
        if item not in result_6:
            result_6.update([item])
    return result_6


print(remove_duplicates(dict_6))

# 7. Write a Python program to remove spaces from dictionary keys.
dict_7 = { ' one ': "1", " two ": "2", " three " : "3"}
for key in dict_7:
    updated_key = key.strip()
    dict_7[updated_key] = dict_7.pop(key)
print(dict_7)
# # # RETURN FUNCTION


def space_removal(dict):
    for key in dict:
        updated_key_2 = key.strip()
        dict_7[updated_key_2]= dict_7.pop(key)
    return dict_7


print(space_removal(dict_7))

# 8. Write a Python program to get the maximum and minimum value in a dictionary.
dict_8 = { 'one': "100", "two": "200", "three" : "300", 'four': "500", "five": "10000", "six" : "1"}
list_8 = list(dict_8.values())
max_8 = max(list_8, key=int)
print(max_8)
min_8 = min(list_8, key=int)
print(min_8)
# # # # RETURN FUNCTION # # # Comment : i don't know, how to combine them in one function :):


def max_function(dict):
    return max(list_8, key=int)


def min_function(dict):
    return min(list_8, key=int)


print(max_function(dict_8))
print(min_function(dict_8))

# 9.Write a Python program to check a dictionary is empty or not.
dict_9 = dict()
count = 0
for item in dict_9.items():
    print(item)
    count +=1
print(count == 0)
# #OR:
res= not bool(dict_9)
print(res)
# # # # RETURN FUNCTION #


def empty_dict(dict):
    return not bool(dict_9)


print(empty_dict(dict_9))

# 10.Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
com_dict = Counter(d1)+Counter(d2)
print(com_dict)
# # # # # # RETURN FUNCTION #


def combined_dict(d1, d2):
    com_dict_2 = Counter(d1) + Counter(d2)
    return com_dict_2


print(combined_dict(d1, d2))

# 11. Write a Python program to print a dictionary line by line.
dict_11 = dict(Hungary = 'hungarian', Russia = 'russian', Italy = 'italian')
for key11, value11 in dict_11.items():
    print(key11 +' : '+value11)
# # # # # # RETURN FUNCTION #
## Can't find how to use Return statement in for loop















import logging
logging.basicConfig(filename='Prog22.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
Question1
Create a function that takes three parameters where:
•	x is the start of the range (inclusive).
•	y is the end of the range (inclusive).
•	n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
'''


def list_operation(x,y,n):
    ' return number within range start to end which is divisible by divisor '
    try:
        logging.info('entering list_operation fun')
        if type(x) == int and type(y) == int and type(n) == int:
            result = []
            for i in range(x, y + 1):
                if i % n == 0:
                    result.append(i)
            return result
        else:
            raise TypeError("all inputs should be integers")
    except Exception as e:
        logging.error(e)


# print(list_operation(7,9,5))
'''
Question2
Create a function that takes in two lists and returns True if the second list follows the first list by one element, 
and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.
Examples
simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes
•	Both input lists will be of the same length, and will have a minimum length of 2.
•	The values of the 0-indexed element in the second list and the n-1th indexed element in the first list do not matter.
'''


def simon_says(list1,list2):
    ' return True if list2 follows list1 by one element '
    try:
        logging.info('Entering simon_says function')
        if type(list1) == list and type(list2) == list:
            if list1[:-1] == list2[1:]:
                return True
            else:
                return False
        else:
            raise TypeError('Give inputs in lists of same length')
    except Exception as e:
        logging.error(e)


# print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
'''
Question3
A group of friends have decided to start a secret society. The name will be the first letter of each of their names, 
sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.
Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])
'''


def society_name(names):
    ' takes a list of names and return the name as first letter of each name alphabetically '
    try:
        logging.info('entering society_name function')
        if type(names) == list:
            names.sort()
            result = ''
            for i in names:
                if type(i) ==str:
                    result = result + i[0].upper()
                else:
                    raise TypeError('All elements in list should be string')
            return result
        else:
            raise TypeError('Input should be a list')
    except Exception as e:
        logging.error(e)


# print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
'''
Question4
An isogram is a word that has no duplicate letters. 
Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples
is_isogram("Algorism") ➞ True
is_isogram("PasSword") ➞ False
# Not case sensitive.
is_isogram("Consecutive") ➞ False
Notes
•	Ignore letter case (should not be case sensitive).
•	All test cases contain valid one word strings.
'''


def is_isogram(word):
    ' takes a word input and tell if it is an isogram or not '
    try:
        logging.info('Entering is_isogram function')
        if type(word) == str:
            word = word.lower()
            unique = list(set(word))
            for i in word:
                if word.count(i) >1 :
                    return False
            return True
        else:
            raise TypeError('Please give string input')
    except Exception as e:
        logging.error(e)


# print(is_isogram("Consecutive"))
'''
Question5
Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
Examples
is_in_order("abc") ➞ True
is_in_order("edabit") ➞ False
is_in_order("123") ➞ True
is_in_order("xyzz") ➞ True
Notes
You don't have to handle empty strings.
'''


def is_in_order(word):
    ' check whether string letters are in order or not '
    try:
        if type(word) == str:
            ordered = ''.join(sorted(word))
            if ordered == word:
                return True
            else:
                return False
        else:
            raise TypeError('Please give input in string')
    except Exception as e:
        logging.error(e)


# print(is_in_order("123"))

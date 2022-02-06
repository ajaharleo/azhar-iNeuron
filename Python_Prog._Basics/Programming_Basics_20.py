import logging
logging.basicConfig(filename='Prog20.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question1
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []
'''
def filter_list(list_inp):
    ' take a list of string and integers then return list with integers only '
    try:
        logging.info('Filtering items with filter_list() function')
        if type(list_inp) == list:
            result = []
            for i in list_inp:
                if type(i) == int:
                    result.append(i)
            return result
        else:
            raise TypeError('Please give input as a list')
    except Exception as e:
        logging.error(e)


# print(filter_list(["A", 0, "Edabit", 1729, "Python",-3, "1729"]))
'''
Question2
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. 
This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
'''
def add_indexes(list_inp):
    ' take a list of numbers and return the same list but index of each item added to the item '
    try:
        logging.info('Filtering items with add_indexes() function')
        if type(list_inp) == list:
            result = [i+list_inp[i] for i in range(len(list_inp))]
            return result
        else:
            raise TypeError('Please give input as a list')
    except Exception as e:
        logging.error(e)


# print(add_indexes([5, 4, 3, 2, 1]))
'''
Question3
Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth.
 See the resources tab for the formula.
 Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0
'''


def cone_volume( height, radius):
    ' take height and radius as input and return volume of cone '
    try:
        logging.info('Entering cone_volume function')
        import math
        volume = (1/3)*math.pi *(radius**2)*height
        return round(volume,2)
    except Exception as e:
        logging.error(e)


# print(cone_volume(15,6))
'''
Question4
This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are: 
1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number of the sequence.
Examples
triangle(1) ➞ 1
triangle(6) ➞ 21
triangle(215) ➞ 23220
'''


def triangle(number):
    ' give the nth iteration of the given series '
    try:
        logging.info('Entering triangle function')
        if type(number) == int:
            if number == 1:
                return 1
            else :
                return number+triangle(number-1)
        else:
            raise TypeError("please input nth iteration in integer")
    except Exception as e:
        logging.error(e)


# print(triangle(215))
'''
Question5
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
'''


def missing_num(list_num):
    ' takes a list of numbers between 1 and 10 and returns the missing number '
    try:
        if type(list_num) == list:
            standard = list(range(1,11))
            for i in list_num:
                standard.remove(i)
            return standard[0]
        else:
            raise TypeError('Please give list input')
    except Exception as e:
        logging.error(e)


# print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
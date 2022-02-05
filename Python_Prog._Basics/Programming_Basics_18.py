import logging
logging.basicConfig(filename='Prog18.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question 1
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
'''

def filter_list(list_inp):
    ' return list with positive integer '
    try:
        logging.info('Filterig items with filter_list() function')
        if type(list_inp) == list:
            result = []
            for i in list_inp:
                if type(i) == int:
                    if i >=0:
                        result.append(i)
            return result
        else:
            raise TypeError('Please give input as a list')
    except Exception as e:
        logging.error(e)


# print(filter_list([1, 2, "aasf", "1", "123", 123]))

'''
Question 2
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"
reverse("ReVeRsE") ➞ "eSrEvEr"
reverse("Radar") ➞ "RADAr"
'''

def reverser(word):
    ' takes a string as input and returns string in reverse order, with the opposite case '
    try:
        logging.info("Entering reverser function")
        if type(word) == str:
            word = word[::-1]
            result = ''
            for i in word:
                if i.islower():
                    result += i.upper()
                elif i.isupper():
                    result += i.lower()
                else:
                    result += i
            return result
        else:
            raise TypeError('Please give input in string format')
    except Exception as e:
        logging.error(e)


# print(reverser("ReVeRsE"))

'''
Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way.
Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
first  ➞ 1
middle ➞ [2, 3, 4, 5]
last ➞ 6
Your task is to unpack the list writeyourcodehere into three variables,
 being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.
'''

def destructing(list_inp):
    ' take list as input return first,middle and last '
    try:
        logging.info('entering destructing function')
        if type(list_inp) == list:
            first, *middle, last = list_inp
            return first, middle, last
        else:
            raise TypeError('Please give input in list')
    except Exception as e:
        logging.error(e)


# print(destructing([1, 2, 3, 4, 5, 6]))

'''
Question 4
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
'''

def factorial(number):
    ' return factorial of given number '
    try:
        logging.info('entering factorial function')
        if type(number) == int:
            if number == 0:
                return  0
            elif number == 1:
                return  1
            else :
                return factorial(number-1)*number
        else:
            raise TypeError('Please type positive integer only')
    except Exception as e:
        logging.error(e)


# print(factorial(5))

'''
Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
'''


def move_to_end(list_inp, element):
    ' take input as list and an element from the list returns list as element at end '
    try:
        logging.info('entering move_to_end function')
        if type(list_inp) == list:
            if element not in list_inp:
                raise ValueError('element not found')
            else:
                occurance = list_inp.count(element)
                result = []
                for i in list_inp:
                    if i != element:
                        result.append(i)
                for i in range(occurance):
                    result.append(element)
            return result
        else:
            raise TypeError('Give input in list format')
    except Exception as e:
        logging.error(e)


# print(move_to_end([1, 3, 2, 4, 4, 1],1))

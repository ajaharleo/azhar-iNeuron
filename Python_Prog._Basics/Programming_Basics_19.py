import logging

logging.basicConfig(filename='Prog19.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
Question1
Create a function that takes a string and returns a string in which each character is repeated once.
Examples
double_char("String") ➞ "SSttrriinngg"
double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
double_char("1234!_ ") ➞ "11223344!!__  "
'''
def double_char(string_input):
    ' takes a string input and return the same string with each character repeated once'
    try:
        logging.info('Entering double_char function')
        if type(string_input) == str:
            result = ''
            for i in string_input:
                result += 2*i
            return result
        else:
            raise TypeError('Please give input in string format')
    except Exception as e:
        logging.error(e)


# print(double_char("Hello World!"))
'''
Question2
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ "boolean expected"
reverse(None) ➞ "boolean expected"
'''
def reverser(bool_ip):
    ' takes a boolean and return reverse of it else return "boolean expected" '
    try:
        logging.info('Please give valid input')
        if type(bool_ip) == bool:
            return not bool_ip
        else:
            return "boolean expected"
    except Exception as e :
        logging.error(e)


# print(reverser('False'))
'''
Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. 
The paper starts off with a thickness of 0.5mm.
Examples
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)
num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)
num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
'''
def num_layers(initial,number):
    ' take initial thickness and number of folds then return thickness after folding '
    try:
        logging.info('entering num_layers function')
        if type(initial) == float and type(number) == int:
            for i in range(1,number+1):
                initial = initial*2
            result = str(initial/1000)+'m'
            return result
        else:
            raise TypeError('First input should be input and second should be float')
    except Exception as e:
        logging.error(e)


# print(num_layers(0.5,21))
'''
Question4
Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]
index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
index_of_caps("determine") ➞ []
index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
index_of_caps("sUn") ➞ [1]
'''


def index_of_caps(string_ip):
    ' take input as string and return indices of capital letters '
    try:
        logging.info('entering index_of_caps function')
        if type(string_ip) == str:
            result = []
            for i in range(len(string_ip)):
                if string_ip[i].isupper():
                    result.append(i)
            return result
        else:
            raise TypeError('input should be in string format')
    except Exception as e:
        logging.error(e)


# print(index_of_caps("eDaBiT"))
'''
Question5
Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]
'''
def find_even_nums(number):
    ' take integer as input then returns list of event number from 1 to given number '
    try:
        logging.info('entering find_even_nums function')
        if type(number) == int:
            result = [i for i in range(1,number+1) if i%2==0]
            return result
        else:
            raise TypeError('First input should be input and second should be float')
    except Exception as e:
        logging.error(e)


# print(find_even_nums(2))
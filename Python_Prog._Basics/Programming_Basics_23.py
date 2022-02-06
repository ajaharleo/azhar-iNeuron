import  logging
logging.basicConfig(filename='Prog23.log', level=logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')

'''
Question 1
Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True
'''


def is_symmetrical(number):
    ' return true if number is symmetrical else return false'
    try:
        logging.info('entering is_symmetrical function')
        if type(number) == int:
            num_str = str(number)
            if num_str == num_str[::-1]:
                return True
            else:
                return False
        else:
            raise TypeError('Please give integer input')
    except Exception as e:
        logging.error(e)


# print(is_symmetrical(1112111))
'''
Question 2
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20
'''


def multiply_nums(number_str):
    ' give numbers in a string then return product of these '
    try:
        logging.info('entering multiply_nums function')
        if type(number_str) == str:
            num_list = number_str.split(', ')
            multiplication = 1
            for i in num_list:
                multiplication *= int(i)
            return multiplication
        else:
            raise ValueError('all values should be numbers')
    except Exception as e:
        logging.error(e)


# print(multiply_nums("54, 75, 453, 0"))
'''
Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.
'''


def square_digits(number):
    ' take integers as input the then return integer as each number replaced by its square in integer '
    try:
        logging.info('entering square_digits function')
        if type(number) == int:
            result = ''
            for i in str(number):
                result += str(int(i)**2)
            return int(result)
        else:
            raise ValueError('Input should be an integer')
    except Exception as e:
        logging.error(e)


# print(square_digits(2483))
'''
Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
'''


def setify(list_ip):
    ' take a list of numbers and return sorted list with unique items '
    try:
        logging.info('entering setify function')
        if type(list_ip) == list:
            list_ip.sort()
            return list(set(list_ip))
        else:
            raise ValueError('Input should be a list')
    except Exception as e :
        logging.error(e)


# print(setify([3, 3, 3, 2, 1]))
'''
Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
•	The mean of all digits is the sum of digits / 
how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
•	The mean will always be an integer.
'''


def mean_n(number):
    ' take number as input and return mean of all digits in number '
    try:
        logging.info('entering mean_n function')
        if type(number) == int:
            total,count = 0,0
            for i in str(number):
                count += 1
                total += int(i)
            return total//count
        else:
            raise ValueError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(mean_n(666))

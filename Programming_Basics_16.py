import logging
logging.basicConfig(filename='Prog16.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question1. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each,
and then the word is pronounced with a question mark ?.
Examples
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"
Hint :- Assume all input is in lower case and at least two characters long.
'''
def question1(word):
    ' converts given word as some stuttering comment '
    try:
        logging.info('Trying to stutter given word')
        if type(word) == str:
            result = word[:2]+'... '+word[:2]+'... '+word+'?'
            return result
        else:
            raise TypeError('Please give input in string format and len >2')
    except Exception as e:
        logging.error(e)


# print(question1('incredible'))

'''
Question 2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3
radians_to_degrees(20) ➞ 1145.9
radians_to_degrees(50) ➞ 2864.8
'''

def question2(radians):
    ' take angle in radian and return in degree '
    try:
        logging.info('Function to convert radians to degree')
        if type(radians) == int or type(radians) == float:
            import math
            degree = 180*radians/(math.pi)
            return round(degree,1)
        else:
            raise TypeError('Input should be a real number')
    except Exception as e :
        logging.error(e)


# print(question2(1))

'''
Question 3. In this challenge, establish if a given integer num is a Curzon number. 
If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11
is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21
is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29
'''

def question3(number):
    ' return True if given number is curzon number else False'
    try:
        logging.info('Checking number a curzon or not')
        if type(number) == int:
            numerator = 2**number + 1
            denominator = 2* number + 1
            if numerator%denominator == 0:
                return True
            else:
                return False
        else:
            raise TypeError('Give input in integer')
    except Exception as e:
        logging.error(e)


# print(question3(14))

'''
Question 4.Given the side length x find the area of a hexagon.
 
Examples
area_of_hexagon(1) ➞ 2.6
area_of_hexagon(2) ➞ 10.4
area_of_hexagon(3) ➞ 23.4
'''

def question4(side):
    ' side is given return area of hexagon '
    try:
        logging.info('calculating area of hexagon')
        if type(side) == int or type(side) == float:
            tri_area = (3**0.5)*(side**2)/4
            area = 6 * tri_area
            return round(area,1)
    except Exception as e:
        logging.error(e)


# print(question4(2))
'''
Question 5. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number.
To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, 
now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
Examples
binary(1) ➞ "1"
# 1*1 = 1
binary(5) ➞ "101"
# 1*1 + 1*4 = 5
binary(10) ➞ "1010"
# 1*2 + 1*8 = 10
'''


def question5(decimal_number):
    ' return given decimal number in binary number '
    try:
        if type(decimal_number) == int:
            result_list = []
            while decimal_number >1 :
                result_list.append(str(decimal_number%2))
                decimal_number = decimal_number//2
            if decimal_number == 1:
                result_list.append(str(1))
            return  ''.join(result_list)[::-1]
    except Exception as e:
        logging.error(e)


# print(question5(10))
import logging
import math

logging.basicConfig(filename='Prog12.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. For this challenge, forget how to add two numbers together. The best explanation on what to do for this function is this meme:
Examples
meme_sum(26, 39) ➞ 515
# 2+3 = 5, 6+9 = 15
# 26 + 39 = 515
meme_sum(122, 81) ➞ 1103
# 1+0 = 1, 2+8 = 10, 2+1 = 3
# 122 + 81 = 1103
meme_sum(1222, 30277) ➞ 31499
'''


def meme_sum(num1, num2):
    ' add numbers as a toddler '
    try:
        logging.info('entering meme_sum() function')
        if type(num1) == int and type(num2) == int:
            num1_str = str(num1)
            num2_str = str(num2)
            minm = min(len(num1_str), len(num2_str))
            result = ''
            for i in range(-1,-(minm+1),-1):
                result = str(int(num1_str[i])+int(num2_str[i])) + result
            if len(num1_str) == len(num2_str):
                pass
            elif len(num1_str) == minm:
                result = num2_str[:(len(num2_str)-minm)] + result
            elif len(num2_str) == minm:
                result = num1_str[:(len(num1_str)-minm)] + result
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(meme_sum(26,39))
'''
2. Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
Examples
next_prime(12) ➞ 13
next_prime(24) ➞ 29
next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
'''
from Programming_Advance_1 import prime_checker


def next_prime(number):
    ' if given number is prime then return itself else return next prime '
    try:
        logging.info('entering next_prime() function')
        if type(number) == int:
            if prime_checker(number):
                return number
            else:
                while prime_checker(number) == False:
                    number += 1
            return number
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(next_prime(24))
'''
3. If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph 
then their average speed traveled was 30mph.
Write a function that returns the average speed traveled given an uphill time, 
uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.
Examples
ave_spd(18, 20, 60) ➞ 30
ave_spd(30, 10, 30) ➞ 15
ave_spd(30, 8, 24) ➞ 12
'''


def ave_spd(up_time,up_rate,down_rate):
    ' caluculate average speed for given uphill time uphill rate and downhill rate '
    try:
        logging.info('entering ave_spd() function')
        if type(up_time) == int or type(up_time) == float:
            distance = up_rate*up_time/60
            average_spd = 2*distance / ((up_time/60)+(distance/down_rate))
            return average_spd
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(ave_spd(30,10,30))
'''
4. The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero 
whose factorial is exactly divided by the number.
kempner(6) ➞ 3
1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0
kempner(10) ➞ 5
1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0
A Kempner Function applied to a prime will always return the prime itself.
kempner(2) ➞ 2
kempner(5) ➞ 5
Given an integer n, implement a Kempner Function.
Examples
kempner(6) ➞ 3
kempner(10) ➞ 5
kempner(2) ➞ 2
'''
def factorial(number):
    ' return factorial of given number '
    result = 1
    for i in range(1,number+1):
        result *= i
    return result


def kempner(number):
    ' returns the smallest integer whose factorial can be divided by the given number '
    try:
        logging.info('entering kempner() function')
        if type(number) == int:
            if prime_checker(number):
                return number
            else:
                fac = 1
                while True:
                    if factorial(fac) % number ==0:
                        return fac
                    else:
                        fac += 1
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(kempner(13))
'''
5. You work in a factory, and your job is to take items from a conveyor belt and pack them into boxes. 
Each box can hold a maximum of 10 kgs. Given a list containing the weight (in kg) of each item, 
how many boxes would you need to pack all of the items?
Example
boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]) ➞ 5
# Box 1 = [2, 1, 2, 5] (10kg)
# Box 2 = [4, 3] (7kg)
# Box 3 = [6, 1, 1] (8kg)
# Box 4 = [9] (9kg)
# Box 5 = [3, 2] (5kg)
'''

'''
the above problem statement seems contradictory to me as it says a box can contain max 10kg but example don't support this
because box 5 items can be adjusted to box 2 and box 3 so overall we need only 4 boxes
if my understanding is not correct then please explain to me on ajaharuddin10217@gmail.com
'''
def boxes(items):
    ' minimum boxes need to pack the item '
    try:
        logging.info('entering boxes() function')
        if type(items) == list:
            return math.ceil(sum(items)/len(items))
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


print(boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]))
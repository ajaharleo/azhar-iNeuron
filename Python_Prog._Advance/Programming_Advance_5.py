import logging
logging.basicConfig(filename='Prog5.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function that takes a number n (integer greater than zero) as an argument, 
and returns 2 if n is odd and 8 if n is even.
You can only use the following arithmetic operators: 
addition of numbers +, subtraction of numbers -, multiplication of number *, division of number /, and exponentiation **.
You are not allowed to use any other methods in this challenge (i.e. no if statements, comparison operators, etc).
Examples
f(1) ➞ 2
f(2) ➞ 8
f(3) ➞ 2
'''


def odd_even(number):
    ' tells odd even without using if else and comparison operator '
    try:
        logging.info('entering odd_even function')
        if type(number) == int:
            output = [8, 2]
            return output[number%2]
        else:
            raise TypeError('Input should be integers')
    except Exception as e:
        logging.error(e)


' could not find a way without using ramainder operator'
# print(odd_even(34))
'''
2. Create a function that returns the majority vote in a list. 
A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
Examples
majority_vote(["A", "A", "B"]) ➞ "A"
majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
'''


def majority_vote(votes):
    ' return majority string from given strings '
    try:
        logging.info('entering odd_even function')
        if type(votes) == list:
            unique = list(set(votes))
            for i in unique:
                if votes.count(i) > len(votes)/2:
                    return i
        else:
            raise TypeError('Input should be integers')
    except Exception as e:
        logging.error(e)


# print(majority_vote(["A", "B", "B", "A", "C", "C"]))
'''
3. Create a function that takes a string txt and censors any word from a given list lst. 
The text removed must be replaced by the given character char.
Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
'''


def censor_string(text,censor_items,censor_char):
    ' censor specific words with the character given in the string '
    try:
        logging.info('entering odd_even function')
        if type(text) == str and type(censor_items) == list and type(censor_char) == str:
            text_items = text.split()
            import re
            for i in censor_items:
                text = re.sub(rf"{i.lower()}", '*' * len(i), text)
            return text
        else:
            raise TypeError('Input should be string,list and string')
    except Exception as e:
        logging.error(e)


# print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
'''
4. In mathematics a Polydivisible Number (or magic number) is a number in a given number base with digits abcde... 
that has the following properties:
-  Its first digit a is not 0.
- The number formed by its first two digits ab is a multiple of 2.
- The number formed by its first three digits abc is a multiple of 3.
- The number formed by its first four digits abcd is a multiple of 4.
Create a function which takes an integer n and returns True if the given number is a Polydivisible Number and False otherwise.
Examples
is_polydivisible(1232) ➞ True
# 1     / 1 = 1
# 12    / 2 = 6
# 123   / 3 = 41
# 1232  / 4 = 308
is_polydivisible(123220 ) ➞ False
# 1   / 1 = 1
# 12   / 2 = 6
# 123   / 3 = 41
# 1232   / 4 = 308
# 12322   / 5 = 2464.4         # Not a Whole Number
# 123220   /6 = 220536.333...  # Not a Whole Number
'''


def is_polydivisible(number):
    ' return True if number is polydivisible else return False '
    try:
        logging.info('entering is_polydivisible function')
        if type(number) == int:
            num_str = str(number)
            for i in range(1,len(num_str)+1):
                if int(num_str[:i]) % i == 0:
                    continue
                else:
                    return False
            return True
        else:
            raise TypeError('Input should be integers')
    except Exception as e:
        logging.error(e)


# print(is_polydivisible(123220))
'''
5. Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
sum_primes([]) ➞ None
'''


def sum_primes(numbers):
    ' return sum of primes numbers from given numbers '
    try:
        logging.info('entering odd_even function')
        if type(numbers) == list:
            if len(numbers) == 0:
                return []
            total = 0
            from Programming_Advance_1 import prime_checker # import function from previous assignment file
            for i in numbers:
                if prime_checker(i):
                    total += i
            return total
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(sum_primes([]))

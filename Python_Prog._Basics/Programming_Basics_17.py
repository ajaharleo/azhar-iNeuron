import logging
logging.basicConfig(filename='Prog17.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''

def question1(start,end,divisor):
    ' return number within range start to end which is evenly divisible by divisor '
    try:
        logging.info('entering question1 fun')
        if type(start) == int and type(end) == int and type(divisor) == int:
            if divisor > end :
                return 0
            else:
                result = []
                for i in range(start,end+1):
                    if i % divisor == 0:
                        result.append(i)
            return sum(result)

        else:
            raise TypeError("all inputs should be integers")
    except Exception as e:
        logging.error(e)


# print(question1(1,10,2))

'''
Question2. Create a function that returns True if a given inequality expression is correct and False otherwise.
Examples
correct_signs("3 < 7 < 11") ➞ True
correct_signs("13 > 44 > 33 > 1") ➞ False
correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
'''

def question2(statement):
    ' return True if given expression is correct else false '
    return eval(statement)


# print(question2("1 < 2 < 6 < 9 > 3"))

'''
Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
'''


def replace_vowels(statement,special_case):
    ' take a string and a special character as input then replaces all vowels in the string with special character '
    try:
        logging.info('entering replace_vowels() function')
        if type(statement) == str:
            for i in range(len(statement)):
                if statement[i] in 'aeiou':
                    statement = statement[:i] + special_case + statement[i + 1:]
            return statement
        else:
            raise TypeError('give input in string format')
    except Exception as e:
        logging.error(e)



# print(replace_vowels('minnie mouse','?'))
'''
Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
'''


def factorial(number):
    ' return factorial of given number '
    try:
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
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"
Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1
'''

def hamming_distance(stat1,stat2):
    ' return hamming number of two strings '
    try:
        if type(stat1)==str and type(stat2)==str:
            if len(stat1) != len(stat2):
                raise IOError('strings should be of same length')
            else:
                hamming = 0
                for i in range(len(stat2)):
                    if stat2[i] != stat1[i]:
                        hamming += 1
                return hamming
        else:
            raise TypeError('Both should be string')
    except Exception as e:
        logging.error(e)


# print(hamming_distance("strong", "strung"))



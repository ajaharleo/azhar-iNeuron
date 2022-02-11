import logging
logging.basicConfig(filename='Prog2.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Write a function that takes a positive integer num and calculates 
how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. 
On the third, there are 16 dots, and on the fourth there are 31 dots.
Return the number of dots that exist in the whole pentagon on the Nth iteration.
Examples
pentagonal(1) ➞ 1
pentagonal(2) ➞ 6
pentagonal(3) ➞ 16
pentagonal(8) ➞ 141
'''


def pentagonal(n_iteration):
    'return number of dots inside the pentagon accordig to logic above'
    try:
        logging.info('entering pentagonal function')
        if type(n_iteration) == int:
            dots_inside_pentagon = [0,1]
            dots_on_pentagon = [0,5]
            if n_iteration < 1:
                return 0
            elif n_iteration == 1:
                return 1
            else:
                for i in range(2,n_iteration+1):
                    dots_inside_pentagon.append(dots_inside_pentagon[-1]+dots_on_pentagon[-1])
                    dots_on_pentagon.append(dots_on_pentagon[-1]+5)
            return dots_inside_pentagon[-1]
        else:
            raise TypeError('Enter iteration in integer format')
    except Exception as e:
        logging.error(e)


# print(pentagonal(8))
'''
2.  Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
a => 0
e => 1
i => 2
o => 2
u => 3
# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"
Examples
encrypt("banana") ➞ "0n0n0baca"
encrypt("karaca") ➞ "0c0r0kaca"
encrypt("burak") ➞ "k0r3baca"
encrypt("alpaca") ➞ "0c0pl0aca"
'''


def encrypt(statement):
    ' return encrypted string as given logic '
    try:
        logging.info('entering encrypt function')
        if type(statement) == str:
            vowels = {"a":0,'A':0,'e':1, 'E':1,'i':2,'I':2,'o':3,'O':3,'u':4,'U':4}
            statement = statement[::-1]
            result = ''
            for i in statement:
                if i in vowels:
                    result += str(vowels[i])
                else:
                    result += i
            result += 'aca'
            return result
        else:
            raise TypeError('enter input in a string')
    except Exception as e:
        logging.error(e)


# print(encrypt('banana'))
'''
3. Given the month and year as numbers, return whether that month contains a Friday 13th.(i.e You can check Python's datetime module)
Examples
has_friday_13(3, 2020) ➞ True
has_friday_13(10, 2017) ➞ True
has_friday_13(1, 1985) ➞ False
'''


def has_friday_13(month_, year_):
    ' return True if given month of year has date 13 on Friday '
    try:
        logging.info('entering has_friday_13() function')
        import datetime
        if type(month_) == int and type(year_) == int:
            if datetime.date(year_, month_, 13).weekday() == 4:
                return True
            else:
                return False
        else:
            raise TypeError('Input should be in integer format')
    except Exception as e:
        logging.error(e)


# print(has_friday_13(10,2017))
'''
4. Write a regular expression that will help us count how many bad cookies are produced every day. You must use RegEx negative lookbehind.
Example
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = "yourregularexpressionhere"
len(re.findall(pattern, ", ".join(lst))) ➞ 2
'''
import re
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = r'(?<!good\s)cookie'
# print(len(re.findall(pattern, ", ".join(lst))))

'''
5. Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
pluralize(["table", "table", "table"]) ➞ { "tables" }
pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
'''


def pluralize(words):
    ' return a set of words given in list, pluaralize if multiple occurance '
    try:
        logging.info('entering pluralize() function')
        if type(words):
            unique = set(words)
            result = []
            for i in range(len(words)):
                if words.count(words[i])>1:
                    result.append(words[i]+'s')
                else:
                    result.append(words[i])
            return set(result)
        else:
            raise TypeError('Input should be a list')
    except Exception as e:
        logging.error(e)


# print(pluralize(["table", "table", "table"]))

import logging
logging.basicConfig(filename='Prog8.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Given a sentence as txt, return True if any two adjacent words have this property: 
One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
Examples
vowel_links("a very large appliance") ➞ True
vowel_links("go to edabit") ➞ True
vowel_links("an open fire") ➞ False
vowel_links("a sudden applause") ➞ False
'''


def vowel_links(sentence):
    try:
        logging.info('entering vowel_links() function')
        if type(sentence) == str:
            vowels = ['a','e','i','o','u']
            words = sentence.split()
            for i in range(len(words)-1):
                if words[i][-1].lower() in vowels and words[i+1][0] in vowels:
                    return True
            return False
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(vowel_links('an open fire'))
'''
2. You are given three inputs: a string, one letter, and a second letter.
Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.
Examples
first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".
first_before_second("knaves knew about waterfalls", "k", "w") ➞  True
first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".
first_before_second("precarious kangaroos", "k", "a") ➞ False
'''


def first_before_second(sentence, first, second):
    try:
        logging.info('entering first_before_second() function')
        if type(sentence) == str and type(first) == str and type(second) == str:
            first_of_second = sentence.index(second)
            if first in sentence[first_of_second:]:
                return False
            return True
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(first_before_second("precarious kangaroos", "k", "a"))
'''
3. Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. 
The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).
Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions
char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions
char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]
'''


def char_at_pos(items, specifier):
    try:
        logging.info('entering char_at_pos() function')
        if (type(items) == str or type(items) == list) and type(specifier) == str:
            if type(items) == list:
                result = []
                for i in range(len(items)):
                    if specifier == 'odd':
                        if i%2 == 0:
                            result.append(items[i])
                    elif specifier == 'even':
                        if i%2 != 0:
                            result.append(items[i])
                    else:
                        raise KeyError('Wrong specifiers')
            else:
                result = ''
                for i in range(len(items)):
                    if specifier == 'odd':
                        if i % 2 == 0:
                            result += items[i]
                    elif specifier == 'even':
                        if i % 2 != 0:
                            result += items[i]
                    else:
                        raise KeyError('Wrong specifiers')
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))
'''
4. Write a function that returns the greatest common divisor of all list elements. If the greatest common divisor is 1, return 1.
Examples
GCD([10, 20, 40]) ➞ 10
GCD([1, 2, 3, 100]) ➞ 1
GCD([1024, 192, 2048, 512]) ➞ 64
'''


def GCD(items):
    try:
        logging.info('entering GCD() function')
        if type(items) == list:
            gcd = min(items)
            while gcd >= 1 :
                count = 0
                for i in items:
                    if i % gcd ==0:
                        count += 1
                if count == len(items):
                    return gcd
                else:
                    gcd = gcd -1
            return 1
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(GCD([1024, 192, 2048, 512]))
'''
5. A number/string is a palindrome if the digits/characters are the same when read both forward and backward. 
Examples include "racecar" and 12321. Given a positive number n, check if n or the binary representation of n is palindromic. 
Return the following:
- "Decimal only." if only n is a palindrome.
- "Binary only." if only the binary representation of n is a palindrome.
- "Decimal and binary." if both are palindromes.
- "Neither!" if neither are palindromes.
Examples
palindrome_type(1306031) ➞ "Decimal only."
# decimal = 1306031
# binary  = "100111110110110101111"
palindrome_type(427787) ➞ "Binary only."
# decimal = 427787
# binary  = "1101000011100001011"
palindrome_type(313) ➞ "Decimal and binary."
# decimal = 313
# binary  = 100111001
palindrome_type(934) ➞ "Neither!"
# decimal = 934
# binary  = "1110100110"
'''


def palindrome_type(number):
    try:
        logging.info('entering palindrome_type() function')
        if type(number) == int:
            binary_num = format(number,'b')
            num_pal, bin_pal = False, False
            if str(number) == str(number)[::-1]:
                num_pal = True
            if str(binary_num) == str(binary_num)[::-1]:
                bin_pal = True
            if num_pal == True and bin_pal ==True:
                return "Decimal and binary."
            elif num_pal == True and bin_pal ==False:
                return "Decimal only."
            elif num_pal == False and bin_pal ==True:
                return "Binary only."
            else:
                "Neither!"
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(palindrome_type(313))

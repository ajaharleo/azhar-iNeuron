import logging
logging.basicConfig(filename='Prog1.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Write a function that takes a list of lists and returns the value of all of the symbols in it, 
where each symbol adds or takes something from the total score. Symbol values:
# = 5
O = 3
X = 1
! = -1
!! = -3
!!! = -5
A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and 
a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
check_score([["#", "!"],["!!", "X"]]) ➞ 2
check_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]]) ➞ 0
'''


def check_score(lst_inp):
    ' takes a list of lists and return result according to the above details '
    try:
        logging.info('entering check_score() function')
        if type(lst_inp) == list:
            values = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
            result = 0
            for i in lst_inp:
                for j in i:
                    result += values[j]
            if result<0:
                return  0
            else:
                return result
        else:
            raise TypeError('Please enter a list')
    except Exception as e:
        logging.error(e)


# print(check_score([["#", "!"],["!!", "X"]]))
'''
2. Create a function that takes a variable number of arguments, each argument representing the number of items in a group,
and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
Examples
combinations(2, 3) ➞ 6
combinations(3, 7, 4) ➞ 84
combinations(2, 3, 4, 5) ➞ 120
'''


def combinations(*args):
    ' take variable number of integers and return possible combinations '
    try:
        logging.info('entering combinations funciton')
        result = 1
        for i in args:
            if type(i) == int:
                result *= i
            else:
                raise TypeError('All inputs should be integers')
        return result
    except Exception as e:
        logging.error(e)


# print(combinations(2,5,3,4))


'''
3. Create a function that takes a string as an argument and returns the Morse code equivalent.
Examples
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
This dictionary can be used for coding:
'''
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}


def encode_morse(str_inp):
    ' takes a string and return morse coded string '
    try:
        logging.info('entering encode_morse() function')
        if type(str_inp)==str:
            result = ''
            for i in str_inp:
                result += char_to_dots[i]
            return result
        else:
            raise TypeError
    except Exception as e:
        logging.error(e)


# print(encode_morse('EDABBIT CHALLENGE'))


'''
4.  Write a function that takes a number and returns True if it's a prime; False otherwise. 
The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit.
Examples
prime(7) ➞ True
prime(56963) ➞ True
prime(5151512515524) ➞ False
'''


def prime_checker(number):
    try:
        logging.info('entering prime_checker function')
        if type(number)==int:
            if number < 2:
                return False
            for i in range(2,int(number**0.5)+1):
                if number % i ==0:
                    return False
            else :
                return True
        else:
            raise TypeError('Entering prime_chcker() function')
    except Exception as e:
        logging.error(e)


# print(prime_checker(56963963963))


'''
5.  Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:
    1. Locate the position of the letter in the English alphabet (from 1 to 26).
    2. Odd positions will be represented as 1 and 0 otherwise.
    3. Convert the represented positions to boolean values, 1 for True and 0 for False.
    4. Store the conversions into an array.
Examples
to_boolean_list("deep") ➞ [False, True, True, False]
# deep converts to 0110
# d is the 4th alphabet - 0
# e is the 5th alphabet - 1
# e is the 5th alphabet - 1
# p is the 16th alphabet - 0
to_boolean_list("loves") ➞ [False, True, False, True, True]
to_boolean_list("tesh") ➞ [False, True, True, False]
'''


def to_boolean_list(word):
    try:
        logging.info('entering to_boolean_list function')
        if type(word)==str:
            bool_word = ''
            odd_even = lambda x : 0 if x%2==0 else 1
            for i in word:
                bool_word += str(odd_even(ord(i.lower())-96))  # taking all alphabets in lower case then get it's ascii number to get oreder
            result = []
            for i in bool_word:
                result.append(bool(int(i)))
            return result
        else:
            raise TypeError('Input should be a string')
    except Exception as e:
        logging.error(e)


# print(to_boolean_list('loves'))
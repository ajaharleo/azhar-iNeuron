import logging
logging.basicConfig(filename='Prog10.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function that takes the width, height and character and returns a picture frame as a 2D list.
Examples
get_frame(4, 5, "#") ➞ [["####"],["#  #"],["#  #"],["#  #"],["####"]]
# Frame is 4 characters wide and 5 characters tall.
get_frame(10, 3, "*") ➞ [["**********"],["*        *"],["**********"]]
# Frame is 10 characters and wide and 3 characters tall.
get_frame(2, 5, "0") ➞ "invalid"
# Frame's width is not more than 2.
'''


def get_frame(width,height,char_):
    try:
        logging.info('entering get_frame() function')
        if type(width) == int and type(height) == int and type(char_) == str:
            result = [[char_*width]]
            result.append([char_ + ' '*(width-2) +char_]*(height-2))
            result.append([char_*width])
            if width < 3 or height <3:
                return 'invalid'
            else:
                return result
        else:
            raise TypeError('Input should be integer and str')
    except Exception as e:
        logging.error(e)


# print(get_frame(10, 3, "*"))
'''
2. Write three functions:
  1. boolean_and
  2. boolean_or
  3. boolean_xor
These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.
Examples
boolean_and([True, True, False, True]) ➞ False
# [True, True, False, True] => [True, False, True] => [False, True] => False
boolean_or([True, True, False, False]) ➞ True
# [True, True, False, True] => [True, False, False] => [True, False] => True
boolean_xor([True, True, False, False]) ➞ False
# [True, True, False, False] => [False, False, False] => [False, False] => False
'''


def boolean_and(booleans):
    try:
        logging.info('entering boolean_and() function')
        if type(booleans) == list:
            while len(booleans) > 1:
                if booleans[0] == True and booleans[1] == True:
                    booleans[1] = True
                    booleans.pop(0)
                else:
                    booleans[1] = False
                    booleans.pop(0)
            return booleans[0]
        else:
            raise TypeError('Input should be list of booleans')
    except Exception as e:
        logging.error(e)


# print(boolean_and([True, True, False, True]))


def boolean_or(booleans):
    try:
        logging.info('entering boolean_or() function')
        if type(booleans) == list:
            while len(booleans) > 1:
                if booleans[0] == False and booleans[1] == False:
                    booleans[1] = False
                    booleans.pop(0)
                else:
                    booleans[1] = True
                    booleans.pop(0)
            return booleans[0]
        else:
            raise TypeError('Input should be list of booleans')
    except Exception as e:
        logging.error(e)


# print(boolean_or([True, True, False, False]))


def boolean_xor(booleans):
    try:
        logging.info('entering boolean_xor() function')
        if type(booleans) == list:
            while len(booleans) > 1:
                if not booleans[0] == True or not booleans[1] == True:
                    booleans[1] = False
                    booleans.pop(0)
                else:
                    booleans[1] = True
                    booleans.pop(0)
            return booleans[0]
        else:
            raise TypeError('Input should be list of booleans')
    except Exception as e:
        logging.error(e)


# print(boolean_xor([True, True, False, False]))
'''
3. Create a function that creates a box based on dimension n.
Examples
make_box(5) ➞ [
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"]
make_box(3) ➞ [
  "###",
  "# #",
  "###"]
make_box(2) ➞ [
  "##",
  "##"]
make_box(1) ➞ ["#"]
'''


def make_box(number):
    try:
        logging.info('entering make_box() function')
        if type(number) == int:
            result = [['#' * number]]
            result.append(['#' + ' ' * (number - 2) + '#'] * (number - 2))
            result.append(['#' * number])
            return result
        else:
            raise TypeError('Input should be int')
    except Exception as e:
        logging.error(e)


# print(make_box(3))
'''
4. Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.
Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True
no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".
no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".
'''


def no_duplicate_letters(phrase):
    try:
        logging.info('entering no_duplicate_letters() function')
        if type(phrase) == str:
            words = phrase.split()
            for i in words:
                if len(i) != len(set(i)):
                    return False
            return True
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
'''
5. Write a regular expression that will match the states that voted yes to President Trump's impeachment. 
You must use RegEx positive lookahead.
Example
txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
pattern = "yourregularexpressionhere"
re.findall(pattern, txt) ➞ ["California", "Florida"]
'''


def yes_vote(text):
    try:
        logging.info('entering yes_vote() function')
        if type(text) == str:
            import re
            pattern = re.compile(r'\w+(?=\s=\syes)')
            return re.findall(pattern, text)
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(yes_vote("Texas = no, California = yes, Florida = yes, Michigan = no"))
import logging
logging.basicConfig(filename='Prog14.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Given a list of numbers, create a function that removes 25% from every number in the list except the smallest number,
 and adds the total amount removed to the smallest number.
Examples
show_the_love([4, 1, 4]) ➞ [3, 3, 3]
show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
show_the_love([2, 100]) ➞ [27, 75]
'''


def show_the_love(items):
    ' from given list of numbers reduces 25% of each numbers except minimum and enhance minimum to the total cut '
    try:
        logging.info('entering show_the_love() function')
        if type(items) == list:
            minm = min(items)
            total = 0
            for i in range(len(items)):
                if items[i] != minm:
                    total += 0.25 * items[i]
                    items[i] = 0.75 * items[i]
            minm_index = items.index(minm)
            items[minm_index] = minm + total
            return items
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(show_the_love([16,10,8]))
'''
2. Create a function that takes in two words as input and returns a list of three elements, in the following order:
   1.Shared letters between two words.
   2.Letters unique to word 1.
   3.Letters unique to word 2.
Each element should have unique letters, and have each letter be alphabetically sorted.
Examples
letters("sharp", "soap") ➞ ["aps", "hr", "o"]
letters("board", "bored") ➞ ["bdor", "a", "e"]
letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should 
# only exist a single "f" in your first element.
letters("match", "ham") ➞ ["ahm", "ct", ""]
# "ham" does not contain any letters that are not found already 
# in "match".
'''


def letters(word1, word2):
    ' take two words and return shared letters,unique in first and unique in second '
    try:
        logging.info('entering find_the_difference() function')
        if type(word1) == str and type(word2) == str:
            first = set(word1)
            second = set(word2)
            shared = first.intersection(second)
            result = ['','','']
            for i in shared:
                result[0] += i
            uniq1 = first.difference(second)
            uniq2 = second.difference(first)
            for i in uniq1:
                result[1] += i
            for i in uniq2:
                result[2] += i
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(letters("match", "ham"))
'''
3. Write a function that pairs the first number in an array with the last, the second number with the second to last, etc.
Examples
pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]
pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]
pairs([]) ➞ []
'''


def pairs(items):
    ' take a list and pair elements from both ends '
    try:
        logging.info('entering pairs() function')
        if type(items) == list:
            result = []
            if len(items) == 0:
                pass
            elif len(items) %2 == 0:
                for i in range(len(items)//2):
                    result.append([items[i],items[-(i+1)]])
            else:
                for i in range(len(items)//2+1):
                    result.append([items[i],items[-(i+1)]])
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(pairs([1,2,3,4,5]))
'''
4. Write a function that adds two numbers. The catch, however, is that the numbers will be strings.
Examples
add_str_nums("4", "5") ➞ "9"
add_str_nums("abcdefg", "3") ➞ "-1"
add_str_nums("1", "") ➞ "1"
add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ "1874682736267235927391936562808774986"
'''


def add_str_nums(num1, num2):
    ' add two numbers given in integer format '
    try:
        logging.info('entering add_str_nums() function')
        if type(num1) == str and type(num2) == str:
            try:
                if len(num2) == 0:
                    return int(num1)
                elif len(num1) == 0:
                    return int(num2)
                else:
                    return int(num1)+int(num2)
            except:
                return -1
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(add_str_nums("1874682736267235927359283579235789257", "32652983572985729"))
'''
5. lPaeesh le pemu mnxit ehess rtnisg! Oh, sorry, that was supposed to say: Please help me unmix these strings!
Somehow my strings have all become mixed up; every pair of characters has been swapped. Help me undo this so 
I can understand my strings again.
Examples
unmix("123456") ➞ "214365"
unmix("hTsii  s aimex dpus rtni.g") ➞ "This is a mixed up string."
unmix("badce") ➞ "abcde"
'''


def unmix(phrase):
    ' unmix the given phrase '
    try:
        logging.info('entering unmix() function')
        if type(phrase) == str:
            result = ''
            for i in range(0,len(phrase)-1,2):
                result += phrase[i+1] + phrase[i]
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(unmix("hTsii  s aimex dpus rtni.g"))

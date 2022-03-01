import logging
logging.basicConfig(filename='Prog19.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a checker board generator, which takes as inputs n and 2 elements to generate an n x n checkerboard with 
those two elements as alternating squares.
Examples
checker_board(2, 7, 6) ➞ [
  [7, 6],
  [6, 7]]
checker_board(3, "A", "B") ➞ [
  ["A", "B", "A"],
  ["B", "A", "B"],
  ["A", "B", "A"]]
checker_board(4, "c", "d") ➞ [
  ["c", "d", "c", "d"],
  ["d", "c", "d", "c"],
  ["c", "d", "c", "d"],
  ["d", "c", "d", "c"]]
checker_board(4, "c", "c") ➞ "invalid"
'''


def checker_board(n, ele1, ele2):
    ' return a checker board of size n*n with given two elements ele1 and ele2 '
    try:
        logging.info('entering checker_board() function')
        if type(n) == int:
            result = [[0 for i in range(n)] for i in range(n)]
            if ele1 == ele2:
                logging.error('Both elements should not be same')
                return 'invalid'
            else:
                for col in range(0,n,2):
                    for row in range(0,n,2):
                        result[row][col] = ele1
                    for alt_row in range(1,n,2):
                        result[alt_row][col] = ele2
                for col in range(1,n,2):
                    for row in range(0,n,2):
                        result[row][col] = ele2
                    for alt_row in range(1,n,2):
                        result[alt_row][col] = ele1
            return result
        else:
            raise TypeError('Value of n should be integer')
    except Exception as e:
        logging.error(e)


# print(checker_board(4,'c','d'))
'''
2. A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. 
Create a function that returns True if a string is an almost-palindrome and False otherwise.
Examples
almost_palindrome("abcdcbg") ➞ True
# Transformed to "abcdcba" by changing "g" to "a".
almost_palindrome("abccia") ➞ True
# Transformed to "abccba" by changing "i" to "b".
almost_palindrome("abcdaaa") ➞ False
# Can't be transformed to a palindrome in exactly 1 turn.
almost_palindrome("1234312") ➞ False
'''


def almost_palindrome(string):
    ' return True if given string is almost a palindrome '
    try:
        logging.info('entering almost_palindrome() function')
        if type(string) == str:
            count = 0
            for i in range(len(string)):
                if string[i] != string[-(i+1)]:
                    count += 1
            if count == 2:
                return True
            else:
                return False
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(almost_palindrome("1234312"))
'''
3. Create a function that finds how many prime numbers there are, up to the given integer.
Examples
prime_numbers(10) ➞ 4
# 2, 3, 5 and 7
prime_numbers(20) ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19
prime_numbers(30) ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
'''


def prime_numbers(number):
    ' tells count of prime numbers upto given number '
    try:
        logging.info('entering prime_numbers() function')
        if type(number) == int:
            count = 0
            for i in range(2,number+1):
                for j in range(2,i):
                    if i%j == 0:
                        break
                else:
                    count += 1
            return count
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(prime_numbers(30))
'''
4. If today was Monday, in two days, it would be Wednesday.
Create a function that takes in a list of days as input and the number of days to increment by. 
Return a list of days after n number of days has passed.
Examples
after_n_days(["Thursday", "Monday"], 4) ➞ ["Monday", "Friday"]
after_n_days(["Sunday", "Sunday", "Sunday"], 1) ➞ ["Monday", "Monday", "Monday"]
after_n_days(["Monday", "Tuesday", "Friday"], 1) ➞ ["Tuesday", "Wednesday", "Saturday"]
'''


def find_the_difference(days_list, after_days):
    ' take a list of days and return the list after incrementing to given integers '
    try:
        logging.info('entering after_n_days() function')
        if type(days_list) == list and type(after_days) == int:
            std = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
            result = []
            for i in days_list:
                for k, v in std.items():
                    if v == i:
                        result.append(std[(k + after_days) % 7])
            return result
        else:
            raise TypeError('Input should be list and integer')
    except Exception as e:
        logging.error(e)


# print(find_the_difference(["Thursday", "Monday"], 4))
'''
5. You are in the process of creating a chat application and want to add an anonymous name feature. 
This anonymous name feature will create an alias that consists of two capitalized words beginning with the same letter as the users first name.
Create a function that determines if the list of users is mapped to a list of anonymous names correctly.
Examples
is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", 
"Marvelous Mouse"]) ➞ True
is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."], ["Reassuring Rat", "Peaceful Panda",
 "Fantastic Frog", "Notable Nickel"]) ➞ True
is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]) ➞ False
# Both words in "Brandishing Mimosa" should begin with a "B" - "Brandishing Beaver" would do the trick.
'''


def is_correct_aliases(names, aliases):
    ' check if given aliases are correct for given names or not '
    try:
        logging.info('entering is_correct_aliases() function')
        if type(names) == list and type(aliases) == list:
            for i in range(len(names)):
                temp_name = names[i].split()
                temp_alias = aliases[i].split()
                if temp_alias[0][0] != temp_name[0][0] or temp_alias[1][0] != temp_name[0][0]:
                    return False
            return True
        else:
            raise TypeError('Input should be lists')
    except Exception as e:
        logging.error(e)


# print(is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]))

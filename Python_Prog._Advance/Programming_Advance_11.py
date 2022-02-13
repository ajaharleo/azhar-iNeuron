import logging
logging.basicConfig(filename='Prog11.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function that takes a list and returns a new list containing only prime numbers.
Examples
filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]
filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]
filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]
'''


def filter_primes(data):
    try:
        logging.info('entering filter_primes() function')
        if type(data) == list:
            #data = list(set(data))
            primes = []
            for number in data:
                for i in range(2, int(number ** 0.5) + 1):
                    if number % i == 0:
                        break
                else:
                    primes.append(number)
            return primes
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))
'''
2. Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.
The effect of a water balloon popping can be modeled using a list. 
Create a function that takes a list which takes the pre-pop state and returns the state after the balloon is popped. 
The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.
Examples
pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
pop([0]) ➞ [0]
'''


def pop_(pre_pop):
    try:
        logging.info('entering pop() function')
        if type(pre_pop) == list:
            mid = len(pre_pop)//2 + 1
            end = len(pre_pop) - 1
            for i in range(1,mid):
                pre_pop[i] = i
                pre_pop[end-i] = i
            return pre_pop
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(pop_([0]))
'''
3. "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, 
saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.
Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal,
 and return the last phrase in all caps. Remember to put a comma and space between phrases.
Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"
loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
loves_me(1) ➞ "LOVES ME"
'''


def loves_me(petals):
    try:
        logging.info('entering loves_me() function')
        if type(petals) == int:
            items = ['Loves me', 'Loves me not']
            result = ''
            for i in range(petals-1):
                if i%2 == 0:
                    result += items[0] + ', '
                else:
                    result += items[1] + ', '
            if petals % 2 == 0:
                result += items[1].upper()
            else:
                result += items[0].upper()
            return result
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


#
# print(loves_me(6))
'''
4. Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).
Examples
sort_by_letter(["932c", "832u32", "2344b"])
➞ ["2344b", "932c", "832u32"]
sort_by_letter(["99a", "78b", "c2345", "11d"])
➞ ["99a", "78b", "c2345", "11d"]
sort_by_letter(["572z", "5y5", "304q2"])
➞ ["304q2", "5y5", "572z"]
sort_by_letter([])
➞ []
'''


def sort_by_letter(items):
    try:
        logging.info('entering sort_by_letter() function')
        if type(items) == list:
            import re
            alpha_num = {}
            for i in items:
                alphas = re.findall(r'[a-zA-Z]',i)
                alpha_num[alphas[-1]]=i
            dic_keys = list(alpha_num.keys())
            dic_keys.sort()
            result = []
            for i in dic_keys:
                result.append(alpha_num[i])
            return result
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
'''
5. There are three cups on a table, at positions A, B, and C. At the start, there is a ball hidden under the cup at position B.
However, I perform several swaps on the cups, which is notated as two letters. 
For example, if I swap the cups at positions A and B, I could notate this as AB or BA.
Create a function that returns the letter position that the ball is at, once I finish swapping the cups. 
The swaps will be given to you as a list.
Example
cup_swapping(["AB", "CA", "AB"]) ➞ "C"
# Ball begins at position B.
# Cups A and B swap, so the ball is at position A.
# Cups C and A swap, so the ball is at position C.
# Cups A and B swap, but the ball is at position C, so it doesn't move.
'''


def cup_swapping(moves):
    try:
        logging.info('entering cup_swapping() function')
        if type(moves) == list:
            position = 'B'
            for i in moves:
                swap = list(i)
                if swap[0] == position:
                    position = swap[1]
                elif swap[1] == position:
                    position = swap[0]
            return position
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(cup_swapping(["AB", "CA", "AB"]))

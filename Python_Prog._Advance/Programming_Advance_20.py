import logging
logging.basicConfig(filename='Prog20.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function based on the input and output. Look at the examples, there is a pattern.
Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"
secret("p.one") ➞ "<p class='one'></p>"
secret("p.four.five") ➞ "<p class='four five'></p>"
'''


def secret(in_string):
    ' return output based on the given input - output pairs '
    try:
        logging.info('entering secret() function')
        if type(in_string) == str:
            words = in_string.split('.')
            result = f"<{words[0]} class='"
            for i in range(1,len(words)):
                result += words[i] + ' '
            result = result[:-1] +f"'></{words[0]}>"
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(secret("p.four.five"))
'''
2. Create a function which counts how many lone 1s appear in a given number. Lone means the number doesn't appear twice or more in a row.
Examples
count_lone_ones(101) ➞ 2
count_lone_ones(1191) ➞ 1
count_lone_ones(1111) ➞ 0
count_lone_ones(462) ➞ 0
'''


def count_lone_ones(number):
    ' returns count of lone numbers '
    try:
        logging.info('entering count_lone_ones() function')
        if type(number) == int:
            num_str = str(number)
            count = 0
            for i in range(1,len(num_str)-1):
                if num_str[i] == '1':
                    if num_str[i+1] == '1' or num_str[i-1] == '1':
                        continue
                    else:
                        count += 1
                if num_str[0] == '1' and num_str[1] != '1':
                    count += 1
                if num_str[-1] == '1' and num_str[-2] != '1':
                    count += 1
            return count
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(count_lone_ones(456))
'''
3. Write a method that accepts two integer parameters rows and cols. 
The output is a 2d array of numbers displayed in column-major order, 
meaning the numbers shown increase sequentially down each column and
 wrap to the top of the next column to the right once the bottom of the current column is reached.
Examples
printGrid(3, 6) ➞ [
  [1, 4, 7, 10, 13, 16],
  [2, 5, 8, 11, 14, 17],
  [3, 6, 9, 12, 15, 18]]
printGrid(5, 3) ➞ [
  [1, 6, 11],
  [2, 7, 12],
  [3, 8, 13],
  [4, 9, 14],
  [5, 10, 15]]
printGrid(4, 1) ➞ [
  [1],
  [2],
  [3],
  [4]]
'''


def printGrid(rows, cols):
    ' return grid of given order '
    try:
        logging.info('entering printGrid() function')
        if type(rows) == int and type(cols) == int:
            result = [[0 for col in range(cols)] for row in range(rows)]
            grid_items = list(range(1,rows*cols+1))
            idx = 0
            for col in range(cols):
                for row in range(rows):
                    result[row][col] = grid_items[idx]
                    idx += 1
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(printGrid(5, 3))
'''
4. Given a list of integers, return the smallest positive integer not present in the list.
Here is a representative example. Consider the list:
[-2, 6, 4, 5, 7, -1, 7, 1, 3, 6, 6, -2, 9, 10, 2, 2]
After reordering, the list becomes:
[-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 9, 10]
from which we see that the smallest missing positive integer is 8.
Examples
min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]) ➞ 8
# After sorting, list becomes [-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 9, 10]
# So the smallest missing positive integer is 8
min_miss_pos([5, 9, -2, 0, 1, 3, 9, 3, 8, 9]) ➞ 2
# After sorting, list becomes [-2, 0, 1, 3, 3, 5, 8, 9, 9, 9]
# So the smallest missing positive integer is 2
min_miss_pos([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9]) ➞ 1
# After sorting, list becomes [-1, 0, 2, 3, 4, 4, 4, 5, 6, 7, 9, 9, 10, 10]
# So the smallest missing positive integer is 1
'''


def min_miss_pos(num_list):
    ' returns the smallest positive number from given integer list '
    try:
        logging.info('entering min_miss_pos() function')
        if type(num_list) == list:
            max_in_list = max(num_list)
            min_positive = min([i for i in num_list if i > 0])
            for i in range(1,max_in_list+1):
                if i not in num_list:
                    return i
        else:
            raise TypeError('Input should be list of integers')
    except Exception as e:
        logging.error(e)


# print(min_miss_pos([5, 9, -2, 0, 1, 3, 9, 3, 8, 9]))
'''
5. Google is launching a network of autonomous pizza delivery drones and wants you to 
create a flexible rewards system (Pizza Points™) that can be tweaked in the future. The rules are simple: 
if a customer has made at least N orders of at least Y price, they get a FREE pizza!
Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. 
Return a list of customers that are eligible for a free pizza.
Examples
customers = {
  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]}
  pizza_points(customers, 5, 20) ➞ ["Spider-Man"]
  pizza_points(customers, 3, 10) ➞ ["Batman", "Spider-Man"]
  pizza_points(customers, 5, 100) ➞ []
'''


def pizza_points(customers, orders, min_order_price):
    ' returns list of customers who are eligible for free pizza based on given conditions '
    try:
        logging.info('entering pizza_points() function')
        if type(customers) == dict:
            result = []
            for kys in customers.keys():
                count = 0   # count of number of orders greater then minimum order price
                for order_price in customers[kys]:
                    if order_price >= min_order_price:
                        count += 1
                if count >= orders:
                    result.append(kys)
            return result
        else:
            raise TypeError('Input should be dictionary')
    except Exception as e:
        logging.error(e)


customers = {
  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]}
# print(pizza_points(customers,5,100))

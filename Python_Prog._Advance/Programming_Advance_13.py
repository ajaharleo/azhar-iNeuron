import logging
logging.basicConfig(filename='Prog13.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]
remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
'''


def remove_letters(items, statement):
    ' takes a list and string, remove list elements if it is in string '
    try:
        logging.info('entering remove_letters() function')
        if type(items) == list and type(statement) == str:
            temp = items.copy()
            st_list = list(statement)
            for i in items:
                if i in st_list:
                    temp.remove(i)
                    st_list.remove(i)
            return temp
        else:
            raise TypeError('Input should be list and string')
    except Exception as e:
        logging.error(e)


# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
'''
2. A block sequence in three dimensions. We can write a formula for this one:
Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.
Examples
blocks(1) ➞ 5
blocks(5) ➞ 39
blocks(2) ➞ 12
'''


def blocks(number):
    ' returns number of blocks in nth step '
    try:
        logging.info('entering blocks() function')
        if type(number) == int:
            items = [5,12]
            if number == 1 :
                return 5
            elif number == 2:
                return 12
            else:
                return blocks(number-1)+7+number-2
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(blocks(5))
'''
3. Create a function that subtracts one positive integer from another, without using any arithmetic operators such as -, %, /, +, etc.
Examples
my_sub(5, 9) ➞ 4
my_sub(10, 30) ➞ 20
my_sub(0, 0) ➞ 0
'''


def my_sub(num1,num2):
    ' docstring '
    try:
        logging.info('entering my_sub() function')
        if type(num1) == int and type(num2) == int:
            if num1 == 0:
                return num2
            elif num2 == 0:
                return num1
            else:
                if num1 >= num2:
                    return my_sub(num1 ^ num2, (~num1 & num2) << 1)
                else:
                    return my_sub(num1 ^ num2, (~num2 & num1) << 1)
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(my_sub(5,5))
'''
4. Create a function that takes a string containing money in dollars and pounds sterling (seperated by comma) and 
returns the sum of dollar bills only, as an integer.
For the input string:

   - Each amount is prefixed by the currency symbol: $ for dollars and £ for pounds.
   - Thousands are represented by the suffix k.
i.e. $4k = $4,000 and £40k = £40,000
Examples
add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70
add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170
add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200
'''


def add_bill(bill_str):
    ' return the sum of money in dollars only '
    try:
        logging.info('entering add_bill() function')
        if type(bill_str) == str:
            bill = bill_str.split(',')
            result = 0
            for i in bill:
                if 'd' in i:
                    if 'k' in i:
                        result += int(i[1:-1])*1000
                    else:
                        result += int(i[1:])
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(add_bill("p30,d2k,p60,d200,p360"))
'''
5. Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.
In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.
Examples
flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.
flip_list([[5], [6], [9]]) ➞ [5, 6, 9]
# Take a vertical list and flip it horizontal.
flip_list([]) ➞ []
'''


def flip_list(item):
    ' change horizontal array to vertical and vertical to horizontal '
    try:
        logging.info('entering flip_list() function')
        if type(item) == list:
            result = []
            for i in item:
                if type(i) == list:
                    result.append(i[0])
                else:
                    result.append([i])
            return result
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(flip_list([[5], [6], [9]]))
import logging
import math

logging.basicConfig(filename='Prog17.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function that transposes a 2D matrix.
Examples
transpose_matrix([
  [1, 1, 1],
  [2, 2, 2],
  [3, 3, 3]]) ➞ 
  [[1, 2, 3],
  [1, 2, 3],
  [1, 2, 3]]
transpose_matrix([
  [5, 5],
  [6, 7],
  [9, 1]]) ➞ [
  [5, 6, 9],
  [5, 7, 1]]
'''


def transpose_matrix(matrix):
    ' transpose a 2d matrix '
    try:
        logging.info('entering transpose_matrix() function')
        if type(matrix) == list:
            rows = len(matrix)
            cols = len(matrix[0])
            result = [[0 for i in range(rows)] for j in range(cols)]  # empty matrix of reverse order of original matrix
            for row in range(rows):
                for col in range(cols):
                    result[col][row] = matrix[row][col]
            return result
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(transpose_matrix([[5, 5],[6, 7],[9, 1]]))
'''
2. Create a function that determines whether a string is a valid hex code.
A hex code must begin with a pound key # and is exactly 6 characters in length. 
Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.
Examples
is_valid_hex_code("#CD5C5C") ➞ True
is_valid_hex_code("#EAECEE") ➞ True
is_valid_hex_code("#eaecee") ➞ True
is_valid_hex_code("#CD5C58C") ➞ False
# Length exceeds 6
is_valid_hex_code("#CD5C5Z") ➞ False
# Not all alphabetic characters in A-F
is_valid_hex_code("#CD5C&C") ➞ False
# Contains unacceptable character
is_valid_hex_code("CD5C5C") ➞ False
# Missing #
'''


def is_valid_hex_code(code):
    ' check if given code in str format is valid hex code or not '
    try:
        logging.info('entering is_valid_hex_code() function')
        if type(code) == str:
            if len(code) > 7:
                return False
            import re
            hex_pattern = re.compile(r'(#{1}[A-Fa-f0-9]{6})')
            if hex_pattern.match(code) is None:
                return False
            else:
                return True
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(is_valid_hex_code("CD5C5C"))
'''
3. Given a list of math equations (given as strings), return the percentage of correct answers as a string.
Round to the nearest whole number.
Examples
mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ➞ "75%"
mark_maths(["1-2=-2"]), "0%"
mark_maths(["2+3=5", "4+4=9", "3-1=2"]) ➞ "67%"
'''


def mark_maths(equations):
    ' counts how many string equations are correct '
    try:
        logging.info('entering mark_maths() function')
        if type(equations) == list:
            import re
            right = 0
            for equation in equations:
                nums = re.findall(r'[0-9]+',equation)
                operators = re.findall(r'[^0-9]',equation)
                if operators[0] == '+':
                    if int(nums[0]) + int(nums[1]) == int(nums[2]):
                        right += 1
                elif operators[0] == '-':
                    if int(nums[0]) - int(nums[1]) == int(nums[2]):
                        right += 1
                elif operators[0] == '*':
                    if int(nums[0]) * int(nums[1]) == int(nums[2]):
                        right += 1
                elif operators[0] == '/':
                    if int(nums[0]) // int(nums[1]) == int(nums[2]):
                        right += 1
            return str(math.ceil(right*100/len(equations)))+'%'
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(mark_maths(["2+3=5", "4+4=9", "3-1=2"]))
'''
4. There are two players, Alice and Bob, each with a 3-by-3 grid. A referee tells Alice to fill out one particular row 
in the grid (say the second row) by putting either a 1 or a 0 in each box, such that the sum of the numbers in 
that row is odd. The referee tells Bob to fill out one column in the grid (say the first column) by putting either a 1 
or a 0 in each box, such that the sum of the numbers in that column is even.
Alice and Bob win the game if Alice’s numbers give an odd sum, Bob’s give an even sum, and (most important) 
they’ve each written down the same number in the one square where their row and column intersect.
Examples
magic_square_game([2, "100"], [1, "101"]) ➞ False
magic_square_game([2, "001"], [1, "101"]) ➞ True
magic_square_game([3, "111"], [2, "011"]) ➞ True
magic_square_game([1, "010"], [3, "101"]) ➞ False
# Two lists, Alice [row, "her choice"], Bob [column, "his choice"]
'''


def magic_square_game(Alice, Bob):
    ' return True if win else False '
    try:
        logging.info('entering magic_square_game() function')
        if type(Alice) == list and type(Bob) == list:
            alice_matrix = [[0 for i in range(3)] for i in range(3)]
            bob_matrix = [[0 for i in range(3)] for i in range(3)]
            alice_total, bob_total = 0, 0
            for i in range(3):
                for j in Alice[1]:
                    alice_total += int(j)
                    alice_matrix[Alice[0]-1][i] = int(j)
                for k in Bob[1]:
                    bob_total += int(k)
                    bob_matrix[i][Bob[0]-1] = int(k)
            if alice_total % 2 != 0 and bob_total % 2 ==0 and alice_matrix[Alice[0]-1][Bob[0]-1] == bob_matrix[Alice[0]-1][Bob[0]-1]:
                return True
            else:
                return False
        else:
            raise TypeError('Input should be lists')
    except Exception as e:
        logging.error(e)


# print(magic_square_game([1, "010"], [3, "101"]))
'''
5. From point A, an object is moving towards point B at constant velocity va (in km/hr). 
From point B, another object is moving towards point A at constant velocity vb (in km/hr). 
Knowing this and the distance between point A and B (in km), 
write a function that returns how much time passes until both objects meet.
Format the output like this:
"2h 23min 34s"
Examples
lets_meet(100, 10, 30) ➞ "2h 30min 0s"
lets_meet(280, 70, 80) ➞ "1h 52min 0s"
lets_meet(90, 75, 65) ➞ "0h 38min 34s"
'''


def lets_meet(dist,sp1,sp2):
    ' tells the time when both object will meet '
    try:
        logging.info('entering lets_meet() function')
        if type(dist) == int and type(sp1) == int and type(sp2) == int:
        #as we know time required will be distance / relative velocity. here relative velocity will be sp1+sp2
            hrs = dist // (sp1+sp2)
            mins = (dist%(sp1+sp2))*60 // (sp1+sp2)
            seconds = ((dist%(sp1+sp2))*60 % (sp1+sp2))*60 // (sp1+sp2)
            return f'{hrs}h {mins}min {seconds}s'
        else:
            raise TypeError('Input should be integers')
    except Exception as e:
        logging.error(e)


# print(lets_meet(90,75,65))

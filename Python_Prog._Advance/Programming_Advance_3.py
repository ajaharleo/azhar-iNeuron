import logging
logging.basicConfig(filename='Prog3.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a function to perform basic arithmetic operations that includes addition, subtraction, 
multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 
2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.
For example:
"15 // 0"  ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0
arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
'''


def arithmetic_operation(str_inp):
    ' do mathematical operation given in str format '
    try:
        logging.info('entering arithmetic_operation() function')
        if type(str_inp) == str:
            values = str_inp.split(' ')
            if '+' in values:
                return int(values[0])+int(values[2])
            elif '-' in values:
                return int(values[0])-int(values[2])
            if '*' in values:
                return int(values[0])*int(values[2])
            if '//' in values:
                if int(values[2]) == 0:
                    return -1
                else:
                    return int(values[0])/int(values[2])
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(arithmetic_operation("12 // 0"))
'''
2. Write a function that takes the coordinates of three points in the form of a 2d array and 
returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
Examples
perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08
perimeter( [ [0, 0], [0, 1], [1, 0] ] ) ➞ 3.42
perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) ➞ 68.28
'''


def perimeter(coordinates):
    ' takes cordinates of three points in a list of lists and return perimeter of triangle '
    try:
        logging.info('entering perimeter() function')
        if type(coordinates) == list or type(coordinates) == tuple:
            dist1 = ((coordinates[0][0]-coordinates[1][0])**2+(coordinates[0][1]-coordinates[1][1])**2)**0.5
            dist2 = ((coordinates[0][0] - coordinates[2][0]) ** 2 + (coordinates[0][1] - coordinates[2][1]) ** 2)**0.5
            dist3 = ((coordinates[2][0] - coordinates[1][0]) ** 2 + (coordinates[2][1] - coordinates[1][1]) ** 2)**0.5
            peri = dist1+dist2+dist3
            return round(peri,2)
        else:
            raise TypeError('Input should be list or tuple')
    except Exception as e:
        logging.error(e)


# print(perimeter([ [15, 7], [5, 22], [11, 1] ]))
'''
3. A city skyline can be represented as a 2-D list with 1s representing buildings. 
In the example below, the height of the tallest building is 4 (second-most right column).
[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
Examples
tallest_skyscraper([[0, 0, 0, 0],[0, 1, 0, 0],[0, 1, 1, 0],[1, 1, 1, 1]]) ➞ 3
tallest_skyscraper([[0, 1, 0, 0],[0, 1, 0, 0],[0, 1, 1, 0],[1, 1, 1, 1]]) ➞ 4
tallest_skyscraper([[0, 0, 0, 0],[0, 0, 0, 0],[1, 1, 1, 0],[1, 1, 1, 1]]) ➞ 2
'''


def tallest_skyscraper(skyline):
    ' tells the highest height '
    try:
        logging.info('entering tallest_skyscraper() function')
        if type(skyline) == list:
            height = [0]*len(skyline[0])
            total = 0
            for i in range(len(skyline[0])):
                for j in range(len(skyline)):
                    total += skyline[j][i]
                height[i] = total
                total = 0
            return max(height)
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


'''print(tallest_skyscraper([[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]))'''
'''
4. A financial institution provides professional services to banks and 
claims charges from the customers based on the number of man-days provided. 
Internally, it has set a scheme to motivate and reward staff to meet and exceed targeted billable utilization and
 revenues by paying a bonus for each day claimed from customers in excess of a threshold target.
This quarterly scheme is calculated with a threshold target of 32 days per quarter, 
and the incentive payment for each billable day in excess of such threshold target is shown as follows:
Days	                             Bonus
0 to 32 days	                   Zero
33 to 40 days	         SGD$325 per billable day
41 to 48 days	         SGD$550 per billable day
Greater than 48 days      SGD$600 per billable day
Please note that incentive payment is calculated progressively. As an example, 
if an employee reached total billable days of 45 in a quarter, his/her incentive payment is computed as follows:
32*0 + 8*325 + 5*550 = 5350
Write a function to read the billable days of an employee and return the bonus he/she has obtained in that quarter.
Examples
bonus(15) ➞ 0
bonus(37) ➞ 1625
bonus(50) ➞ 8200
'''


def bonus(billable_days):
    ' return the bonus for the given billable days '
    try:
        logging.info('entering bonus() function')
        total = 0
        if type(billable_days) == int:
            if billable_days <= 32:
                return total
            else:
                if billable_days <=40:
                    total = (billable_days - 32)*325
                    return total
                else:
                    total += 8 * 325
                    if billable_days <= 48:
                        total += (billable_days-40)*550
                    else:
                        total += 8*550 + (billable_days-48)*600
            return total
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(bonus(50))
'''
5. A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32
is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium(544) ➞ False
is_disarium(518) ➞ True
is_disarium(466) ➞ False
is_disarium(8) ➞ True
'''


def is_disarium(number):
    ' check whether a number is disarium or not  '
    try:
        logging.info('entering is_disarium() function')
        if type(number) == int or type(number):
            num_str = str(number)
            total = 0
            for i in range(len(num_str)):
                total += int(num_str[i])**(i+1)
            if total == number:
                return True
            else:
                return False
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(is_disarium(135))

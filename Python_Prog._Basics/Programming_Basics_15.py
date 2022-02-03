import logging
logging.basicConfig(filename='Prog15.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form 
while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
'''

def multipleOf5n7(n):
    ''' generate the numbers divisible by both 5 and 7 within range '''
    try:
        logging.info('entering multiple function')
        if type(n)==int:
            for i in range(n):
                if i%5 == 0 and i%7 ==0:
                    yield i
        else:
            raise TypeError('Number should be input')
    except Exception as e:
        logging.error(e)


def question1(n):
    ''' return numbers divisible by both 5 and 7 '''
    try:
        logging.info('entering question1 function')
        if type(n)==int:
            result_list = list(multipleOf5n7(n))
            result = ''
            for i in result_list:
                result += str(i) + ','
            return result[:-1]
        else:
            raise TypeError('Number should be input')
    except Exception as e:
        logging.error(e)


#print(question1(100))
'''
Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
'''

def oddEven(n):
    ''' generate the even numbers within range '''
    try:
        logging.info('entering oddEven() function')
        if type(n) == int:
            for i in range(n+1):
                if i % 2 == 0:
                    yield i
        else:
            raise TypeError('Number should be input')
    except Exception as e:
        logging.error(e)


def question2(n):
    ''' return even numbers within range '''
    try:
        logging.info('entering question2 function')
        if type(n)==int:
            result_list = list(oddEven(n))
            result = ''
            for i in result_list:
                result += str(i) + ','
            return result[:-1]
        else:
            raise TypeError('Number should be input')
    except Exception as e:
        logging.error(e)


#print(question2(10))

'''
Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
'''


def fibonacci(n):
    ''' tell nth fibonacci number, n should be integer '''
    try:
        logging.info('creating fibonacci series with fibonacci() function')
        if type(n)==int:
            if n ==0:
                return 0
            elif n==1:
                return 1
            else:
                return fibonacci(n-1)+fibonacci(n-2)
        else:
            raise TypeError("Input should be an iteger")
    except Exception as e:
        logging.error(e)


def question3(n):
    ''' return fibonacci numbers within range '''
    try:
        logging.info('entering question3 function')
        if type(n)==int:
            result_list = [fibonacci(i) for i in range(n+1)]
            result = ''
            for i in result_list:
                result += str(i) + ','
            return result[:-1]
        else:
            raise TypeError('Number should be input')
    except Exception as e:
        logging.error(e)


#print(question3(7))


'''
Question 4:
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
'''

def question4(email):
    ''' return user name from the give email address'''
    try:
        if type(email) == str:
            if '@' not in email:
                raise Exception('Invalid email address')
            details = email.split('@')
            return details[0]
        else:
            raise TypeError("Input should be of string type")
    except Exception as e:
        logging.error(e)


#print(question4('john@google.com'))

'''
Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
'''

class Shape:
    def __init__(self):
        self.areas = 0

    def area(self):
        return self.areas


class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        self.areas = self.length **2
        return self.areas


# a = Shape()
# print(a.area())
#
# b = Square(6)
# print(b.area())
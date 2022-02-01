import logging

logging.basicConfig(filename='Prog13.log', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question 1: Write a program that calculates and prints the value according to the given formula: 
Q = Square root of [(2 * C * D)/H] 
Following are the fixed values of C and H: 
C is 50. H is 30. 
'''

def sqrt(D,C=50,H=30):
    '''retrun the value according to the formula Q = Square root of [(2 * C * D)/H] '''
    try:
        if type(C)==int and type(D)==int and type(H)==int:
            logging.info('calulating Q')
            Q =((2 * C * D)/H)**0.5
            return Q
        else:
            raise TypeError('All input should be integers')
    except Exception as e:
        logging.error(e)

'''
Question 2: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
Note: i=0,1.., X-1; j=0,1,¡Y-1
'''

def array_list(rows,cols):
    '''returns a list with given rows and columns'''
    try:
        if type(rows)==int and type(cols)==int:
            logging.info('returning array from array_list() function')
            result = [[0 for col in range(cols)] for row in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    result[row][col] = row*col
            return result
        else:
            raise TypeError('Input should be integers')
    except Exception as e:
        logging.error(e)

'''
Question 3: Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically. 
'''
def word_sorting(*args):
    '''take input as strings then return sorted string'''
    try:
        words = list(args)
        words.sort()
        result = ''
        logging.info('sorting words')
        for i in words:
            if type(i)==str:
                result = result + i + ','
            else:
                raise TypeError('All inputs should be string type')
        return result[:-1]
    except Exception as e:
        logging.error(e)

'''
Question 4: Write a program that accepts a sequence of whitespace separated words as input and 
prints the words after removing all duplicate words and sorting them alphanumerically. 
'''
def words_sequence(statement):
    '''take a statement in string format and return all unique words inside statement in a string'''
    try:
        logging.info('words_sequence() function')
        if type(statement)==str:
            words = statement.split()
            words = list(set(words))
            words.sort()
            result = ''
            for i in words:
                result = result + i + ','
        else:
            raise TypeError("Please give input in string format")
        return result[:-1]
    except exception as e:
        logging.error(e)

'''
Question 5: Write a program that accepts a sentence and calculate the number of letters and digits
'''
def letter_digit(statement):
    '''return no of letters and digits present in the given statement'''
    try:
        if type(statement)==str:
            letters = 0
            digits = 0
            for i in statement:
                if i.isalpha():
                    letters+=1
                elif i.isnumeric():
                    digits += 1
        else:
            raise TypeError("Please give input in string format")
        return (letters,digits)
    except Exception as e:
        logging.error(e)

'''
Question 6: 
A website requires the users to input username and password to register. Write a program to check the validity of password input by users. 
Following are the criteria for checking the password: 
1. At least 1 letter between [a-z] 
2. At least 1 number between [0-9] 
3. At least 1 letter between [A-Z] 
4. At least 1 character from [$#@] 
5. Minimum length of transaction password: 6 
6. Maximum length of transaction password: 12 
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma. 
'''

def password_validator(password):
    '''take password as input and return True if satisfy all conditions else return False'''
    password_valid = True
    loop = True
    import re
    logging.info('Validating Password')
    try:
        if type(password)==str:
            while loop:
                if not re.search('[a-z]',password):
                    password_valid = False
                    logging.debug('Password do not have any lower case letter')
                    loop = False
                elif not re.search('[0-9]',password):
                    password_valid = False
                    logging.debug('Password do not have any digit')
                    loop = False
                elif not re.search('[A-Z]',password):
                    password_valid = False
                    logging.debug('Password do not have any upper case letter')
                    loop = False
                elif not re.search('[$#@]',password):
                    password_valid = False
                    logging.debug('Password do not have any required special character')
                    loop = False
                elif len(password)<6:
                    password_valid = False
                    logging.debug('Password length is less than 6')
                    loop = False
                elif len(password)>12:
                    password_valid = False
                    logging.debug('Password length is grater then 12')
                else:
                    password_valid = True
                    logging.info('Password is valid')
                    loop = False
        else:
            raise TypeError('Password should be string type')
        return password_valid
    except Exception as e:
        logging.error(e)

def password_filter(*args):
    '''take bunch of paasswords and filter out invaild passwords. return valid passwords only'''
    valid = ''
    try:
        logging.info("entering password_filter() function")
        for i in args:
            if type(i)==str:
                if password_validator(i):
                    valid = valid + i + ','
            else:
                raise TypeError('Password should be string')
        return valid[:-1]
    except Exception as e:
        logging.error(e)

#print(password_filter('09as5ASS','ABd1234@1','a F1#','2w3E*','2We3345 '))


logging.shutdown()
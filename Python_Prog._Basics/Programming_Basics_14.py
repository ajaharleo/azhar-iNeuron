import logging
import zlib

logging.basicConfig(filename='Prog14.log', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

'''
Question 1:
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.
'''

class Multiple7:
    ''' class which iterates from start to end and give multiple of 7'''
    logging.info('Creating instance of class Multiple7')
    def __init__(self,start,end):
        if type(start)==int and type(end)==int:
            self.start = start
            self.end = end
            self.index = start
        else:
            logging.error('invalid inputs')
            raise TypeError('attributes should be integers')

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        result = self.index
        self.index = self.index +7
        return result


# a = Multiple7(0,89)
# for i in a:
#     print(i)

'''
Question 2:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

def word_frequency(statement):
    ''' take a statement input as string format and return frequency of words after sorting'''
    try:
        if type(statement)==str:
            words = statement.split()
            unique_words = list(set(words))
            unique_words.sort()
            result = []
            for i in unique_words:
                result.append((i,words.count(i)))
            return result
        else:
            raise TypeError("Give only string Input")
    except Exception as e:
        logging.error(e)

#print(word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'))

'''
Question 3:
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
'''


class Person:
    def __init__(self, gender):
        self.gender = gender

    def getgender(self):
        return self.gender


class Male(Person):
    def __init__(self):
        self.gender = 'Male'

    def getgender(self):
        return self.gender


class Female(Person):
    def __init__(self):
        self.gender = 'Female'

    def getgender(self):
        return self.gender

# p = Female()
# print(p.getgender())


'''
Question 4:
Please write a program to generate all sentences where subject is in ["I", "You"] and 
verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''
def generate_sentence(subject, verb, object):
    """take inputs in multiple lists then generate sentences from the combination"""
    try:
        logging.info('generate_sentence() function initiated')
        result = []
        if (type(subject) == list or type(subject) == tuple) and (type(verb) == list or type(verb) == tuple) and (type(object) == list or type(object) == tuple):
            for i in subject:
                for j in verb:
                    for k in object:
                        sent = i + ' ' + j + ' ' + k + '.'
                        result.append(sent)
                        sent = ''
            return result
        else:
            raise TypeError('Inputs should be in list or tuple')
    except Exception as e:
        logging.error(e)

#print(generate_sentence(["I", "You"], ["Play", "Love"], ["Hockey","Football"]))

'''
Question 5:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''


def compress(string):
    ''' compress string to utf-8'''
    try:
        logging.info('compressing statement')
        if type(string) == str:
            byte_string = bytes(string, 'utf-8')
            return zlib.compress(byte_string)
        else:
            raise TypeError('Give inputs only in string format')
    except Exception as e:
        logging.error(e)


# a = compress("hello world!hello world!hello world!hello world!")
# print(a)


def decompress(byte_string):
    ''' decompress give compressed byte string'''
    try:
        logging.info('Decompressing statement')
        if type(byte_string) == bytes:
            return zlib.decompress(byte_string)
        else:
            raise TypeError('Give inputs only in byte string format')
    except Exception as e:
        logging.error(e)


#print(decompress(a))


'''
Question 6:
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
'''

def binary_search(collection,item):
    ''' binary search item in a list'''
    try:
        logging.info('Binary searching item it the collection')
        if type(collection==list):
            collection.sort()
            import bisect
            return bisect.bisect_left(collection, item)
        else:
            raise TypeError('collection should be in list format')
    except Exception as e:
        logging.error(e)


#print(binary_search(['hey','xavier','batman','wolverine','captain','jocker'],'wolverine'))
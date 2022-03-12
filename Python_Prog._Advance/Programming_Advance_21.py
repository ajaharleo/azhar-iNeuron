import logging
logging.basicConfig(filename='Prog21.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Given a sentence, return the number of words which have the same first and last letter.
Examples
count_same_ends("Pop! goes the balloon") ➞ 1
count_same_ends("And the crowd goes wild!") ➞ 0
count_same_ends("No I am not in a gang.") ➞ 1
'''


def count_same_ends(sentence):
    ' returns number of words in string with same first and last letter '
    try:
        logging.info('entering count_same_ends() function')
        if type(sentence) == str:
            import re
            sentence = re.sub(r'[^a-zA-Z0-9\s]','',sentence)
            words = sentence.split(' ')
            count = 0
            for i in words:
                if len(i) >1 and i[0].lower() == i[-1].lower():
                    count += 1
            return count
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(count_same_ends("And the crowd goes wild!"))
'''
2. The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter 
in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
Create a function that takes a string and applies the Atbash cipher to it.
Examples
atbash("apple") ➞ "zkkov"
atbash("Hello world!") ➞ "Svool dliow!"
atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
'''


def atbash(sentence):
    ' returns encrypted string as replace letter with its mirror letter '
    try:
        logging.info('entering atbash() function')
        if type(sentence) == str:
            result = ''
            for i in sentence:
                if 65 <= ord(i) <= 90:
                    result += chr(90 - (ord(i) - 65))
                elif 97 <= ord(i) <= 122:
                    result += chr(122 - (ord(i) - 97))
                else:
                    result += i
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(atbash("apple"))
'''
3. Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords.
Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.
Examples
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
'''


class Employee:
    def __init__(self, full_name, **kwargs):
        logging.info('constructing Employee class object')
        self.full_name = full_name
        self.__dict__.update(kwargs)


giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
#print(giancarlo.height)

'''
4. Create a function that determines whether each seat can "see" the front-stage. 
A number can "see" the front-stage if it is strictly greater than the number before it.
Everyone can see the front-stage in the example below:
# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]
# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
Not everyone can see the front-stage in the example below:
# FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]
# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, and False if even a single number cannot.
Examples
can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]) ➞ True
can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]]) ➞ True
can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]]) ➞ False
can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]]) ➞ False
# Number must be strictly smaller than 
# the number directly behind it.
'''


def can_see_stage(seats):
    ' return True if height of seats is correct else return False '
    try:
        logging.info('entering can_see_stage() function')
        if type(seats) == list:
            rows, cols = len(seats), len(seats[0])
            for col in range(cols-1):
                for row in range(rows):
                    if seats[col][row] >= seats[col+1][row]:
                        return False
            return True
        else:
            raise TypeError('Input should be a 2-d list')
    except Exception as e:
        logging.error(e)


# print(can_see_stage([[0, 0, 0],[1, 1, 1],[2, 2, 2]]))
'''
5. Create a Pizza class with the attributes order_number and ingredients (which is given as a list). 
Only the ingredients will be given as input.
You should also make it so that its possible to choose a ready made pizza flavour rather 
than typing out the ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.
Name	                    Ingredients
hawaiian	          ham, pineapple
meat_festival	beef, meatball, bacon
garden_feast	spinach, olives, mushroom
Examples
p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]
p2.ingredients ➞ ["spinach", "olives", "mushroom"]
p1.order_number ➞ 1
p2.order_number ➞ 2
'''


class Pizza:
    order_no = 0

    def __init__(self,ingredients):
        Pizza.order_no += 1
        self.order_number = Pizza.order_no
        self.ingredients = ingredients
        if type(self.ingredients) == tuple:
            self.ingredients = list(self.ingredients)
        elif type(self.ingredients) != list:
            raise TypeError('Ingredients should be in a list or tuple')

    @staticmethod
    def hawaiian():
        logging.info('Creating Pizza object of hawaiian flavour')
        return Pizza(['ham','pineapple'])

    @staticmethod
    def meat_festival():
        logging.info('Creating Pizza object of meat_festival flavour')
        return Pizza(['beef','meatball','bacon'])

    @staticmethod
    def garden_feast():
        logging.info('Creating Pizza object of garden_feast flavour')
        return Pizza(['spinach','olives','mushroom'])


p1 = Pizza(["bacon", "parmesan", "ham"])
print(p1.ingredients)
print(p1.order_number)
p2 = Pizza(["spinach", "olives", "mushroom"])
print(p2.order_number)
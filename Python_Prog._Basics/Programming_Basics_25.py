import  logging
logging.basicConfig(filename='Prog25.log', level=logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')
'''
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.
'''


def equal(a, b, c):
    ' takes three integers and tell how many are equal '
    try:
        logging.info('entering equal function')
        uniq = list(set((a,b,c)))
        if len(uniq) == 1:
            return 3
        elif len(uniq) == 2:
            return 2
        elif len(uniq) == 3:
            return 0
    except Exception as e:
        logging.error(e)


# print(equal(3,3,3))
'''
Question2
Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]
dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
Notes
Return the elements in the list in alphabetical order.
'''


def dict_to_list(str_dct):
    ' takes a dictionary and return key values in pairs in a list '
    try:
        logging.info('entering dict_to_list function')
        if type(str_dct) == dict:
            order = sorted(str_dct)
            result = []
            for i in order:
                result.append((i,str_dct[i]))
            return result
        else:
            raise ValueError('Input should be a dictionary')
    except Exception as e:
        logging.error(e)


# print(dict_to_list({"likes": 2,"dislikes": 3,"followers": 10}))
'''
Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes
All of the letters in the input list will always be lowercase.
'''


def mapping(str_list):
    ' takes list of alphabets return diction lower case as key and upper case as value '
    try:
        logging.info('entering mapping function')
        if type(str_list) == list:
            result = {}
            for i in str_list:
                result[i] = i.upper()
            return result
        else:
            raise ValueError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(mapping(["p", "s"]))
'''
Question4
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.
'''


def vow_replace(str_input,special):
    ' take two string inputs and return first string with all vowels replaced by special letter '
    try:
        logging.info('entering vow_replace function')
        if type(str_input) == str and type(special) == str:
            result = ''
            for i in str_input:
                if i in 'aeiou':
                    result += special
                else:
                    result += i
            return result
        else:
            raise ValueError('Both inputs should be string')
    except Exception as e:
        logging.error(e)


# print(vow_replace("cheese casserole", "o"))
'''
Question5
Create a function that takes a string as input and capitalizes a letter 
if its ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
'''

def ascii_capitalize(str_inp):
    ' capitalize according to ASCII value of character '
    try:
        logging.info('entering ascii_capitalize function')
        if type(str_inp) == str:
            result =''
            for  i in str_inp:
                if ord(i)%2 == 0:
                    result += i.upper()
                elif ord(i)%2 != 0:
                    result += i.lower()
                else:
                    result.append(i)
            return  result
        else:
            raise ValueError('Input should be string')
    except Exception as e :
        logging.error(e)


# print(ascii_capitalize("to be or not to be!"))
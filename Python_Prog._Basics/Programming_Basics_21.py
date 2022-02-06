import logging
logging.basicConfig(filename='Prog21.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
Question1
Write a function that takes a list and a number as arguments. 
Add the number to the end of the list, then remove the first element of the list. 
The function should then return the updated list.
Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
next_in_line([], 6) ➞ "No list has been selected"
'''
def next_in_line(list_in,new):
    ' first item is a list and 2nd is a new argument to be added at the end of list then remove first element and return list'
    try:
        logging.info('entering next_in_line function')
        if type(list_in) == list:
            list_in.append(new)
            list_in.remove(list_in[0])
            if len(list_in) == 0:
                return 'No list has been selected'
            else:
                return list_in
        else:
            raise TypeError("Please give input in a list")
    except Exception as e:
        logging.error(e)


# print(next_in_line([], 1))
'''
Question2
Create the function that takes a list of dictionaries and returns the sum of people's budgets.
Examples
get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]) ➞ 65700
get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]) ➞ 62600
'''


def get_budgets(list_dict):
    ' takes list of dictionaries and return sum of budget mentioned in dictionary'
    try:
        logging.info('Entering get_budget function')
        if type(list_dict) == list:
            result = 0
            for i in list_dict:
                if type(i) == dict:
                    result+=i['budget']
                else:
                    raise TypeError("Data in the list should be in dictionary")
            return result
        else:
            raise TypeError("input should be in a list")
    except Exception as e:
        logging.error(e)


# print(get_budgets([{ "name": "John",  "age": 21, "budget": 29000 },
#  { "name": "Steve",  "age": 32, "budget": 32000 },{ "name": "Martin",  "age": 16, "budget": 1600 }]))
'''
Question3
Create a function that takes a string and returns a string with its letters in alphabetical order.
Examples
alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("edabit") ➞ "abdeit"
alphabet_soup("hacker") ➞ "acehkr"
alphabet_soup("geek") ➞ "eegk"
alphabet_soup("javascript") ➞ "aacijprstv"
'''


def alphabet_soup(str_inp):
    ' take a string and return the string as letters in alphabetical error'
    try:
        logging.info('enering alphabet_soup')
        if type(str_inp) == str:
            st_list = sorted(str_inp)
            return ''.join(st_list)
        else:
            raise TypeError('give string input')
    except Exception as e:
        logging.error(e)


# print(alphabet_soup("hello"))
'''
Question4
Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly. 
What will be the value of your investment at the end of the 10 year period?
Create a function that accepts the principal p, the term in years t, the interest rate r, 
and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.
For the example above:
compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
Note that the interest rate is given as a decimal and n=12 because with monthly compounding there are 12 periods per year. 
Compounding can also be done annually, quarterly, weekly, or daily.
Examples
compound_interest(100, 1, 0.05, 1) ➞ 105.0
compound_interest(3500, 15, 0.1, 4) ➞ 15399.26
compound_interest(100000, 20, 0.15, 365) ➞ 2007316.26
'''


def compound_interest(invest,time,rate,compounds):
    ''' invest in $, time in years, rate annually and compounds per year
    returns amount at the end of given time'''
    try:
        logging.info('Entering compound_interest function')
        rate = rate/compounds
        final  = invest*(1+rate)**(time*compounds)
        return round(final,2)
    except Exception as e:
        logging.error(e)


# print(compound_interest(3500, 15, 0.1, 4))
'''
Question5
Write a function that takes a list of elements and returns only the integers.
Examples
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]
return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]
return_only_integer(["String",  True,  3.3,  1]) ➞ [1]
'''


def return_only_integer(list_inp):
    ' take a list of string and integers then return list with integers only '
    try:
        logging.info('Filtering items with return_only_integer() function')
        if type(list_inp) == list:
            result = []
            for i in list_inp:
                if type(i) == int:
                    result.append(i)
            return result
        else:
            raise TypeError('Please give input as a list')
    except Exception as e:
        logging.error(e)


# print(return_only_integer([9, 2, "space", "car", "lion", 16]))

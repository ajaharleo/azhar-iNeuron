import logging
logging.basicConfig(filename='Prog16.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Rondo Form is a type of musical structure, in which there is a recurring theme/refrain, notated as A. 
Here are the rules for valid rondo forms:
   - Rondo forms always start and end with an A section.
   - In between the A sections, there should be contrasting sections notated as B, then C, then D, etc... No letter should be skipped.
   - There shouldn't be any repeats in the sequence (such as ABBACCA).
Create a function which validates whether a given string is a valid Rondo Form.
Examples
valid_rondo("ABACADAEAFAGAHAIAJA") ➞ True
valid_rondo("ABA") ➞ True
valid_rondo("ABBACCA") ➞ False
valid_rondo("ACAC") ➞ False
valid_rondo("A") ➞ False
'''


def valid_rondo(music):
    ' check music string is rondo forms or not '
    try:
        logging.info('entering valid_rondo() function')
        if type(music) == str:
            pass
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


'''
2. Create a function that returns the whole of the first sentence which contains a specific word. 
Include the full stop at the end of the sentence.
Examples
txt = "I have a cat. I have a mat. Things are going swell."
sentence_searcher(txt, "have") ➞ "I have a cat."
sentence_searcher(txt, "MAT") ➞ "I have a mat."
sentence_searcher(txt, "things") ➞ "Things are going swell."
sentence_searcher(txt, "flat") ➞ ""
'''


def sentence_searcher(sentences, word):
    ' return only sentence which have the given word '
    try:
        logging.info('entering sentence_searcher() function')
        if type(sentences) == str and type(word) == str:
            sentences = sentences.split('. ')
            for i in sentences:
                if word in i:
                    return i+'.'
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(sentence_searcher("I have a cat. I have a mat. Things are going swell.",'have'))
'''
3. Given a number, find the "round "of each digit of the number. 
An integer is called "round" if all its digits except the leftmost (most significant) are equal to zero.
    - Round numbers: 4000, 1, 9, 800, 90
    - Not round numbers: 110, 707, 222, 1001
Create a function that takes a number and returns the "round" of each digit (except if the digit is zero) as a string. 
Check out the following examples for more clarification.
Examples
sum_round(101) ➞ "1 100"
sum_round(1234) ➞ "4 30 200 1000"
sum_round(54210) ➞ "10 200 4000 50000"
'''


def sum_round(number):
    ' return round of each digit of integer '
    try:
        logging.info('entering sum_round() function')
        if type(number) == int:
            digit_str = str(number)[::-1]
            result = ''
            for i in range(len(digit_str)):
                if digit_str[i] != '0':
                    result += digit_str[i] + '0' * i + ' '
            return result[:-1]
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(sum_round(54210))
'''
4. Your task, is to create N x N multiplication table, of size n provided in parameter.
For example, when n is 5, the multiplication table is:
   - 1, 2, 3, 4, 5
   - 2, 4, 6, 8, 10
   - 3, 6, 9, 12, 15
   - 4, 8, 12, 16, 20
   - 5, 10, 15, 20, 25
This example will result in:
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
Examples
multiplication_table(1) ➞ [[1]]
multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
'''


def multiplication_table(number):
    ' create multiplication table of given number '
    try:
        logging.info('entering multiplication_table() function')
        if type(number) == int:
            result = [[0 for col in range(number)] for row in range(number)]
            for row in range(1,number+1):
                for column in range(1,number+1):
                    result[row-1][column-1] = row * column
            return result
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(multiplication_table(3))
'''
5. Create a function that returns True if two lines rhyme and False otherwise. 
For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.
Examples
does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True
does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.
does_rhyme("You are off to the races", "a splendid day.") ➞ False
does_rhyme("and frequently do?", "you gotta move.") ➞ False
'''


def does_rhyme(line1, line2):
    ' return True if two lines rhyme else False '
    try:
        logging.info('entering does_rhyme() function')
        if type(line2) == str and type(line1) == str:
            first = line1.split()
            second = line2.split()
            import re
            first_vowel = re.findall(r'[aeiou]',first[-1].lower())  # getting vowels in last item of first sentence
            second_vowel = re.findall(r'[aeiou]', second[-1].lower()) # vowels in last element of second sentence
            if first_vowel[-1] == second_vowel[-1]:
                return True
            else:
                return False
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(does_rhyme("Sam I am!", "Green eggs and HAM."))

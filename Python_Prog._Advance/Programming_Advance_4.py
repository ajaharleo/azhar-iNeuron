import logging
logging.basicConfig(filename='Prog4.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


'''
1. In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1:
The beginning of the sequence is this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
The function fastFib(num) returns the fibonacci number Fn, of the given num as an argument.
Examples
fib_fast(5) ➞ 5
fib_fast(10) ➞ 55
fib_fast(20) ➞ 6765
fib_fast(50) ➞ 12586269025
'''


def fib_fast(number):
    try:
        logging.info('entering fib_fast number')
        if type(number)==int :
            fibonacci = [0,1]
            if number <1:
                return fibonacci[0]
            elif number==1:
                return fibonacci[1]
            else:
                for i in range(2, number + 1):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
                return fibonacci[number]
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(fib_fast(50))
'''
2. Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.
Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
'''


def convert_to_hex(statement):
    try:
        logging.info('entering convert_to_hex number')
        if type(statement) == str :
            result = ''
            for i in statement:
                result += hex(ord(i))[-2:] + ' '
            return result[:-1]
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(convert_to_hex("Marty Poppinson"))
'''
3. Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, 
I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.
Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
uncensor("abcd", "") ➞ "abcd"
uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
'''


def uncensor(censored,vowels):
    try:
        logging.info('entering uncensor funciton')
        if type(censored) == str and type(vowels) == str:
            count = 0
            for i in range(len(censored)):
                if censored[i] == '*':
                    censored = censored[:i] + vowels[count] + censored[i+1:]
                    count += 1
            return censored
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(uncensor("*PP*RC*S*", "UEAE"))
'''
4. Write a function that takes an IP address and returns the domain name using PTR DNS records.
Example
get_domain("8.8.8.8") ➞ "dns.google"
get_domain("8.8.4.4") ➞ "dns.google"
'''


def get_domain(IP):
    try:
        logging.info('entering get_domain number')
        if type(IP) == str:
            import socket
            return socket.gethostbyaddr("8.8.8.8")[0]
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(get_domain('8.8.4.4'))
'''
5. Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:
Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288
fact_of_fact(5) ➞ 34560
fact_of_fact(6) ➞ 24883200
'''


def factorial(number):
    ' return factorial of given number '
    if number <0:
        raise ValueError('Value should be positive integer')
    else:
        result = 1
        for i in range(1,number+1):
            result *= i
        return result


def fact_of_fact(number):
    try:
        logging.info('entering fact_of_fact number')
        if type(number) == int:
            result = 1
            for i in range(1,number+1):
                result *= factorial(i)
            return result
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(fact_of_fact(5))

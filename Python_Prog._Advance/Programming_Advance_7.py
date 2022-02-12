import logging
logging.basicConfig(filename='Prog7.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Write a function that counts how many concentric layers a rug.
Examples
count_layers(["AAAA","ABBA","AAAA"]) ➞ 2
count_layers(["AAAAAAAAA","ABBBBBBBA",
  "ABBAAABBA","ABBBBBBBA","AAAAAAAAA"]) ➞ 3
count_layers(["AAAAAAAAAAA","AABBBBBBBAA","AABCCCCCBAA",
"AABCAAACBAA","AABCADACBAA","AABCAAACBAA","AABCCCCCBAA",
"AABBBBBBBAA","AAAAAAAAAAA"]) ➞ 5
'''


def count_layers(inp):
    ' return number of concentric layers '
    try:
        logging.info('entering count_layers() function')
        if type(inp) == list:
            if len(inp)%2 == 0:
                if inp == inp[::-1]:
                    return len(inp)//2
            else:
                count = 0
                mid = (len(inp)//2) + 1
                if inp[mid] == inp[mid][::-1]:
                    count +=1
                    if inp == inp[::-1]:
                        count += mid -1
                return count
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


'''print(count_layers(["AAAAAAAAAAA","AABBBBBBBAA","AABCCCCCBAA",
"AABCAAACBAA","AABCADACBAA","AABCAAACBAA","AABCCCCCBAA",
"AABBBBBBBAA","AAAAAAAAAAA"]))'''

'''
2. There are many different styles of music and many albums exhibit multiple styles. 
Create a function that takes a list of musical styles from albums and returns how many styles are unique.
Examples
unique_styles(["Dub,Dancehall","Industrial,Heavy Metal",
  "Techno,Dubstep","Synth-pop,Euro-Disco","Industrial,Techno,Minimal"]) ➞ 9
unique_styles(["Soul","House,Folk",
  "Trance,Downtempo,Big Beat,House","Deep House","Soul"]) ➞ 7
'''


def unique_styles(music):
    ' tells unique elements from the given music list '
    try:
        logging.info('entering unique_styles() function')
        if type(music) == list:
            unique = []
            for i in music:
                temp = i.split(',')
                for j in temp:
                    unique.append(j)
            unique = list(set(unique))
            return len(unique)
        else:
            raise TypeError('Input should be list of strings')
    except Exception as e:
        logging.error(e)


# print(unique_styles(["Soul","House,Folk","Trance,Downtempo,Big Beat,House","Deep House","Soul"]))
'''
3. Create a function that finds a target number in a list of prime numbers. 
Implement a binary search algorithm in your function. 
The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".
Examples
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
is_prime(primes, 3) ➞ "yes"
is_prime(primes, 4) ➞ "no"
is_prime(primes, 67) ➞ "yes"
is_prime(primes, 36) ➞ "no"
'''


def is_prime(number,primes):
    try:
        logging.info('entering is_prime() function')
        if type(number) == int and type(primes) == list:
            primes.sort()
            low, mid, high = 0, 0, len(primes) - 1
            while low <= high:
                mid = (low + high) // 2
                if primes[mid] == number:
                    return 'yes'
                elif primes[mid] > number:
                    high = mid - 1
                else:
                    low = mid + 1
            return 'no'
        else:
            raise TypeError('Input should be integer and list')
    except Exception as e:
        logging.error(e)


# print(is_prime(3,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]))
'''
4. Create a function that takes in n, a, b and returns the number of positive values raised to 
the nth power that lie in the range [a, b], inclusive.
Examples
power_ranger(2, 49, 65) ➞ 2
# 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)
power_ranger(3, 1, 27) ➞ 3
# 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)
power_ranger(10, 1, 5) ➞ 1
# 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)
power_ranger(5, 31, 33) ➞ 1
power_ranger(4, 250, 1300) ➞ 3
'''


def power_ranger(n,a,b):
    try:
        logging.info('entering power_ranger() function')
        if type(n) == int and type(a) == int and type(b) == int:
            count, i = 0,1
            while i**n <= b and i**n <= a:
                count += 1
                i += 1
            return count
        else:
            raise TypeError('Input should be integers')
    except Exception as e:
        logging.error(e)


# print(power_ranger(4, 250, 1300))
'''
5. Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.
Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833
rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823
rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
'''


def rearranged_difference(number):
    ' tells the difference of maxm and minm when shuffle the given number '
    try:
        logging.info('entering rearranged_difference() function')
        if type(number) == int:
            num_list = list(str(number))
            num_list.sort()
            minm = ''.join(num_list)
            maxm = ''.join(num_list[::-1])
            return int(maxm)-int(minm)
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(rearranged_difference(3320707))
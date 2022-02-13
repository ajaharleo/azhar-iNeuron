import logging
logging.basicConfig(filename='Prog9.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. YouTube offers different playback speed options for users. This allows users to increase or decrease the speed of the
video content. Given the actual duration and playback speed of the video, calculate the playback duration of the video.
Examples
playback_duration("00:30:00", 2) ➞ "00:15:00"
playback_duration("01:20:00", 1.5) ➞ "00:53:20"
playback_duration("51:20:09", 0.5) ➞ "102:40:18"
'''


def playback_duration(time_str,speed):
    ' take duration of video in string and speed in float and return the actual time '
    try:
        logging.info('entering playback_duration() function')
        if type(time_str) == str and (type(speed) ==float or type(speed)==int):
            time_ = time_str.split(':')
            seconds = int(time_[0])*3600 + int(time_[1])*60 + int(time_[2])
            actual_seconds = seconds / speed
            hours = actual_seconds // 3600
            actual_seconds = actual_seconds % 3600
            minutes = actual_seconds // 60
            seconds = actual_seconds % 60
            return f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
        else:
            raise TypeError('Input should be string and float')
    except Exception as e:
        logging.error(e)


# print(playback_duration("01:20:00", 1.5))
'''
2. We needs your help to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and 
so on until the top which will have a volume of 1^3.
Given the total volume m of the building, can you find the number of cubes n required for the building?
In other words, you have to return an integer n such that:
n^3 + (n-1)^3 + ... + 1^3 == m
Return None if there is no such number.
Examples
pile_of_cubes(1071225) ➞ 45
pile_of_cubes(4183059834009) ➞ 2022
pile_of_cubes(16) ➞ None
'''


def pile_of_cubes(number):
    try:
        logging.info('entering pile_of_cubes() function')
        if type(number) == int:
            for i in range(number):
                cube_sum = (i*(i+1)/2)**2 # formula to get cube of first n natural numbers
                if cube_sum == number:
                    return i
        else:
            raise TypeError('Input should be integer')
    except Exception as e:
        logging.error(e)


# print(pile_of_cubes(4183059834009))
'''
3. A fulcrum of a list is an integer such that all elements to the left of it and all elements to the 
right of it sum to the same value. Write a function that finds the fulcrum of a list.
To illustrate:
find_fulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
// Since [3, 1, 5] and [4, 6, -1] both sum to 9
Examples
find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4
find_fulcrum([9, 1, 9]) ➞ 1
find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0
find_fulcrum([8, 8, 8, 8]) ➞ -1
'''


def find_fulcrum(items):
    try:
        logging.info('entering find_fulcrum() function')
        if type(items) == list:
            for i in range(1,len(items)-1):
                if sum(items[:i]) == sum(items[i+1:]):
                    return items[i]
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))
'''
4. Given a list of integers representing the color of each sock, determine how many pairs of socks with 
matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. 
There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
Create a function that returns an integer representing the number of matching pairs of socks that are available.
Examples
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4
sock_merchant([]) ➞ 0
'''


def sock_merchant(socks):
    try:
        logging.info('entering sock_merchant() function')
        if type(socks) == list:
            uniques = list(set(socks))
            pairs = 0
            for i in uniques:
                if socks.count(i) >= 2:
                    if socks.count(i) % 2 == 0:
                        pairs += socks.count(i)//2
                    else:
                        pairs += socks.count(i)//2
            if len(socks) == 0:
                return 0
            else:
                return pairs
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
'''
5. Create a function that takes a string containing integers as well as other characters and return the sum of the negative integers only.
Examples
negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23
negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33
'''


def negative_sum(str_sum):
    try:
        logging.info('entering negative_sum() function')
        if type(str_sum) == str:
            import re
            str_sum = re.sub(r'[^0-9-]', ' ', str_sum)
            inp = ''
            for i in range(len(str_sum)):
                if str_sum[i] == '-' and str_sum[i-1] in '0123456789':
                    inp += ' '+str_sum[i]
                else:
                    inp += str_sum[i]
            numbers = inp.split(' ')
            negatives = 0
            for i in numbers:
                if int(i) < 0:
                    negatives += int(i)
            return negatives
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(negative_sum("22 13%14&-11-22 13 12"))
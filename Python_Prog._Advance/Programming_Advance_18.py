import logging
import re

logging.basicConfig(filename='Prog18.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. A robot has been given a list of movement instructions. Each instruction is either left, right, up or down, 
followed by a distance to move. The robot starts at [0, 0]. 
You want to calculate where the robot will end up and return its final position as a list.
To illustrate, if the robot is given the following instructions:
["right 10", "up 50", "left 30", "down 10"]
It will end up 20 left and 40 up from where it started, so we return [-20, 40].
Examples
track_robot(["right 10", "up 50", "left 30", "down 10"]) ➞ [-20, 40]
track_robot([]) ➞ [0, 0]
// If there are no instructions, the robot doesn't move.
track_robot(["right 100", "right 100", "up 500", "up 10000"]) ➞ [200, 10500]
'''


def track_robot(commands):
    ' tells position of robot after certain movements '
    try:
        logging.info('entering track_robot() function')
        if type(commands) == list:
            position = [0,0]
            for i in commands:
                command = i.split()
                if command[0] == 'left':
                    position[0] -= int(command[1])
                elif command[0].lower() == 'right':
                    position[0] = position[0] + int(command[1])
                elif command[0].lower() == 'down':
                    position[1] -= int(command[1])
                elif command[0].lower() == 'up':
                    position[1] += int(command[1])
                else:
                    raise ValueError('Input movement not valid')
            return position
        else:
            raise TypeError('Input should be list')
    except Exception as e:
        logging.error(e)


# print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
'''
2. Write a function that will return the longest word in a sentence. In cases where more than one word is found, return the first one.
Examples
find_longest("A thing of beauty is a joy forever.") ➞ "forever"
find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"
'''


def find_longest(sentence):
    ' return the longest word in given string '
    try:
        logging.info('entering find_longest() function')
        if type(sentence) == str:
            import re
            sentence = re.sub(r'[^a-zA-Z\s]','',sentence)
            words = sentence.split()
            max_len = max(list(map(len, words)))
            for word in words:
                if len(word) == max_len:
                    return word
        else:
            raise TypeError('Input should be string')
    except Exception as e:
        logging.error(e)


# print(find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel."))
'''
3. Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.
The criteria for a candidate to be qualified in the coding interview is:
   1. The candidate should have complete all the questions.
   2. The maximum time given to complete the interview is 120 minutes.
   3. The maximum time given for very easy questions is 5 minutes each.
   4. The maximum time given for easy questions is 10 minutes each.
   5. The maximum time given for medium questions is 15 minutes each.
   6. The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".
You will be given a list of time taken by a candidate to solve a particular question and 
the total time taken by the candidate to complete the interview.
Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].
The maximum time to complete the interview includes a buffer time of 20 minutes.
Examples
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"
interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"
interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.
interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.
interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.
'''


def interview(time, total):
    ' tells if a candidate is qualified or not on given criteria '
    try:
        logging.info('entering interview() function')
        if type(time) == list and type(total) == int:
            if len(time) != 8:
                return 'disqualified'
            elif time[0] > 5 or time[1] > 5:
                return 'disqualified'
            elif time[2] > 10 or time[3] > 10:
                return 'disqualified'
            elif time[4] > 15 or time[5] > 15:
                return 'disqualified'
            elif time[6] > 20 or time[7] > 20:
                return 'disqualified'
            elif total > 120:
                return 'disqualified'
            return 'qualified'
        else:
            raise TypeError('Input should be list of integers and an integer')
    except Exception as e:
        logging.error(e)


# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
'''
4. Write a function that divides a list into chunks of size n, where n is the length of each chunk.
Examples
chunkify([2, 3, 4, 5], 2) ➞ [[2, 3], [4, 5]]
chunkify([2, 3, 4, 5, 6], 2) ➞ [[2, 3], [4, 5], [6]]
chunkify([2, 3, 4, 5, 6, 7], 3) ➞ [[2, 3, 4], [5, 6, 7]]
chunkify([2, 3, 4, 5, 6, 7], 1) ➞ [[2], [3], [4], [5], [6], [7]]
chunkify([2, 3, 4, 5, 6, 7], 7) ➞ [[2, 3, 4, 5, 6, 7]]
'''


def chunkify(original,size):
    ' divides a list into chunk of size '
    try:
        logging.info('entering chunkify() function')
        if type(original) == list and type(size) == int:
            result = []
            for i in range(0,len(original),size):
                result.append(original[i:i+size])
            return result
        else:
            raise TypeError('Input should be list and integer')
    except Exception as e:
        logging.error(e)


# print(chunkify([2, 3, 4, 5, 6, 7], 7))
'''
5. You are given a list of strings consisting of grocery items, with prices in parentheses. 
Return a list of prices in float format.
Examples
get_prices(["salad ($4.99)"]) ➞ [4.99]
get_prices(["artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"])➞ [1.99, 5.99, 0.75]
get_prices(["ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"])➞ [5.99, 0.2, 8.50, 1.99]
'''


def get_prices(grocery):
    ' return the sum of grocery items given in a list of string '
    try:
        logging.info('entering get_prices() function')
        if type(grocery) == list:
            result = []
            import re
            pattern = re.compile(r'([0-9]+.[0-9]+)')
            for i in grocery:
                temp = re.findall(pattern,i)
                result.append(float(temp[0]))
                temp = []
            return result
        else:
            raise TypeError('Input should be list of strings')
    except Exception as e:
        logging.error(e)


# print(get_prices(["ice cream ($5.99)","banana ($0.20)","sandwich ($8.50)","soup ($1.99)"]))

import logging
logging.basicConfig(filename='Prog22.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

'''
1. Create a class Smoothie and do the following:
    - Create an instance attribute called ingredients.
    - Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
    - Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. 
    Round to two decimal places.
    - Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive 
    sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". 
    sRemember to change "-berries" to "-berry". See the examples below.
Ingredient	   Price
Strawberries   $1.50
Banana	       $0.50
Mango	       $2.50
Blueberries	   $1.00
Raspberries	   $1.00
Apple	       $1.75
Pineapple	   $3.50
Examples
s1 = Smoothie(["Banana"])
s1.ingredients ➞ ["Banana"]
s1.get_cost() ➞ "$0.50"
s1.get_price() ➞ "$1.25"
s1.get_name() ➞ "Banana Smoothie"
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
s2.get_cost() ➞ "$3.50"
s2.get_price() ➞ "$8.75"
s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"
'''


class Smoothie:
    Prices = {'Strawberries':1.50,'Banana':0.50,'Mango':2.50,'Blueberries':1.00,'Raspberries':1.00,'Apple':1.75,'Pineapple':3.50}
    def __init__(self,ingredients):
        logging.info('Creating object for Smoothie class')
        try:
            if type(ingredients==list):
                self.ingredients = ingredients
        except:
            raise TypeError('Ingredients should be in list format')


    def get_cost(self):
        cost = 0
        logging.info('calculating cost of the smoothie with given ingredients')
        for  item in self.ingredients:
            cost += Smoothie.Prices[item]
        return cost

    def get_price(self):
        logging.info('calculating price of smoothie')
        price = 2.5 * self.get_cost()
        return round(price,2)

    def get_name(self):
        result =''
        logging.info('getting name of all ingredients')
        self.ingredients.sort()
        if len(self.ingredients) == 1:
            result = self.ingredients[0] + ' ' + 'Smoothie'
        else:
            for item in self.ingredients:
                if item.lower().endswith('ies'):
                    result += item[:-3] + 'y' + ' '
                elif item.lower().endswith('s'):
                    result += item[:-1] +' '
                else:
                    result += item + ' '
            result = result + 'Fusion'
        return result


# s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
# print(s2.get_name())


'''
2. Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper 
and to be also able to assign a minimum pass mark. The testpaper's subject should also be included. The attributes are in the following order:
  1. subject
  2. markscheme
  3. pass_mark
As well as that, we need to create student objects to take the test itself! Create another class called Student and do the following:
  - Create an attribute called tests_taken and set the default as 'No tests taken'.
  - Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers.
  Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way 
  as shown in the point below.
  - Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen 
  in the examples below (whether or not the student has failed, and their percentage in brackets).
Examples
paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
student1 = Student()
student2 = Student()
student1.tests_taken ➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}
'''


class Testpaper:
    def __init__(self,subject,markscheme,pass_mark):
        try:
            self.subject = subject
            self.markscheme = markscheme
            self.pass_mark = pass_mark
            logging.info('Creating Testpaper object')
        except Exception as e:
            logging.error(e)


class Student:
    def __init__(self,tests_taken = 'No tests taken'):
        logging.info('Creating Student object')
        self.tests_taken = tests_taken

    def take_test(self,test_obj,answers):
        correct_ans = 0
        if type(self.tests_taken) == str:
            self.tests_taken = {}
        logging.info('Calculating marks and declaring result for the test')
        for i in range(len(answers)):
            if test_obj.markscheme[i] == answers[i]:
                correct_ans += 1
        marks = int(correct_ans*100/len(answers))
        result = ''
        if marks >= int(test_obj.pass_mark[:-1]):
            result = f'Passed! ({marks}%)'
        else:
            result = f'Failed! ({marks}%)'
        self.tests_taken[test_obj.subject] = result


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
student1 = Student()
student2 = Student()
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# print(student2.tests_taken)
'''
3. Due to unforseen circumstances in Suburbia, the trains will be delayed by a further 10 minutes.
Create a function that will help to plan out and manage these delays! Create a function called manage_delays that does the following:
   - Parameters will be the train object, a destination and number of minutes the delay is.
   - Increment to the train object's expected_time by the delay, if the destination given is in the train object's destinations.
Examples
trains = [
  Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
  Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
  Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")]
for t in trains:
    manage_delays(t, "Lakeside Valley", 60)
trains[0].expected_time ➞ "13:04"
trains[1].expected_time ➞ "14:20"
trains[2].expected_time ➞ "14:22"
'''


class Train:
    def __init__(self,stations,expected_time):
        self.stations = stations
        self.expected_time = expected_time


def manage_delays(train_object, destination, delay):
    time_lst = train_object.expected_time.split(':')
    if destination in train_object.stations:
        time_lst[1] = int(time_lst[1]) + int(delay)
        if time_lst[1] >= 60:
            time_lst[0] = int(time_lst[0]) + (int(time_lst[1]) // 60)
            time_lst[1] = int(time_lst[1]) % 60
            if len(str(time_lst[1])) == 1:
                time_lst[1] = '0' + str(time_lst[1])
        train_object.expected_time = f'{time_lst[0]}:{time_lst[1]}'


trains = [Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
  Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
  Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")]
for t in trains:
    manage_delays(t, "Lakeside Valley", 60)
# print(trains[1].expected_time)


'''
4. Ted works as a computer programmer at Minecraft Inc. His boss has just given him an important assignment to 
update the code for the minecart tracks by the end of April. However, he has recently had to self-isolate due to 
Covid-19 and has left the code for the tracks BACK AT WORK!! He has the shorthand for the tracks he's supposed to look at,
 and where the carts are suppost to end up, but not the actual code.
He knows that:
  1. "-->" = "Speed-Up Track" ⁠— If a minecart interacts with this track, it's velocity increases by 2.67 BPS unless 
  it's at its maximum sp
  eed of 8 BPS.
  2. "<-->" = "Powered Track" ⁠— If a minecart interacts with this track, it's velocity remains the same.
  3. "<--" = "Slow-Down Track" ⁠— If a minecart interacts with this track, it's velocity decreases by 2.67 BPS unless 
  it's velocity equals 0, at which point it stops.
  4. "---" = "Unpowered Track" ⁠— If a minecart interacts with this track, it's velocity decreases by 1 BPS unless 
  it's velocity equals 0, at which point it stops.
 Help Ted by writing a class for the tracks that interact with the provided Minecart class as shown above. 
 And then write a function that will take a list of the shorthand tracks and:
   - If the Minecart reaches the last peice of Track, return True.
   - Else return the index of the Track where the Minecart stops.
Examples
mine_run(["-->", "-->", "-->", "<--", "<--", "<--"]) ➞ True
mine_run(["-->", "<--", "-->", "-->", "<-->", "---"]) ➞ 1
'''


class Minecraft:
    def __init__(self, tracks):
        self.speed = 0
        self.tracks = tracks


def mine_run(short_tracks):
    ' take a list of minecraft tracks and return True if reach at the end of the list '
    try:
        logging.info('entering mine_run() function')
        if type(short_tracks) == list:
            mine = Minecraft(short_tracks)
            for track in mine.tracks:
                if track == "-->":
                    mine.speed += 2.67
                    if mine.speed > 8.0:
                        mine.speed = 8.0
                elif track == "<-->":
                    pass
                elif track == "<--":
                    mine.speed -= 2.67
                    if mine.speed == 0.0:
                        return mine.tracks.index(track)
                elif track == "---":
                    mine.speed -= 1.0
                    if mine.speed == 0.0:
                        return mine.tracks.index(track)
            else:
                return True
        else:
            raise TypeError('Input should be a list')
    except Exception as e:
        logging.error(e)


# print(mine_run(["-->", "<--", "-->", "-->", "<-->", "---"]))
'''
5. Make a Rectangle class with four parameters, an x, a y (representing the top-left corner of the rectangle), 
a width and a height exclusively in that order.
Lastly, make a function intersecting that takes two Rectangle objects and returns True if those objects are intersecting
(colliding), else return False.
Examples
a = Rectangle(10, 20, 100, 20)
b = Rectangle(10, 40, 15, 20)
c = Rectangle(50, 50, 20, 30)
intersecting(a, b) ➞ True
intersecting(a, c) ➞ False
intersecting(b, c) ➞ True
'''


class Rectangle:
    def __init__(self,x,y,width,height):
        self.left_x = x
        self.left_y = y
        self.width = width
        self.height = height
        self.top_left = (self.left_x,self.left_y)
        self.top_right = (self.left_x + self.width, self.left_y)
        self.bottom_left = (self.left_x, self.left_y-self.height)
        self.bottom_right = (self.left_x + self.width, self.left_y - self.height)


def intersection(rect1, rect2):
    ' takes two rectangle object and return True if they are intersecting '
    try:
        logging.info('entering intersection() function')
        rect1_corners = [rect1.top_left,rect1.top_right,rect1.bottom_left,rect1.bottom_right]
        for corner in rect1_corners:
            if ((rect2.top_left[0] <= corner[0]) and (rect2.top_right[0] >= corner[0])) and \
                    ((rect2.bottom_left[1] <= corner[1]) and (rect2.top_left[1] >= corner[0])):
                return True
        else:
            return False
    except Exception as e:
        logging.error(e)

# NOTE:  b and c is not intersecting
a = Rectangle(10, 20, 100, 20)
b = Rectangle(10, 40, 15, 20)
c = Rectangle(50, 50, 20, 30)
# print(intersection(b,c))
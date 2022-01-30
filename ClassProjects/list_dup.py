import logging


class ListClass:
    import logging
    logging.basicConfig(filename='list.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    def __init__(self, *args):
        self.out = list(args)  # creating list of items given to the class
        logging.info('__init__:Creating object to the class ListClass')

    def append(self, item):
        self.out = self.out + [item]
        logging.info(f'append:Appending item {item} to the end of the list')

    def clear(self):
        self.out = []
        logging.info('clear:Clearing the list object')

    def copy(self):
        return self.out
        logging.info('copy: Creating a copy of the current object')

    def count(self, item):
        logging.info(f'count:Counting occurance of item {item} in the list object')
        val = 0
        for i in self.out:
            if i == item:
                val += 1
        return val

    def extend(self, iterable):
        try:
            if type(iterable) == str or type(iterable) == list or type(iterable) == tuple:
                for i in iterable:
                    self.out.append(i)
        except:
            logging.error('extend:Raised type error as given item is not an iterable')
            raise Exception(iterable, 'is not an iterable item')

    def index(self, item):
        val = 0
        logging.info(f'index:finding index of item {item} in the list object')
        for i in self.out:
            if i == item:
                break
            else:
                val += 1
        return val

    def insert(self, index, item):
        logging.info(f'insert:Inserting item {item} to the index {index}')
        self.out = self.out[:index]+[item]+self.out[index:]

    def pop(self, index=-1):
        logging.info(f'pop:Removing item from the index {index}')
        if len(self.out) == 0 or index > len(self.out):
            logging.error('Index out of range OR empty list')
            raise IndexError
        deleted = self.out[index]
        self.out = self.out[:index]+self.out[index+1:]
        return deleted

    def remove(self, item):
        logging.info(f'remove:Removing item {item} from the list object')
        if item not in self.out:
            logging.error(f'Given item {item} is not in the list object')
            raise ValueError
        for i in range(len(self.out)):
            if self.out[i] == item:
                del self.out[i]
                break

    def reverse(self):
        logging.info('reverse:Reverse function intiated')
        self.out = self.out[::-1]

    def sort(self, reverse=False):
        self.result = []
        while self.out:
            mini = self.out[0]
            for i in self.out:
                if i < mini:
                    mini = i
            self.result.append(mini)
            self.out.remove(mini)
        if reverse == False or reverse == 0:
            self.out = self.result.copy()
        elif reverse == True or reverse == 1:
            self.out = self.result[::-1]
        else:
            raise ValueError('wrong keyword argument')


#a = ListClass(1,2,0,-3,7,-87)
#c = a.index(-3)
#print(c)
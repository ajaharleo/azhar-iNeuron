import logging


class TupleClass:
    logging.basicConfig(filename='Tuple.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    def __init__(self,*args):
        self.tple = (args)
    logging.info('Creating object of the class TupleClass')

    def Count(self,item):
        '''returns the occurance of the item inside object'''
        logging.info(f'Count: trying to find out the number of occurance of item {item} inside self.tple')
        count = 0
        for i in self.tple:
            if item in self.tple:
                count+=1
        return count

    def index(self,item):
        '''returns the index of given item'''
        try:
            val = 0
            logging.info(f'index:finding index of item {item} in the object')
            for i in self.tple:
                if i == item:
                    break
                else:
                    val += 1
            return val
        except:
            logging.error(f'index: key {key} not present in the object')
            raise KeyError

#a =TupleClass(2,3,4,6,744,56,-45)
#a.tple
#print(a.index(744))
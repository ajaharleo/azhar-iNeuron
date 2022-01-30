import logging

class SetClass:
    logging.basicConfig(filename='Set.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    def __init__(self,*args):
        self.st = set(args)

    def Add(self,item):
        '''add item to the set if not present else do nothing'''
        if item in self.st:
            logging.info(f'Add: item {item} already present in the set')
        else:
            logging.info(f'Add: adding item {item} to the set')
            result = list(self.st)
            result.append(item)
            self.st = set(result)

    def Clear(self):
        '''removes all elements from the set'''
        logging.info('Clear: removing all elements from the object')
        self.st = set()

    def Copy(self):
        ''' return a shallow copy of the object '''
        logging.info('Copy: returning copy of the object')
        return self.st

    def Difference(self,*args):
        '''return the difference among two or more sets'''
        try:
            logging.info('Difference: returning difference of objects')
            second = []
            for i in args:
                second += list(i)
            first = list(self.st)
            result = []
            for i in first:
                if i not in second:
                    result.append(i)
            return set(result)
        except:
            raise KeyError('Please input correct datatype')

    def Difference_update(self,*args):
        ''' remove elements from original object which are also in other objects'''
        try:
            logging.info('Difference_update: updating original object')
            second = []
            for i in args:
                second += list(i)
            first = list(self.st)
            result = []
            for i in first:
                if i not in second:
                    result.append(i)
            self.st = set(result)
        except:
            raise KeyError('Please input correct datatype')

    def Discard(self,item):
        '''remove item from the object if present else do nothing'''
        if item in self.st:
            logging.info(f'Discard: removing item {item} from the object')
            result = list(self.st)
            result.remove(item)
            self.st = set(result)
        else:
            logging.info(f'Add: item {item} not in the object')

    def Intersection(self, *args):
        '''return the common elements among two or more objects as a new object'''
        logging.info('Intersection: returning common elements')
        second = []
        for i in args:
            second += list(i)
        first = list(self.st)
        result = []
        for i in first:
            if i in second:
                result.append(i)
        return set(result)

    def Intersection_update(self, *args):
        '''update original object with common elements among two or more objects'''
        logging.info('Intersection_update: updating original object with common elements')
        second = []
        for i in args:
            second += list(i)
        first = list(self.st)
        result = []
        for i in first:
            if i in second:
                result.append(i)
        self.st = set(result)

    def disjoint(self, *args):
        '''return true if there are no elements common else false'''
        logging.info('disjoint: checking common elements')
        second = []
        for i in args:
            second += list(i)
        first = list(self.st)
        count = 0
        for i in first:
            if i in second:
                count+=1
        if count == 0:
            return True
        else:
            return False

    def Subset(self,another):
        ''' return true if all items from original object present in another'''
        logging.info('Subset: checking subset')
        first = list(self.st)
        second = list(another)
        for i in first:
            if i not in second:
                logging.info('Subset: first is not a subset of another')
                return False
            else:
                continue
        return True

    def Superset(self,another):
        ''' return true if all items in another object present inside original object '''
        logging.info('Superset: checking subset')
        first = list(self.st)
        second = list(another)
        for i in second:
            if i not in first:
                logging.info('Superset: first is not superset of another')
                return False
            else:
                continue
        logging.info('Superset: first is superset of another')
        return True

    def Pop(self):
        '''remove random item from the object'''
        try:
            first = list(self.st)
            import random
            deleted = first[random.randint(0,len(first)-1)]
            first.remove(deleted)
            logging.info(f'Pop: removing random item {deleted}')
            self.st = set(first)
            return deleted
        except:
            logging.error('object is empty')
            raise KeyError

    def Remove(self,item):
        '''remove given item from the object'''
        try:
            first = list(self.st)
            first.remove(item)
            logging.info(f'Remove: removing item {item}')
            self.st = set(first)
            return item
        except:
            logging.error(f'Remove: item {item} not found')
            raise KeyError

    def Symmetric_difference(self,*args):
        '''retrurn object with items not present in both'''
        logging.info('Symmetric_difference: creating a superset without common elements')
        first = list(self.st)
        second = []
        for i in args:
            second += list(i)
        superset = second + first
        result = []
        for i in superset:
            if i not in first and i not in second:
                result.append(i)
        return set(result)

    def Symmetric_difference_update(self,*args):
        '''update original object with items not present in both'''
        logging.info('Symmetric_difference_update: creating a superset without common elements')
        first = list(self.st)
        second = []
        for i in args:
            second += list(i)
        superset = second + first
        result = []
        for i in superset:
            if i not in first and i not in second:
                result.append(i)
        self.st = set(result)
        return self.st

    def Union(self,*args):
        '''returns object with items present in both'''
        logging.info('Union: creating a superset without common elements')
        first = list(self.st)
        second = []
        for i in args:
            second += list(i)
        superset = second + first
        return set(superset)

    def Update(self,*args):
        '''update original object with items present in both'''
        logging.info('Update: creating a superset without common elements')
        first = list(self.st)
        second = []
        for i in args:
            second += list(i)
        superset = second + first
        self.st = set(superset)
        return self.st

#a = SetClass(2, 3, 4, 2, 31, 3, 1, 5)
#print(a.Pop())
#print(a.st)
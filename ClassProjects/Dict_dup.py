import logging


class DictClass:
    logging.basicConfig(filename='Dict.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    def __init__(self,**kwargs):
        logging.info('Creating object to the class DictClass')
        self.dct = kwargs

    def Clear(self):
        '''clear item from object'''
        self.dct = {}
        logging.info('Clear: remove all items from dictionary')

    def Copy(self):
        '''d.Copy() creae a shallow copy of d'''
        logging.info('Copy: ceating a shallow copy of object')
        return self.dct

    def Fromkeys(self,iterable,value=None):
        '''Create a new dictionary with keys from iterable and values set to value'''
        if type(iterable)==str or type(iterable)==list or type(iterable)==tuple:
            logging.info('Fromkeys: return an object with keys as items of iterable')
            self.result = {}
            for i in iterable:
                self.result[i]=value
        else:
            logging.error(f'Fromkeys: Given item {item} not iterable')
            raise TypeError("Item should be iterable")

    def Get(self,key,default=None):
        '''Return the value for key if key is in the dictionary, else return default'''
        if key in self.dct:
            logging.info(f'Get: {key} found in the object')
            return self.dct[key]
        else:
            logging.info(f'Get: {key} not found in the object')
            return default

    def Setdefault(self,key,default=None):
        '''Insert a key in the object with default value if key not present in the object'''
        if key in self.dct:
            logging.info(f'Setdefault: key {key} present in the object')
            pass
        else:
            logging.info(f'Setdefault: key {key} not found in the object')
            self.dct[key] = default

    def Items(self):
        '''return set of key and values in object'''
        logging.info('Items: returning items in the key value pair')
        result = []
        for i in self.dct:
            result.append((i,self.dct[i]))
        return result

    def Keys(self):
        '''return set of keys in object'''
        logging.info('Keys: returning keys available in the object')
        result = []
        for i in self.dct:
            result.append(i)
        return result

    def Values(self):
        '''return set of Values in object'''
        logging.info('Values: returning Values available in the object')
        result = []
        for i in self.dct:
            result.append(self.dct[i])
        return result

    def Pop(self,key,default = None):
        '''return the respected value to the key and remove from the object'''
        if key in self.dct:
            logging.info(f'Pop: key {key} found in the object')
            return self.dct[key]
            del self.dct[key]
        else:
            logging.info(f'key {key} not found in the object')
            if default != None:
                return default
            else:
                raise KeyError

    def Popitem(self):
        key = list(self.dct.keys())
        result = (key[-1],self.dct[key[-1]])
        del self.dct[key[-1]]
        return result

    def Update(self,iterable,**kwargs):
        '''add key value pair to the object'''
        logging.info('Update: updating object')
        if type(iterable) == dict:
            for i in iterable:
                self.dct[i] = iterable[i]
        else:
            for i,j in kwargs.items():
                self.dct[i] = j

#d = DictClass(a=12, b=23)
#e = d.Setdefault('c',default='Hey')
#print(d.dct)
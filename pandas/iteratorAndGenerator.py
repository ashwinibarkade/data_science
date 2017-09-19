
class CIterator:
    def __init__(self,min,max):
        self.min = min
        self.max = max
    def __iter__(self):
        return self
    def next(self):
        if(self.min > self.max):
            raise StopIteration
        else:
            self.min = self.min + 1
            return self.min


def CGenerator(min,max):
    min = min
    max = max
    while(min<max):
        yield min
        min = min + 1

for c in CGenerator(1,10):
    print(c)


#iterator = CIterator(1,10)
#print(list(iterator))
#print(iterator.next())
#print(iterator.next())

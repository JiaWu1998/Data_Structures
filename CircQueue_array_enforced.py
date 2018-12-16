class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    def enqueue(self, val):
        if None in self.data:
            if self.tail == len(self.data)-1:
                for x in range(len(self.data)-1):
                    self.data[x] = self.data[x+1]
                self.tail -= 1
                self.head -= 1
            self.tail += 1
            self.data[self.tail] = val
        else:
            raise RuntimeError
        pass
        
    def dequeue(self):
        returnVal = None
        if self.head == -1:
            self.head = 0
        if self.empty():
            raise RuntimeError
        else:
            returnVal = self.data[self.head]
            self.data[self.head] = None
            self.head += 1
        if self.head == len(self.data):
            self.head = -1
        return returnVal
        pass
    
    def resize(self, newsize):
        assert(len(self.data) < newsize)
        self.tail = len(self.data)-1
        newsize -= len(self.data)
        self.data += [None] * newsize
        pass
    
    def empty(self):
        counts = 0
        for x in self.data:
            if x != None:
                counts += 1
        if counts != 0:
            return False
        else:
            return True
        pass
    
    def __bool__(self):
        return not self.empty()
    
    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        class iterClass:
            def __init__(self,data,head):
                self.lst = data
                self.idx = head
                self.count = 0
            def __next__(self):
                if self.count == len(self.lst):
                    raise StopIteration
                if self.idx == len(self.lst):
                    self.idx = 0
                if self.lst[self.idx] == None:
                    self.count += 1
                    self.idx += 1
                    return self.__next__()
                else:
                    returnVa = self.lst[self.idx]
                    self.count += 1
                    self.idx += 1
                    return returnVa
            def __iter__(self):
                return self
        returnVal = iterClass(self.data,self.head)
        return returnVal
        pass
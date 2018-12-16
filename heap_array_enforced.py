class Heap:
    def __init__(self, key=lambda x:x):
        self.data = []
        self.key  = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2
        
    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2
    
    def heapify(self, idx=0):
        parent = idx
        children = True
        while(children):
            rightChildExist = True
            leftChildExist = True
            leftChild = ''
            rightChild = ''
            try:
                leftChild = self._left(parent)
                test = self.data[leftChild]
            except IndexError:
                leftChildExist = False
            try:
                rightChild = self._right(parent)
                test = self.data[rightChild]
            except IndexError:
                rightChildExist = False
            if (not rightChildExist) and (not leftChildExist):
                children = False
            else:
                #atleast one children or more
                if rightChildExist and leftChildExist:
                    #continues 
                    if self.key(self.data[rightChild]) > self.key(self.data[leftChild]):
                        #rightchild is bigger 
                        if self.key(self.data[parent]) < self.key(self.data[rightChild]):
                            hold = self.data[parent]
                            self.data[parent] = self.data[rightChild]
                            self.data[rightChild] = hold
                            parent = rightChild
                        else:
                            children = False
                    else:
                        #leftchild is bigger or equal
                        if self.key(self.data[parent]) < self.key(self.data[leftChild]):
                            hold = self.data[parent]
                            self.data[parent] = self.data[leftChild]
                            self.data[leftChild] = hold
                            parent = leftChild
                        else:
                            children = False
                elif rightChildExist:
                    if self.key(self.data[parent]) < self.key(self.data[rightChild]):
                        hold = self.data[parent]
                        self.data[parent] = self.data[rightChild]
                        self.data[rightChild] = hold
                        parent = rightChild
                    else:
                        children = False
                elif leftChildExist:
                    if self.key(self.data[parent]) < self.key(self.data[leftChild]):
                        hold = self.data[parent]
                        self.data[parent] = self.data[leftChild]
                        self.data[leftChild] = hold
                        parent = leftChild
                    else:
                        children = False
        pass
            
    def add(self, x):
        self.data.append(x)
        idx = len(self.data)-1
        itemX = idx
        while(idx > 0): 
            idx = self._parent(idx)
            if self.key(self.data[idx]) < self.key(self.data[itemX]):
                hold = self.data[idx]
                self.data[idx] = self.data[itemX]
                self.data[itemX] = hold
                itemX = idx
            else:
                idx = -1
        pass
    def peek(self):
        return self.data[0]

    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        self.heapify()
        return ret
    
    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)
class OrderedHashtable:
    class Node:
        """This class is used to create nodes in the singly linked "chains" in
        each hashtable bucket."""
        def __init__(self, index, next=None):
            # don't rename the following attributes!
            self.index = index
            self.next = next
        
    def __init__(self, n_buckets=1000):
        # the following two variables should be used to implement the "two-tiered" 
        # ordered hashtable described in class -- don't rename them!
        self.indices = [None] * n_buckets
        self.entries = []
        self.count = 0
        
    def __getitem__(self, key):
        existKey = False
        chainIdx = hash(key)%len(self.indices)
        currentNode = self.indices[chainIdx]
        stopNode = True
        returnVal = ''
        if currentNode != None:
            while(stopNode):
                if self.entries[currentNode.index][0] == key:
                    returnVal = self.entries[currentNode.index][1]
                    existKey = True
                if currentNode.next == None:
                    stopNode = False
                else:
                    currentNode = currentNode.next
        if existKey:
            return returnVal
        else:
            raise KeyError
        pass
    
    def __setitem__(self, key, val):    
        chainIdx = hash(key)%len(self.indices)
        if self.indices[chainIdx] == None:
            self.indices[chainIdx] = self.Node(len(self.entries),None)
            self.entries.append([key,val])
        else:
            stopNode = True
            currentNode = self.indices[chainIdx]
            while stopNode:
                if currentNode.next == None:
                    currentNode.next = self.Node(len(self.entries),None)
                    stopNode = False
                else:
                    currentNode = currentNode.next
            self.entries.append([key,val])
        self.count += 1
        pass
    
    def __delitem__(self, key):
        lstOfDeletes = []
        chainIdx = hash(key)%len(self.indices)
        currentNode = self.indices[chainIdx]
        stopNode = True
        doesNotExist = True
        count = 0
        if currentNode != None:
            while(stopNode):
                if self.entries[currentNode.index][0] == key:
                    doesNotExist = False
                    lstOfDeletes.append(currentNode.index)
                if currentNode.next == None:
                    stopNode = False
                else:
                    currentNode = currentNode.next
                    count += 1
        if doesNotExist:
            raise KeyError
        else:
            for x in lstOfDeletes:
                self.count -= 1
                self.entries[x] = None
            while(None in self.entries):
                self.entries.remove(None)

            for x in range(len(self.indices)):
                self.indices[x] = None
            copyEnteries = self.entries.copy()
            self.count = 0
            self.entries = []
            for b in copyEnteries:
                self.__setitem__(b[0],b[1])
        pass
        
    def __contains__(self, key):
        existKey = False
        chainIdx = hash(key)%len(self.indices)
        currentNode = self.indices[chainIdx]
        stopNode = True
        if currentNode != None:
            while(stopNode):
                if self.entries[currentNode.index][0] == key:
                    existKey = True
                if currentNode.next == None:
                    stopNode = False
                else:
                    currentNode = currentNode.next
        
        if existKey:
            return True
        else:
            return False
        pass
        
        
    def __len__(self):
        return self.count
    
    def __iter__(self):
        class keyIterator:
            def __init__(self,entriesHis):
                self.idx = 0
                self.lstOfKeys = [a for a,b in entriesHis]
            def __next__(self):
                if self.idx == len(self.lstOfKeys):
                    raise StopIteration
                returnNextItem = self.lstOfKeys[self.idx]
                self.idx += 1
                return returnNextItem
            def __iter__(self):
                return self
        returnVal = keyIterator(self.entries)
        return returnVal
        pass
        
    def keys(self):
        return iter(self)
    
    def values(self):
        class keyIterator:
            def __init__(self,entriesHis):
                self.idx = 0
                self.lstOfKeys = [b for a,b in entriesHis]
            def __next__(self):
                if self.idx == len(self.lstOfKeys):
                    raise StopIteration
                returnNextItem = self.lstOfKeys[self.idx]
                self.idx += 1
                return returnNextItem
            def __iter__(self):
                return self
        returnVal = keyIterator(self.entries)
        return returnVal
        pass
                
    def items(self):
        class tupleIterator:
            def __init__(self,entriesHistory):
                self.itemHist = [(a,b) for a,b in entriesHistory]
                self.idx = 0
            def __next__(self):
                if self.idx == len(self.itemHist):
                    raise StopIteration
                returnNextItem = self.itemHist[self.idx]
                self.idx += 1
                return returnNextItem
            def __iter__(self):
                return self
        returnVal = tupleIterator(self.entries)
        return returnVal
        pass
                
    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'
            
    def __repr__(self):
        return str(self)
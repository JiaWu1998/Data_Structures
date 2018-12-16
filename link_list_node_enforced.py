class LinkedList:
    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next  = next
    
    def __init__(self):
        self.head = LinkedList.Node(None) # sentinel node (never to be removed)
        self.head.prior = self.head.next = self.head # set up "circular" topology
        self.length = 0
        
        
    ### prepend and append, below, from class discussion
        
    def prepend(self, value):
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next.prior = self.head.next = n
        self.length += 1
        
    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n
        self.length += 1
            
            
    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self)
            if nidx < 0:
                nidx = 0
        return nidx
    
    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        item = self.head
        idxNorm = self._normalize_idx(idx)
        if idxNorm > self.length:
            raise IndexError 
        for x in range(idxNorm+1):
            item = item.next
            if x == idxNorm:
                item = item.val
            if (item == None) and (x == 0):
                raise IndexError
        return item
        pass

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        item = self.head
        idxNorm = self._normalize_idx(idx)
        if idxNorm > self.length:
            raise IndexError 
        for x in range(idxNorm+1):
            item = item.next
            if x == idxNorm:
                item.val = value
        pass
    
    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        item = self.head
        idxNorm = self._normalize_idx(idx)
        if idxNorm > self.length:
            raise IndexError 
        for x in range(idxNorm+1):
            item = item.next
        item.prior.next = item.next
        item.next.prior = item.prior
        self.length -= 1
        pass
        

    ### stringification ###
    
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        head = self.head
        returnStr = ''
        for x in range(self.length):
            head = head.next
            hasVal = str(head.val)
            if x != self.length-1:
                returnStr += (hasVal+', ')
            else:
                returnStr += hasVal
        returnStr = '{0}'+returnStr+'{1}'
        returnStr = returnStr.format('[',']')
        return returnStr
        pass
        
    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        head = self.head
        returnStr = ''
        for x in range(self.length):
            head = head.next
            hasVal = str(head.val)
            if x != self.length-1:
                returnStr += (hasVal+', ')
            else:
                returnStr += hasVal
        returnStr = '{0}'+returnStr+'{1}'
        returnStr = returnStr.format('[',']')
        return returnStr
        pass


    ### single-element manipulation ###
        
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        assert(isinstance(idx, int))
        target = self.head
        idxNorm = self._normalize_idx(idx)
        if idxNorm > self.length:
            raise IndexError 
        for x in range(idxNorm):
            target = target.next
        n = LinkedList.Node(value,prior=target.next.prior,next=target.next)
        n.prior.next = n.next.prior = n
        self.length += 1
        pass
    
    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        assert(isinstance(idx, int))
        idxNorm = self._normalize_idx(idx)
        if idxNorm+1 > self.length:
            raise IndexError
        target = self.head
        for x in range(idxNorm+1):
            target = target.next
        target.next.prior = target.prior
        target.prior.next = target.next
        self.length -= 1
        return target.val
        pass
    
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        target = self.head
        find = self.head
        full = 0
        for x in range(self.length):
            find = find.prior
            if find.val == value:
                target = find
            else:
                full += 1
        if full == self.length:
            raise ValueError
        target.prior.next = target.next
        target.next.prior = target.prior
        self.length -= 1
        pass
    

    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in order) as
        other. If other is not an LinkedList, returns False."""
        if isinstance(other,LinkedList) == False:
            return False
        if self.length != other.length:
            return False
        count = 0
        returnVal = False
        ownHead = self.head
        otherHead = other.head
        for x in range(self.length):
            ownHead = ownHead.next
            otherHead = otherHead.next
            if ownHead.val == otherHead.val:
                count += 1
        if count == self.length:
            returnVal = True
        return returnVal
        pass

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        target = self.head
        returnVal = False 
        for x in range(self.length):
            target = target.next
            if target.val == value:
                returnVal = True
        return returnVal
        pass


    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        return self.length
    
    def min(self):
        """Returns the minimum value in this list."""
        target = self.head.next
        item = target.val
        for x in range(1,self.length):
            target = target.next
            if item > target.val:
                item = target.val
        return item
        pass
    
    def max(self):
        """Returns the maximum value in this list."""
        target = self.head.next
        item = target.val
        for x in range(1,self.length):
            target = target.next
            if item < target.val:
                item = target.val
        return item
        pass
    
    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        if (isinstance(i,int) or isinstance(j,int)) == False:
            raise IndexError
        target = self.head
        returnVal = -1
        count = 0
        if j == None:
            full = 0
            for x in reversed(range(i,self.length)):
                full += 1
                target = target.prior
                count += 1
                if target.val == value:
                    returnVal = x
                    count -= 1
            if count == full:
                raise ValueError
        else:
            idxJ = self._normalize_idx(j)
            if idxJ > self.length-1:
                raise IndexError
            full = 0
            for x in reversed(range(i,self.length)):
                target = target.prior
                count += 1
                full += 1
                print(x)
                print(target.val)
                if (target.val == value) and x<idxJ:
                    count -= 1
                    returnVal = x
                    #plus 1 cause of the sentinial head
            if count == full:
                raise ValueError
        return returnVal
        pass
    
    def count(self, value):
        """Returns the number of times value appears in this list."""
        target = self.head
        count = 0 
        for x in range(self.length):
            target = target.next
            if target.val == value:
                count += 1
        return count
        pass

    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those 
        of other."""
        assert(isinstance(other, LinkedList))
        newlst = LinkedList()
        thisHead = self.head
        otherHead = other.head
        for x in range(self.length):
            thisHead = thisHead.next
            newlst.append(thisHead.val)
        for x in range(other.length):
            otherHead = otherHead.next
            newlst.append(otherHead.val)
        return newlst
        pass
    
    def clear(self):
        """Removes all elements from this list."""
        for x in reversed(range(self.length)):
            self.__delitem__(x)
        self.length = 0
        pass
        
    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        copyOf = LinkedList()
        thisHead = self.head
        for x in range(self.length):
            thisHead = thisHead.next
            copyOf.append(thisHead.val)
        return copyOf
        pass

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        for x in other:
            self.append(x)
        pass

            
    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        class IteratorType:
            def __init__(self,headNode,lengthOf):
                self.head = headNode
                self.idx = 0
                self.length = lengthOf
            def __next__(self):
                self.head = self.head.next
                if self.idx == self.length:
                    raise StopIteration
                else:
                    self.idx += 1
                return self.head.val
            def __iter__(self):
                return self
        returnVal = IteratorType(self.head,self.length)
        return returnVal
        pass
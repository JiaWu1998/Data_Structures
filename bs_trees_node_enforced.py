class BSTree:
    class Node:
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            
    def __init__(self):
        self.size = 0
        self.root = None
        
    def __getitem__(self, key):
        if self.__contains__(key):
            current = self.root
            found = False
            while(found == False):
                if current.key == key:
                    found = True
                if current.key < key:
                    current = current.right
                elif current.key > key:
                    current = current.left
            return current.val
        else:
            raise KeyError
        pass
    
    def __setitem__(self, key, val):
        if self.root == None:
            self.root = self.Node(key,val)
            self.size += 1
        else:
            current = self.root
            found = False
            while(found == False):
                if current.key == key:
                    found = True
                    current.val = val
                if current.key < key:
                    if current.right == None:
                        current.right = self.Node(key,val)
                        self.size += 1
                        found = True
                    else:
                        current = current.right
                else:
                    if current.left == None:
                        current.left = self.Node(key,val)
                        self.size += 1
                        found = True
                    else:
                        current = current.left
        pass
    
    def __delitem__(self, key):
        if self.__contains__(key):
            if not self.root.left and not self.root.right:
                hold = self.root
                self.root = None
                self.size -= 1
                return hold
            else:
                current = self.root
                found = False
                while(found == False):
                    if (current.left.key == key) or (current.right.key == key):
                        found = True
                    if current.key > key:
                        current = current.right
                    else:
                        current = current.left
                #current now stores the target before del target
                if current.right.key == key:
                    hold = current.right
                    if (current.right.right != None) and (current.right.left != None):
                        #case 1 right
                        current.right = None
                    elif (current.right.right == None) and (current.right.left == None):
                        #case 3 right
                        headNode = current.right
                        replaced = False
                        while(replaced == False):
                            if headNode.left != None:
                                headNode = headNode.left
                            else:
                                replaced = True
                        current.right.key = headNode.left.key
                        current.right.val = headNode.left.val
                        headNode.left = None
                    elif current.right.right != None:
                        #case 2 right
                        current.right = current.right.right
                    elif current.right.left != None:
                        #case 4 right
                        current.right = current.right.left
                    self.size -= 1
                    return hold
                else:
                    hold = current.left
                    if (current.left.right != None) and (current.left.left != None):
                        #case 1 left
                        current.right = None
                    elif (current.left.right == None) and (current.left.left == None):
                        #case 3 left
                        headNode = current.right
                        replaced = False
                        while(replaced == False):
                            if headNode.left != None:
                                headNode = headNode.left
                            else:
                                replaced = True
                        current.left.key = headNode.left.key
                        current.left.val = headNode.left.val
                        headNode.left = None
                    elif current.left.right != None:
                        #case 2 left
                        current.left = current.left.right
                    elif current.left.left != None:
                        #case 4 left
                        current.left = current.left.left
                    self.size -= 1
                    return hold
        else:
            raise KeyError
        pass
        
    def __contains__(self, key):
        if self.root == None:
            return False
        else:
            current = self.root
            while(current.key != key):
                if current.key < key:
                    current = current.right
                    if current == None:
                        return False
                elif current.key > key:
                    current = current.left
                    if current == None:
                        return False
            return True 
        pass
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        def iterGenerator(node):
            if node:
                yield from iterGenerator(node.left)
                yield node.key
                yield from iterGenerator(node.right)
        return iterGenerator(self.root)
        pass
    
    def keys(self):
        def keyGenerator(node):
            if node:
                yield from keyGenerator(node.left)
                yield node.key
                yield from keyGenerator(node.right)
        return keyGenerator(self.root)
        pass
    
    def values(self):
        def valGenerator(node):
            if node:
                yield from valGenerator(node.left)
                yield node.val
                yield from valGenerator(node.right)
        return valGenerator(self.root)
        pass

    def items(self):
        def itemGenerator(node):
            if node:
                yield from itemGenerator(node.left)
                yield (node.key,node.val)
                yield from itemGenerator(node.right)
        return itemGenerator(self.root)
        pass
        
    def pprint(self, width=64):
        """Attempts to pretty-print this tree's contents."""
        height = self.height()
        nodes  = [(self.root, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level < height-1:
                    nodes.extend([(None, level+1), (None, level+1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                if n.left or level < height-1:
                    nodes.append((n.left, level+1))
                if n.right or level < height-1:
                    nodes.append((n.right, level+1))
                repr_str += '{val:^{width}}'.format(val=n.key, width=width//2**level)
        print(repr_str)
    
    def height(self):
        """Returns the height of the longest branch of the tree."""
        def height_rec(t):
            if not t:
                return 0
            else:
                return max(1+height_rec(t.left), 1+height_rec(t.right))
        return height_rec(self.root)
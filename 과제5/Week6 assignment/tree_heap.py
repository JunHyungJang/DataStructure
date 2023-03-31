class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class TreeHeap:
    __slots__ = '_root', '_last', '_size'

    #-------------------- nonpublic
    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'
        def __init__(self, element,left,right,parent):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent
    
    def _swap(self, node1, node2):
        """Swap the elements at indices i and j of array."""
        # IMPLEMENT HERE
        node1._element, node2_element = node1._element, node2._element

    
    def _upheap(self, node):
        # IMPLEMENT HERE
        k = node
        while True:
            
            if k._element <k._parent._element:
                k._element,k._parent._element = k._parent._element, k._element
                k = k._parent
                if k == self._root:
                    break
            else:
                break

        
    def _downheap(self, node):
        k = node 
        while True:
            if k._left != None and k._right!= None:
                if k._left._element < k._right._element:
                    k._element, k._left._element = k._left._element, k._element
                    k = k._left
                else:
                    k._element, k._right._element = k._right._element, k._element
                    k = k._right
            elif k._right == None and k._left != None and k._element > k._left._element:
                k._element, k._left._element = k._left._element, k._element
                k = k._left
            else:
                break

    # #-------------------- public
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._root = None
        self._last = None
        self._size = 0

    def __len__(self):
        """Return the number of items in the priority queue."""
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def add(self, key):
        """Add a key to the priority queue."""
        self._size+=1
        if self._root == None:
            self._root = self._Node(key,None,None,None)
            self._last = self._root
            # self._last = Node(None,None,None,self._root.element)
            # self._left = self._last
        else:
            # add_place = self._last
            # print("element", self._last._element)
            
            while True:
                if self._last == self._root:
                    self._last._left = self._Node(key,None,None,self._last)
                    self._last = self._last._left

                    return
                elif self._last == self._last._parent._left:
                   
                    if self._last._parent._right == None:
                        self._last._parent._right = self._Node(key,None,None,self._last._parent)
                        self._last = self._last._parent._right
                        self._upheap(self._last)
                        
                        return
                    else: 
                        self._last = self._last._parent._right
                        break                                      
                elif self._last == self._last._parent._right:
                    if self._last._parent == self._root:
                        self._last = self._last._parent._left                 
                        break
                    else:
                        self._last= self._last._parent
                       
            # self._upheap(self._last)
            while True:
                if self._last == self._root:
                    break
                elif self._last._left == None:
                    self._last._left = self._Node(key,None,None,self._last)

                    self._last = self._last._left
                    self._upheap(self._last)

                    return
                elif self._last._left != None:
                    if self._last._right != None:
                        self._last = self._last._left
                    else:
                        self._last._right = self._Node(key,None,None,self._last)
                        self._last = self._last._right
                        self._upheap(self._last)
                        return
                else:
                    self._last = self._last._parent._right
            # print(self._last._element)

        # IMPLEMENT HERE

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap is empty')
        return self._root._element

    
    def remove_min(self):
        """Remove and return the minimum key.
        Raise Empty exception if empty.
        """
        # IMPLEMENT HERE
        if self._root == None:
            raise Empty("Heap is empty")
        self._size-=1
        value = self._root._element
        self._root._element = self._last._element
        

        if self._last == self._root:
            self._last = None
            self._root = None
            return value
        
        elif self._last == self._root._left:
            self._last = self._root
            self._root._left = None
            self._downheap(self._root)
            return value
        

        elif self._last == self._last._parent._right :
            self._last = self._last._parent._left
            self._last._parent._right = None
            self._downheap(self._root)
            return value
        
        elif self._last == self._last._parent._left:
            self._last._parent._left = None
            self._downheap(self._root)
            self._last = self._last._parent
            

        while True:
            if self._last == self._root._right:
                self._last = self._last._parent._left
                break
            elif self._last == self._root._left:
                self._last = self._root._right
                break
            if self._last == self._last._parent._right:
                self._last = self._last._parent._left
                break
            elif self._last == self._last._parent._left:
                self._last = self._last._parent
        while True:
           
            if self._last._left == None:
                break
            if self._last._right == None:
                self._last = self._last._left
                self._downheap(self._root)
                return value
            elif self._last._right != None:
                self._last = self._last._right

        return value 

    def display(self):
        self._display(self._root, 0)

    def _display(self, node, depth):
        if node == None:
            return

        if node._right != None:
            self._display(node._right, depth+1)
        label = ''
        if node == self._root:
            label += '  <- root'
        if node == self._last:
            label += '  <- last'
        print(f'{"    "*depth}* {node._element}{label}')
        if node._left != None:
            self._display(node._left, depth+1)

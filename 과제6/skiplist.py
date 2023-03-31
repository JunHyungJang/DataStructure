from collections import MutableMapping
import math, random

class SkipList(MutableMapping):
    # add additional slots as you need
    __slots__ = '_head', '_tail', '_n', '_height'   

    #------------------------------- nested _Node class -------------------------------
    class _Node:
        __slots__ = '_key', '_value', '_prev', '_next', '_below', '_above'

        """Lightweight composite to store key-value pairs as map items."""
        def __init__(self, k, v, prev=None, next=None, below=None, above=None):
            self._key = k
            self._value = v
            self._prev = prev
            self._next = next
            self._below = below
            self._above = above

        def __eq__(self, other):               
            if other == None:
                return False
            return self._key == other._key   # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)       # opposite of __eq__

        def __lt__(self, other):               
            return self._key < other._key    # compare items based on their keys

    def __init__(self):
        """Create an empty map."""
        self._head = self._Node(-math.inf, None, None, None, None, None)   # Head: the first node in a skip list
        self._tail = self._Node(math.inf, None, None, None, None, None)    # Tail: the last node in a skip list
        self._head._next = self._tail         # Initially, there's no item -> head is directly linked to the tail
        self._n = 0                              # Initially, there's no item, so _n = 0
        # print("adding start")
        self._height = 0

    def randN(self):
        k = 0
        while random.random() < 1/2:
            k+=1
        return k


    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        # current = self._head
        # lv = self._n

        h = self._height
        current = self._head
        while True:
            if h == 0 and current._next._key > k:
                raise Exception("KeyError")
            if  current._next._key == k:
                return current._next._value
            if  current._next._key > k:
                current = current._below
                h-=1
            elif current._next._key < k:
                current = current._next


   
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        # print("adding start")
        # self.show()
        
        
        h = self._height
        lv = self.randN()
        t = lv
        

        current = self._head
        # print("height",self._height)

        while True:
            if current._next._key == k:
                current = current._next
                while True:
                    current._value = v
                    if current._below == None:
                        return
                    else:
                        current = current._below
            if h == 0 and current._next._key > k:
                break
            if h >0 and current._next._key >k:
                # print("below")
                current = current._below
                h-=1
            else:
                current = current._next
     
        forward = current._next
        backward = current
        current = self._Node(k,v,backward,forward,None,None)
        backward._next = current
        forward._prev = current

        # making new list if in case
        if self._head._next != self._tail:
            new_head = self._Node(-math.inf, None, None, None, backward, None)   # Head: the first node in a skip list
            new_tail = self._Node(math.inf, None, None, None, forward, None)    # Tail: the last node in a skip list
            new_head._next = new_tail
            self._head._above = new_head
            self._tail._above = new_tail
            self._head = new_head
            self._tail = new_tail
            self._height+=1 
          

    


        #inserting with randomnum

        while lv>0:
            # finding backward, forward
            while True:
                if backward._above != None:
                    backward = backward._above
                    break
                else:
                    backward = backward._prev
            while True:
                if forward._above != None:
                    forward = forward._above
                    break
                else:
                    forward = forward._next

            prev_node = current
            current = self._Node(k,v,backward,forward,prev_node,None)
            prev_node._above = current
            backward._next = current
            forward._prev = current
            if self._head._next != self._tail:
                new_head = self._Node(-math.inf, None, None, None, backward, None)   # Head: the first node in a skip list
                new_tail = self._Node(math.inf, None, None, None, forward, None)    # Tail: the last node in a skip list
                new_head._next = new_tail
                self._head._above = new_head
                self._tail._above = new_tail
                self._head = new_head
                self._tail = new_tail
                self._height+=1 
        
            lv -=1

        self._n +=1
        self._height = max(self._height, t)
        # self.show()

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if n
        ot found)."""
        # print(self._n)
        current = self._head
        lv = self._height

        # print("delection")
        # print("firstcurrentkey",current._key)
        while True:
            if lv == 0 and current._next._key > k:
                raise Exception("KeyError")
            if  current._next._key == k:
                current = current._next
                break
            if  current._next._key > k:
                current = current._below
                lv-=1
            elif current._next._key < k:
                current = current._next
        
        # print("delkey", current._key)
        while True:
            # print(lv, current._key)

            if lv == 0:
                current._prev._next = current._next
                current._next._prev = current._prev
                current = None
                break
            else:
                # print(current._key)
                current._prev._next = current._next
                current._next._prev = current._prev
                current = current._below
                current._above = None
            
                lv -= 1
        
        while True:
            if self._head._below == None:
                break
            if self._head._below._next == self._tail._below:
                self._head = self._head._below
                self._tail = self._tail._below
                self._head._above = None
                self._tail._above = None
                self._height-=1
            else:
                break
        self._n -=1
        # self.show()




    def __len__(self):
        """Return number of items in the map."""
        return self._n

    def __iter__(self):                             
        """Generate iteration of the map's keys."""
        # hint: iterate over the base height (where the nodes that node._below is None)
        # self.show()
        lst = []
        current = self._head
        lv = self._height
        # print(lv)

        while  lv > 0:
            current = current._below
            lv -=1
        # print(current._next._key)
        while True:
            # print(current._next._key)
            if current._next._key == math.inf:
                break
            else:
                # print(current._next._key)
                yield current._next._key
                current = current._next
        return lst
        # go down all the way to the bottom

        # yield node._key while node._next is not having math.inf as the key

    def show(self):
        # print("show")
        current = self._head
        head = self._head
        while True :
            while True:
                print(current._key, end = " ")
                if current._next._key == math.inf:
                    print(current._next._key)
                    break
                else:
                    current = current._next
            if head._below == None:
                break
            else:
                current = head._below
                head = head._below
            

        
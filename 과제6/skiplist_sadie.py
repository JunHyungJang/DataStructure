from collections.abc import MutableMapping
import math, random

class SkipList(MutableMapping):
    # add additional slots as you need
    __slots__ = '_head', '_tail', '_n' , '_height'

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
        self._n = 0
        self._height = 0 # Initially, there's no item, so _n = 0
  
    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        x = self._head
        while True:
            if self._height ==0 and x._next._key > k :
                raise Exception("KEYERROR")
            if x._next._key > k :
                return x._next._value
            if x._next._key > k :
                x = x._below
                self._height -=1
            elif x._next._key < k: 
                x = x._next
            
   
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        
        x = self._head
        stack = 0
        new = self._Node(k, v, None, None, None, None)
        
            
        
        
        if self._head._below == None: #아무것도 없으면
            self.put(new,x, x._next)
            
            x = new
            
            while random.random()< 1/2:
                stack +=1
            
            print(stack)
        
            for i in range (stack):
                x._above = self._Node(k, v, None, None, None, None)
                self.updown(x._above, x)
                new_prev = self._Node(x._prev._key, x._prev._value, None, None, None, None)
                new_next = self._Node(x._next._key, x._next._value, None, None, None, None)
                self.put(x._above, new_prev, new_next) 
                self.updown(new_prev, x._prev) 
                self.updown(new_next, x._next)
                x = x._above
                

            new_head = self._Node(-math.inf, None, None, None, None, None)
            new_tail = self._Node(math.inf, None, None, None, None, None)
            new_head._next = new_tail
            new_tail._prev = new_head
            self.updown(new_head, x._prev)
            self.updown(new_tail, x._next)

            
            self._head = new_head
            self._tail = new_tail
            
            self._height = stack+ 2
            print('여기')
            
        else:
           
            x = self._head._below

    
            
            while x._next._below != None: #below가 존재한다면
                if new._key != x._next._key:
                    while new._key > x._next._key: #new 키가 더 크다면, 오른쪽으로 옮긴 후
                        x = x._next
                    x = x._below #내려감.
                if new._key == x._next._key:
                    x = x._next
                    while True:
                        x._value = new._value
                        if x._below == None:
                            return
                        else:
                            x = x._below

                    print('현재키,다음키',new._key, x._next._key)

            print('저기')
            print(new._key, x._next._key)
            
#below가 없을때                
            if new._key < x._next._key:
                self.put(new, x, x._next)
            

            elif new._key > x._next._key:
                while new._key > x._next._key: #작다면 x = x. next
                    x = x._next
                self.put(new, x, x._next)
                    
                self.show()
                return
            
            while random.random()< 1/2:
                stack +=1
            print(stack)
                                   
            if self._height >= stack + 2:
                for i in range (stack):
                    new._above = self._Node(k, v, None, None, new, None)                
                    self.updown(new._above, new)
                    bstep = new._prev
                    fstep = new._next
                    while bstep._above == None:
                        bstep = bstep._prev
                    
                    while fstep._above == None:
                        fstep = fstep._next
                    self.put(new._above, bstep._above, fstep._above)
                    new = new._above
            
            
            elif self._height < stack + 2: 
                for i in range (self._height - 1):
                    new._above = self._Node(k, v, None, None, new, None)                
                    self.updown(new._above, new)
                    bstep = new._prev
                    fstep = new._next
                    while bstep._above == None:
                        bstep = bstep._prev
                    
                    while fstep._above == None:
                        fstep = fstep._next
                        
                    self.put(new._above, bstep._above, fstep._above)
                    new = new._above

                for j in range (stack + 1 - self._height):
                    new._above = self._Node(k, v, None, None, None, None)
                    self.updown(new._above, new)
                    up_prev = self._Node(new._prev._key, new._prev._value, None, new._above, new._prev, None)
                    up_next = self._Node(new._next._key, new._next._value, new._above, None, new._next, None)
                    self.put(new._above, up_prev, up_next) 
                    self.updown(up_prev, new._prev) 
                    self.updown(up_next, new._next)
                    new = new._above
                

                new_head = self._Node(-math.inf, None, None, None, None, None)
                new_tail = self._Node(math.inf, None, None, None, None, None)
                new_head._next = new_tail
                new_tail._prev = new_head
                self.updown(new_head, new._prev)
                self.updown(new_tail, new._next)


                self._head = new_head
                self._tail = new_tail
                self._height = stack + 2
                
        self.show()
        
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""

    def __len__(self):
        """Return number of items in the map."""
        return self._n

    def __iter__(self):                             
        """Generate iteration of the map's keys."""
        # hint: iterate over the base height (where the nodes that node._below is None)
        
        node = self._head
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
                
    def put(self, new, bwd, fwd):
        new._prev = bwd
        new._next = fwd
        bwd._next = new
        fwd._prev = new
    
    def updown(self,up, down):
        up._below = down
        down._above = up
    
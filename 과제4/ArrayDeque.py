from xml.etree.ElementTree import TreeBuilder


class EmptyException(Exception):
   """Raised when the data structure is empty"""
#    print("deque is empty")
   pass

class Deque: # Space used: O(n)
    # Always start from initial capacity=2. Resize if needed.
    DEFAULT_CAPACITY = 2
    
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self._data = [None]*capacity
        self._size = capacity
        self._f = 0
        self._r = -1
        self._l = 0
        
    def __str__(self):
        print(f'DEQUE({len(self)}: {self._data} / {self._f}, {self._r}')

   
    @property
    # def N(self):
        # IMPLEMENT HERE
    def __len__(self): # O(1)
        return self._l
        # IMPLEMENT HERE
        # return self._r +1 + self._capacity_size - self._f + 1

    def is_empty(self): # O(1)
        # IMPLEMENT HERE
        return (self._r == -1)

    def add_first(self, e): # O(1)*
        # IMPLEMENT HERE
        if self._l == self._size:
            self._resize(self._size*2)
        
        if (self._r == -1 and self._f == 0):
            self._r = 0
            self._f = 0
        
        elif self._f == self._size-1:
            self._f = 0
        
        else:
            self._f +=1
        
        self._l+=1
        self._data[self._f] = e
        # print(self._data)
        # print("f,r", self._f, self._r)
        # print("addfirst",self._data)

    def first(self): # O(1)
        # IMPLEMENT HERE
        if self.is_empty():
            raise EmptyException("Deque is empty")
        return self._data[self._f]

    def delete_first(self):   # O(1)*
        # IMPLEMENT HERE
        k = 0
        # print(self._data)
        if self.is_empty():
            raise EmptyException("Deque is empty")
            
        
        # element 하나
        if self._f == self._r:
            k = self._data[self._f]
            self._data[self._f] = None
            self._f = 0
            self._r = -1
        # 0번쨰 index일때
        elif self._f == 0:
            k = self._data[self._f]
            self._data[self._f] = None
            self.f = self._size -1
        else:
            k = self._data[self._f]
            self._data[self._f] = None
            self._f -=1
        
        self._l -=1

        if self._l < self._size // 2:
            self._resize(self._size//2)    

        return k
        
        
    
    def add_last(self, e): # O(1)*
        # IMPLEMENT HERE
        # element 0
        if self._l == self._size:
            self._resize(self._size*2)
        
        if (self._r == -1):
            self._r = self._size-1
            self._f = self._size-1
        
        # element 1
        elif self._r == 0:
            self._r = self._size -1
        else:
            self._r -=1
        
        self._l +=1

        self._data[self._r] = e
        # print("f,r", self._f, self._r)
        # print("addlast", self._data)

    def last(self):
        # IMPLEMENT HERE
        if self.is_empty():
            raise EmptyException("Deque is empty")
        # print("f,r", self._f, self._r)
        # if self._r == self._l:
        #     return self._data[0]
        # else:
        return self._data[self._r]
    def delete_last(self):
        # IMPLEMENT HERE
        k = 0
        # print(self._data)
        if self.is_empty == True:
            raise EmptyException("Deque is empty")
            
        k = self._data[self._r]
        
        if self._r == self._f:
            
            self._data[self._r] = None
            self._r = -1
            self._f = 0
        elif self._r == self._size-1:
            self._data[self._r] = None
            self._r = 0
        else:
            self._data[self._r] = None
            self._r+=1

        
        self._l -=1

        if self._l < self._size // 2:
            self._resize(int(self._size//2))  

        return k
        
    # Use doubling strategy for resizing the buffer.
    def _resize(self, cap): # O(n)
        # IMPLEMENT HERE
        if self._size < cap:
            arr = [None]* cap
            flag = 0
            for i in range(self._size):
                if i == self._f :
                    # print("i",i)
                    arr[i] = self._data[i]
                    self._f = i
                    flag = i
                    break
                else:
                    arr[i] = self._data[i]
            j = 0
            for i in range(self._size-1,-1,-1):
                if i == flag:
                    self._r = len(arr)-1-j+1
                    break
                else:
                    arr[len(arr)-1-j] = self._data[i]
                j+=1
            
            self._size = cap
            self._data = arr
    
        else:
            # print("srhink")
            # print(self._data)
            # print(self._f, self._r)
            arr = [None] * cap
            j = 0
            for i in range(self._size):
                if self._data[i] == None:
                    pass
                else:
                    arr[j] = self._data[i]
                    if i == self._f:
                        self._f = j
                    if i == self._r:
                        self._r = j
                    j+=1
            # print(arr)
            self._size = cap
            self._data = arr
        
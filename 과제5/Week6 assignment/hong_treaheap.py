#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math


# In[18]:


class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class TreeHeap:
    __slots__ = '_root', '_last', '_size' 

    #-------------------- nonpublic
    
    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'
        def __init__(self, element, left, right, parent):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent
    
    def _swap(self, node1, node2):
        """Swap the elements at indices i and j of array."""
        # IMPLEMENT HERE
        node1._element, node2._element = node1._element, node2._element
        
    
    def _upheap(self, node):
        # IMPLEMENT HERE
        while True:
            
            if node._element <node._parent._element:
                node._element,node._parent._element = node._parent._element, node._element
                node = node._parent
                
                if node == self._root:
                    break
                    
            else:
                break
            
                
            
        
        
    def _downheap(self, node):
        # IMPLEMENT HERE
        while True:
            if node._left != None and node._right!= None:
                if node._left._element < node._right._element:
                    node._element, node._left._element = node._left._element, node._element
                    node = node._left
                    
                else:
                    node._element, node._right._element = node._right._element, node._element
                    node = node._right
                    
            elif node._right == None and node._left != None and node._element > node._left._element:
                node._element, node._left._element = node._left._element, node._element
                node = node._left
                
                
            else:
                break


    #-------------------- public
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
        n_stack=0
        r_stack =1
        l_stack =0 #내려갈때 편하려고 
        
        #####올라가는 과정#########
        self._size +=1
        
        if self._root == None: #아무것도 없을때
            self._root = self._Node(key,None,None,None)
            self._last = self._root
            

        elif self._last == self._root: #라스트가 root라면
            self._last._left = self._Node(key,None,None,self._last) ###@@@
            self._last = self._last._left
            self._upheap(self._last)

        
        
        elif self._last == self._last._parent._right: #last가 오른쪽일때
            if math.log2(self._size) % 1 == 0 :  #루트 씌운거 1로 나눴을때 나머지가 없이 떨어지면 2의 거듭제곱임. 
                while self._last != self._root: #루트까지 올라감
                    self._last = self._last._parent
                    n_stack +=1
                    
                if self._last == self._root: #루트까지 올라오면, 스택+!만큼 왼쪽으로 내려감
                    for i in range (n_stack):
                        self._last = self._last._left
                    self._last._left = self._Node(key, None, None, self._last) ###@@@
                    self._last = self._last._left
                    self._upheap(self._last)
                    return

                
            else: #루트로 안나눠 떨어졌을때    
                while self._last == self._last._parent._right: #마지막 노드가 그 parent의 오른쪽이라면, 돌아간다
                    self._last = self._last._parent
                    l_stack += 1

                self._last = self._last._parent



                    ######여기서부턴 내려가는 과정###########     
                for i in range(1):
                    self._last = self._last._right
                    

                if l_stack == 1:
                    self._last._left = self._Node(key,None,None,self._last)
                    self._last= self._last._left
                    
                elif l_stack > 1 :
                    for i in range(l_stack-1):
                        self._last = self._last._left           
                    self._last._left = self._Node(key,None,None,self._last)
                    self._last= self._last._left
                    
                self._upheap(self._last)
                return
                
                
                    
                            
        elif self._last == self._last._parent._left: #last가 왼쪽이라면
            self._last._parent._right = self._Node(key,None,None,self._last._parent)
            self._last = self._last._parent._right
            self._upheap(self._last)
            return 
        

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
        
        
        else:
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
           
            if self._last._left == None: ##@@@@
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


# 

# In[19]:


th = TreeHeap()
for i in range(7):
    th.add(7-i)
th.display()


# In[20]:


print(th.remove_min())
print(th.remove_min())
print(th.remove_min())

th.display()


# In[21]:


import random

sequence = list(range(10))
random.shuffle(sequence)


# In[22]:


print(sequence)


# In[23]:


# pq sort
th = TreeHeap()
for item in sequence:
    th.add(item)

sorted_sequence = []
while not th.is_empty():
    sorted_sequence.append(th.remove_min())


# In[24]:


print(sorted_sequence)


# In[ ]:





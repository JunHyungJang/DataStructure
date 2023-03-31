if self._n == 0:
            current = self._Node(k,v,self._head,self._tail,None)
            self._head._next = current
            self._tail._prev = current
        else:
            t = self._n
            current = self._head
            while True:
                if t == 0 and current._next._key > k:
                    break
                if t >0 and current._next._key > k:
                    current = current._below
                    t-=1
                else:
                    current = current._next

            forward = current._next
            backward = current
            current = self._Node(k,v,backward,forward,None)
            backward._next = current
            forward._prev = current
         

            lv = self.randN()
            # print(lv)
            # print("lv", lv)

            while lv>0:
                while True:
                    if backward._above != None:
                        backward = backward._above
                        break
                    if backward._key == -math.inf:
                        break
                    
                    else:
                        backward = backward._prev
                while True:
                    if forward._above != None:
                        forward = forward._above
                        break
                    if forward._key == math.inf:
                        break
                    
                    else:
                        forward = forward._next
                prev_node = current
                current = self._Node(k,v,backward,forward,prev_node,None)
                prev_node._above = current
             
                backward._next = current
                forward._prev = current
                

                lv -=1
        
        new_head = self._Node(-math.inf, None, None, None, None, None)
        new_tail = self._Node(math.inf, None, None, None, None, None)
        new_head._next = new_tail
        new_head._below = self._head
        new_tail._below = self._tail

        self._tail._above = new_tail
        self._head._above = new_head
        
        self._head = new_head
        self._tail = new_tail

        # print("final", self._head._below._next._key)

        self._n +=1
        # print("adding finish")
        # self.show()
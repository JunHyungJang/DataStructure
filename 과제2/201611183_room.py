class Room:
    # you should initialize all the required instance variables here
    # parameters:
    #   (integer) number: room number 
    #   (integer) bed_count: number of beds in the room (you can assume it's given always >0)
    def __init__(self, number, bed_count):
        # (integer) _number: Rm No. (= number)
        self._number = number
        
        # (integer) _bed_count: # of default bed in room (= bed_count)
        self._bed_count = bed_count
        
        # (list) _cllist: list for storing check-in clients in the room
        self._cllist = []
        
        # (integer) _numcl: # of check-in clients in the room. Same as len(_cllist)
        self._numcl = 0

    # this will be called when string representation is required
    # return: (string) with the following formatting 
    #         'Room number {room number}, occupancy {currently occupied beds}/{total beds}'
    #          example return str: 'Room number 101, occupancy 2/2'
    def __str__(self):
        return 'Room number {0}, occupancy {1}/{2}'.format(self._number, self._numcl, self._bed_count)

    # return: (integer) room number 
    def get_number(self):
        return self._number
    
    # return: (integer) number of beds in the room
    def get_bed_count(self):
        return self._bed_count

    # return: (integer) number of empty bed remaining in the room
    def available(self):
        # current availability = # of total bed - # of occupied bed (= # of check-in clients)
        return (self._bed_count - self._numcl)

    # parameters:
    #   client_name: a name of client who's willing to check in to the room
    # return: (bool)
    #   True  if there was an empty bed, and the client occupies the bed
    #   False if the room was already full
    def check_in(self, client_name):
        # check whether there is any available bed
        # i.e. # of check-in is under limit
        if self._numcl < self._bed_count:
            self._cllist.append(client_name)
            self._numcl += 1
            return True
        else:
            return False

    # parameters:
    #   client_name: a name of client who's willing to check out from the room
    # return: (bool)
    #   True  if the client is actually checked in the room, and checked out successfully
    #   False if the client is nonexisting in the room
    def check_out(self, client_name):
        # check whether there is 'client_name' in _cllist
        if client_name in self._cllist:
            self._cllist.remove(client_name)
            self._numcl -= 1
            return True
        else:
            return False

    # return: (string) 'Empty' if the room is empty, 
    #                  or a string which lists the clients in the room (separated by ', ')
    #                  -> ex: "clinet1, client2, client3"
    def get_clients(self):
        if self._numcl == 0:
            return 'Empty'
        else:
            output = ', '.join(self._cllist)
            return output
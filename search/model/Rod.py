
#from Rod_C import compare_rods3_cython
"""
class which represent a goal_rod. It represents disks assigned to the road with a stack
"""
class Rod:
 
    #Constructor
    def __init__(self):
        self.__stack = []
    
    def hasDisk(self):
        return len(self.__stack) > 0

    #Add Disk
    def addDisk(self, disk):
        self.__stack.append(disk)

    #Rem Disk
    def remDisk(self):
        return self.__stack.pop() if self.__stack else None
    
    def getLast(self):
            return self.__stack[-1]
    
    def getStack(self):
            return self.__stack
    
    def __eq__(self, other) -> bool:

        if(len(self.__stack) != len(other.__stack)):
            return False

        for i in range(len(self.__stack)):
            if(self.__stack[i] != other.__stack[i]):
                return False
            
        return True
    
    def stackLen(self):
        return len(self.__stack)
    
    def getEuristicRod(self):

        value = 0
        cont = 10

        for d in self.__stack:
            if d is not None:
                value += d[1] * cont
            cont-=cont

        return value
    

    def toString(self):
        return str(self.__stack)
    
    
    def compareRods(self, goal_rod):
        min_ = min(self.stackLen(), goal_rod.stackLen())
        return sum(
            self.__stack[i] != goal_rod.getStack()[i]
            for i in range(min_)
        )
     

    def compareRods2(self, goal_rod):  
        h = 0
        my_len = self.stackLen()
        other_len = goal_rod.stackLen()
        other_stack = goal_rod.getStack()
        min_ = min(my_len, other_len)
        h =  sum(
            self.__stack[i] != other_stack[i]
            for i in range(min_)
        )
        
        d = my_len - other_len
        if( (d) > 0):
            h += d 

        
        return h

#====================================================================================================    

    def compareRods3_(self,goal_rod, rod_num, c ,max_d):
        h = 0
        if(self.stackLen()==0):
            return 0
        
        stack = self.__stack
        goal_stack = goal_rod.__stack
        my_len = self.stackLen()
        other_len = goal_rod.stackLen()
        
        #se si è sul terzo rod
        if(rod_num==2):
            for i in range(my_len):
                if(stack[i][0] == 2):
                    h+=1
                else:
                    h += stack[i][0]

        #primo o secondo rod
        
        else:
            min_len = min(my_len, other_len)
            for i in range(min_len):
                if stack[i] != goal_stack[i]:
                    if(stack[i][0] == 2):
                        h+=1
                    else:
                        h += stack[i][0]

            if my_len > other_len:
                for i in range(other_len, my_len):
                    if(stack[i][0] == 2):
                        h+=1
                    else:
                        h += stack[i][0]

            if(stack[0][0] == max_d and stack[0][1] != c[rod_num]):
                h += 3
        
        if(my_len>=2 and h>1):
            if(stack[my_len-1][0] == stack[my_len-2][0]):
                h = h-1

        
        return h
    
    #def compareRods3C(self, goal_rod, rod_num):
       #return compare_rods3_cython(self.__stack,goal_rod.__stack,rod_num)
    
#====================================================================================================
    def compareRods4(self, goal_rod, rod_num):  
        h = 0
        my_len = self.stackLen()
        other_len = goal_rod.stackLen()
        
        if(rod_num == 2):
            h = h + (my_len)
        else:
            h = self.calc_h12(goal_rod, h, my_len, other_len)

        return h

    def calc_h12(self, goal_rod, h, my_len, other_len):
        done = False
        min_len = min(my_len, other_len)
        
        for i in range(min_len):
            d = self.__stack[i]
            if d!= goal_rod.__stack[i]:
                h = h + 1+ 2*(my_len-i-1)
                done = True
                break

        if(not done and my_len > other_len):
            h = h +  2*(my_len-other_len)
  
        return h
#====================================================================================================

#====================================================================================================
    def sameDisks(self):
        s = 0
        ub = len(self.__stack) - 1 
        for i in range(0, ub ):
            if(self.__stack[i][1] == self.__stack[i+1][1]):
                s += 1
        return s

    def rodClone(self):
        clone = Rod()
        clone.__stack = [*self.__stack]
        return clone
    





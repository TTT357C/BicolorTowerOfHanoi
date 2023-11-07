from model.Rod import Rod


class TowerCreation:

    def createTower(self, base, secondo, numD):
        result = Rod()

        for i in range(numD):
            if(i % 2==0):
                result.addDisk((numD - i, base))
            else:
                result.addDisk((numD - i, secondo))
            
        return result
    
    def createSingleBase(self,base,numD):
        result = Rod()

        result.addDisk((numD, base))
            
        return result
    
    def createTowerWithoutTop(self, base, secondo, numD):
        result = Rod()

        for i in range(numD):
            if(i % 2==0):
                result.addDisk((numD - i, base))
            else:
                result.addDisk((numD - i, secondo))

        result.remDisk()
            
        return result
    
    def createTop(self, base, numD):
        result = Rod()

        result.addDisk((base, 1))
            
        return result
    
    #crea torre centrale del primo subgoal
    def createBigTower(self, base, secondo, numD):
        result = Rod()
        cont = 0
        cont2 = 1
        cont_d = numD

        result.addDisk((cont_d, base))
        cont_d-=1
        result.addDisk((cont_d, secondo))

        boo = True

        for i in range(numD+numD-3):

            if boo:
                result.addDisk((cont_d, base))
            else:
                result.addDisk((cont_d, secondo))

            if(cont2 == 1):
                cont_d-=1
                cont2 = 0

            if(cont != 1):
                cont+=1
            else:
                cont = 0
                cont2+=1
                boo = not boo

        return result
    
    def createBigEndTower(self, base, secondo, numD):
        result = Rod()
        cont = 0
        cont2 = 1
        cont_d = numD

        result.addDisk((cont_d, base))
        cont_d-=1
        result.addDisk((cont_d, base))

        boo = [False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False]

        for i in range(numD+numD-3):

            if boo[i]:
                result.addDisk((cont_d, base))
            else:
                result.addDisk((cont_d, secondo))

            if(cont2 == 1):
                cont_d-=1
                cont2 = 0

            if(cont != 1):
                cont+=1
            else:
                cont = 0
                cont2+=1
                
        return result
    
    def createBigEndTower2(self, base, secondo, numD):
        result = Rod()
        cont = 0
        cont2 = 1
        cont_d = numD

        result.addDisk((cont_d, base))
        cont_d-=1
        result.addDisk((cont_d, secondo))

        boo = [True,False,True,False,True,False,True,False,True,False,True,False,True,False]

        for i in range(numD+numD-3):

            if boo[i]:
                result.addDisk((cont_d, base))
            else:
                result.addDisk((cont_d, secondo))

            if(cont2 == 1):
                cont_d-=1
                cont2 = 0

            if(cont != 1):
                cont+=1
            else:
                cont = 0
                cont2+=1
                
        return result
    
    def createBigMiddleTower(self, base, secondo, numD):
        result = Rod()
        cont = 0
        cont2 = 1
        cont_d = numD

        result.addDisk((cont_d, base))
        cont_d-=1
        result.addDisk((cont_d, secondo))

        boo = [True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False]

        for i in range(numD+numD-3):

            if boo[i]:
                result.addDisk((cont_d, base))
            else:
                result.addDisk((cont_d, secondo))

            if(cont2 == 1):
                cont_d-=1
                cont2 = 0

            if(cont != 1):
                cont+=1
            else:
                cont = 0
                cont2+=1
                
        return result
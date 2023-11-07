class scriviInitPDDL:
    '''
    file = open('C:/AI_PDDL_study/pythonPDDL/prova.txt', mode = 'a' , encoding='utf-8')
    file.write("ciao\n")
    file.write("ciao\n")
    file.write("ciao!")
    
    file.close()   
    print("scriviPDDL")
    '''

    domain_file_path = ""
    file = None
    col1 = None
    col2 = None

    def __init__(self, path_domain, col1, col2) -> None:
        self.domain_file_path = path_domain
        self.file = open(self.domain_file_path, mode = 'a' , encoding='utf-8')
        self.col1 = col1
        self.col2 = col2

    def close(self):
        self.file.close()

    #scrive linea definizione dominio e blocco di requisiti del file
    def define(self, problem_name, domain_name):
        stringa= "(define (problem "+problem_name+") (:domain "+domain_name+")\n"
        return stringa
       
#---------------------------------------------------------------------------
    #scrive blocco dei tipi
    def write_objects(self, num_disk, num_rods):
        stringa = ""
        stringa +="(:objects\n"

        #rod--------------------------------
        stringa +="\t"
        for i in range(0, num_disk):
            stringa +=self.col1+str(i+1)+" "
        
        for i in range(0, num_disk):
            stringa +=self.col2+str(i+1)+" "
        
        stringa +="- disk\n"

        #disk-------------------------------
        stringa +="\t"
        for i in range(0, num_rods):
            stringa +="rod"+str(i+1)+" "
        stringa +="- rod\n"
        stringa +="\th - hand\n"
        stringa +=")\n"
        
        return stringa

#---------------------------------------------------------------------------
    def write_located_cond(self, num_disk, col1, col2):
        #rod1 located-------------------------------------------------
        stringa = "\t"
        for i in range(0, num_disk):
            if (i%2==0):
                stringa +="(located "+col1+str(i+1)+" rod1) "
            else:
                stringa +="(located "+col2+str(i+1)+" rod1) "  
        
        stringa +="\n"
        stringa +="\t"

        #rod2 located-------------------------------------------------
        for i in range(0, num_disk):
            if (i%2==0):
                stringa +="(located "+col2+str(i+1)+" rod2) "
            else:
                stringa +="(located "+col1+str(i+1)+" rod2) "

        stringa +="\n"
        return stringa
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------   
    def write_num_disk_cond(self, num_rods, num_disk):
        stringa ="\t"
        for i in range(1, 3):
            stringa +="(=(disks_number rod"+str(i)+")"+str(num_disk)+") "
        
        stringa +="\n\t"
        
        for i in range(3, num_rods+1):
            stringa +="(=(disks_number rod"+str(i)+")0) "
        
        stringa +="\n"
        return stringa
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------   
    def write_on_cond(self, num_disk, col1, col2):
        stringa = ""
        stringa +="\n\t"
        j = 0
        for i in range(1, num_disk):
            if(j%2 == 0):
                stringa +="(on "+col1+str(i)+" "+col2+str(i+1)+")"
            else:
                stringa +="(on "+col2+str(i)+" "+col1+str(i+1)+")"
            j = j+1
        
        stringa +="\n\t"

        j = 0
        for i in range(1, num_disk):
            if(j%2 == 0):
                stringa +="(on "+col2+str(i)+" "+col1+str(i+1)+")"
            else:
                stringa +="(on "+col1+str(i)+" "+col2+str(i+1)+")"
            j = j+1

        stringa +="\n"
        return stringa
#---------------------------------------------------------------------------   

#---------------------------------------------------------------------------   

    #scrive i predicati di smaller tra i dischi dati i due colori e il numero di dischi
    def write_smaller_condition(self, num_disk, color, othercolor):
        stringa = "\n\t"
        for i in range(1, num_disk):
            for j in range(i+1, num_disk+1):
                stringa += "(smaller "+color+str(i)+" "+othercolor+str(j)+")"
                stringa += "(smaller "+color+str(i)+" "+color+str(j)+")"
            stringa += "\n\t"

            for j in range(i+1, num_disk+1):
                stringa += "(smaller "+othercolor+str(i)+" "+color+str(j)+")"
                stringa += "(smaller "+othercolor+str(i)+" "+othercolor+str(j)+")"
            stringa += "\n\t"
        
        return stringa
#---------------------------------------------------------------------------  
 
#---------------------------------------------------------------------------  
   
    #scrive i predicati di smaller tra i dischi dati i due colori e il numero di dischi
    def write_equals_condition(self, num_disk, color, othercolor):
        stringa = "\n\t"
        for i in range(1, num_disk+1):
            stringa += "(equal "+color+str(i)+" "+othercolor+str(i)+")"
            
            #stringa += "\n\t"

            stringa += "(equal "+othercolor+str(i)+" "+color+str(i)+")"

            if(i<num_disk):
                stringa += "\n\t"
        
        return stringa
#--------------------------------------------------------------------------------------

    def write_initial_state(self,p_name, d_name, num_disk, num_rods):
        self.file.truncate(0)
        
        lines = []

        lines.append(self.define(p_name, d_name))
        lines.append(self.write_objects(num_disk, num_rods))

        lines.append("(:init\n")
        lines.append("\t(clear r1) (clear w1) \n")
        
        #located-------------------------------------------------
        lines.append(self.write_located_cond( num_disk, self.col1, self.col2))

        #num_disk------------------------------------------------
        lines.append(self.write_num_disk_cond(num_rods, num_disk))

        #on conditions-------------------------------------------
        lines.append(self.write_on_cond(num_disk, self.col1, self.col2))

        #smaller condition---------------------------------------
        lines.append(self.write_smaller_condition(num_disk, self.col1, self.col2))

        lines.append(self.write_equals_condition(num_disk, self.col1, self.col2))

        lines.append("\n)")
            
        self.define(p_name, d_name)  
        self.write_objects(num_disk, num_rods) 

        self.file.writelines(lines)
        self.file.close()

   

 


""" s = scriviInitPDDL('C:/AI_PLUS/initTest.txt',"r","w")
num_disk = 3
num_rods = 3
p_name = "move_r"+str(num_disk)+"_to_goal"
d_name = "hanoi"

s.write_initial_state(p_name, d_name, num_disk, num_rods)

s.close() """

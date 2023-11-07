class scriviGoalPDDL:

    domain_file_path = ""
    file = None
    num_disk = 0
    num_rods = 0
    col1 = None
    col2 = None
#-----------------------------------------------------------------------------------------------------
    def __init__(self, path_domain, num_disk, num_rods, col1, col2) -> None:
        self.domain_file_path = path_domain
        self.file = open(self.domain_file_path, mode = 'a' , encoding='utf-8')
        self.num_disk = num_disk
        self.num_rods = num_rods
        self.col1 = col1
        self.col2 = col2
#------------------------------------------------------------------------------------------------------  
#-----------------------------------------------------------------------------------------------------
    def write_located_cond(self):
        #rod1 located-------------------------------------------------
        stringa = "\t"
        for i in range(0, self.num_disk):
            stringa += "(located "+self.col1+str(i+1)+" rod1) "

        stringa += "\n\t"

        #rod2 located-------------------------------------------------
        
        for i in range(0, self.num_disk):
            stringa += "(located "+self.col2+str(i+1)+" rod2) "

        stringa += "\n"
        stringa += "\n"

        return stringa  
#------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------   
    def write_num_disk_cond(self):
        stringa ="\n\t"
        for i in range(1, 3):
            stringa +="(=(disks_number rod"+str(i)+")"+str(self.num_disk)+") "
        
        stringa +="\n\t"
        
        for i in range(3, self.num_rods+1):
            stringa +="(=(disks_number rod"+str(i)+")0) "
        
        stringa +="\n"
        return stringa
#---------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
    def write_clear_cond(self, colors):
        stringa = ""
        
        for i in colors:
            stringa += "\t(clear "+i+"1) \n"

        stringa += "\t"

        for c in colors:
            for i in range(2, self.num_disk+1):
                stringa += "(not(clear "+c+str(i)+")) "
            
            stringa += "\n\t"

        #stringa+="\n"
        return stringa
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
    def write_on_cond(self, col1, col2):
        stringa ="\n\t"
        
        for i in range(1, self.num_disk):
            stringa +="(on "+col1+str(i)+" "+col1+str(i+1)+") "
           
        stringa +="\n\t"

        for i in range(1, self.num_disk):
            stringa +="(on "+col2+str(i)+" "+col2+str(i+1)+") "

        stringa +="\n"
        return stringa
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
    def write_goal_state(self):
        #self.file.truncate(0)
        lines = []
        colors = []
        colors.append(self.col1)
        colors.append(self.col2)

        lines.append( "\n(:goal (and\n" )
        lines.append( self.write_located_cond( ))
        lines.append(self.write_num_disk_cond())
        lines.append( self.write_clear_cond(colors) )
        lines.append( self.write_on_cond(self.col1, self.col2) )
        lines.append("\t(not(handfull h))\n")
        lines.append("\t(forall (?d - disk) (not(toAllocate ?d)) )\n")

        lines.append("))")
        lines.append("\n)")


        self.file.writelines(lines)
        self.file.close()

    

""" dischi = 6#int(input("dischi: "))
rods = 5#int(input("rod: "))
s = scriviGoalPDDL('C:/AI_PDDL_study/pythonPDDL/goalTest.txt', dischi, rods, "w", "r")
s.write_goal_state() """

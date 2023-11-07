import numpy as np

cpdef int heutristicCalc(s_rods, g_rods, max_d, c):

    cdef int i
    cdef int j
    cdef int summ = 0
    cdef int mindim = len(s_rods)

    for i in range(mindim):

        summ+=compare_rods3_cython(s_rods[i], g_rods[i], i, max_d, c, (mindim-1))

    return summ


cpdef int compare_rods3_cython(s_rod, goal_rod, int rod_num, int max_d, c, int mindim):
    cdef int h = 0
    cdef int i = 0
    cdef minrod = mindim - 2
    cdef int my_len = len(s_rod._Rod__stack)
    cdef int other_len = len(goal_rod._Rod__stack)
    cdef int min_len = min(my_len, other_len)

    if my_len == 0:
        return 0

    cdef list stack = s_rod._Rod__stack
    cdef list goal_stack = goal_rod._Rod__stack

    if rod_num > 1:
        for i in range(my_len):
            if stack[i][0] < mindim :
                h += 1
            else:
                h += stack[i][0]
    else:
        for i in range(min_len):
            if stack[i] != goal_stack[i]:
                if stack[i][0] < mindim :    
                    h += 1
                else:     
                    h += stack[i][0]

        if my_len > other_len:
            for i in range(other_len, my_len):
                if stack[i][0] < mindim :
                    h += 1
                else:   
                    h += stack[i][0]

        if minrod == 0:
            if stack[0][0] == max_d and stack[0][1] != c[rod_num]:
                h += 3
            
    return h



cpdef aP_C(mat_a, max_d, rods):
        
    mat = np.array(mat_a)
    cdef int l = len(rods)

    for i in range(l):
        for j in range(l):
            if(i<j):
                '''lp = LineProfiler()
                lp_wrapper = lp(self.__aPCalculation)
                lp_wrapper(mat, i, j, max_d)
                lp.print_stats()'''
                __aPCalculation1(mat, i, j, max_d, rods) 

    return mat
    
cpdef aPRulesCalculation(mat, action):
    mat[action.j, action.i] = 0
    return mat


cpdef __aPCalculation1(mat, i, j, max_d, rods):
    
    #check if the node is empty
    if rods[i].hasDisk():
        if rods[j].hasDisk():

            if(rods[i].getLast()[0] == rods[j].getLast()[0]):
                boo = 0
            elif rods[i].getLast()[0] > rods[j].getLast()[0]:
                boo = 1
            else:
                boo = -1

            if boo==1:
                mat[i, j] = 0
            if boo==-1:
                mat[j, i] = 0
            if (rods[i].stackLen() == 1 and rods[j].stackLen() == 1) and (rods[i].getLast()[0] == max_d and rods[j].getLast()[0] == max_d):
                mat[i, j] = 0
                mat[j, i] = 0
        else:
            mat[j, i] = 0
    else:
        mat[i, j] = 0
    if not rods[j].hasDisk():
        mat[j, i] = 0
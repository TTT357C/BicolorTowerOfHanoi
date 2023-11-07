
def cleanSolution(result):

    tokens = result.split("\n")
    solution = ""
    j = 0
    for i in range(len(tokens)):
        s = tokens[i]
        
        if "put" in s:
            j += 1
            x = s.split(":")
            solution += str(j)+": "+x[1]+"\n"
    
    return solution


""" f = open("C:\\Users\\paolo\\OneDrive\\Desktop\\mosse4.txt", "r")
solution = (f.read())
f.close()
print(cleanSolution(solution)) """

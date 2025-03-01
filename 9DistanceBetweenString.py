import numpy as np
def Levenshetein(s1,s2):
    if s1 =="":
        return len(s2)
    if s2 =="":
        return len(s1)
    if s1[-1]== s2[-1]:
        cost = 0
    else :
        cost = 1
    res = min([Levenshetein(s1[:-1], s2)+1,
            Levenshetein(s1,s2[:-1])+1,
            Levenshetein(s1[:-1],s2[:-1])+ cost])
    return res
print(Levenshetein("excution", "intenstion"))

import random
def isNumber(someString):
    for i in range(0,len(someString)):
        if(not(someString[i] in "0123456789.")):
            return False
    return True

def chance(percent):
    if(random.random() * 100 < percent):
        return True
    else:
        return False

def pickOccupation(dic):
    lastKey = None
    for key in dic:
        if((not (isinstance(dic[key], basestring))) and (dic[key] != "Total" and key != "Total")):
            if(chance(dic[key])):
                return key
        lastKey = key
    return lastKey

def toDictionary(file):
    file = open(file,"r")
    dic = {}
    for line in file:
        length = len(line)
        inQuote = False
        lineEnd = None
        splitIndex = None
        for i in range(0,length):
            if(line[i] == '"'):
                inQuote = not inQuote
            elif((not inQuote) and line[i] == ','):
                splitIndex = i
                break
        i = -1
        while(i <= len(line)):
            if(line[i] == '\r' or line[i] == '\n'):
                lineEnd = i
            else:
                break
            i -= 1
        if(isNumber(line[splitIndex + 1:lineEnd])):
            dic[line[0:splitIndex]] = float(line[splitIndex + 1:lineEnd])
        else:
            dic[line[0:splitIndex]] = line[splitIndex + 1 : lineEnd]
    return dic
dic = toDictionary("occupations.csv")
print dic
print "--------------------------------------------"
print pickOccupation(dic)

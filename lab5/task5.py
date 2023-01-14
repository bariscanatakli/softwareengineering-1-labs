import string
import random

alphabetList, identifyOfNurses = list(string.ascii_lowercase), list()

for number in range(len(alphabetList)):
    print(number)
    nurseShift = random.randint(1,24)
    identifyOfNurses.append({"ID":number,"Ending Time" :nurseShift ,"Name":alphabetList[number]})

def getNurse():
    endingTimeList = list()
    for nurse in identifyOfNurses:
        endingTimeList.append((nurse['Ending Time'],nurse["ID"]))
    endingTimeList.sort()
    
    for index in range(1,len(endingTimeList)):
        
        if index == len(endingTimeList) -1:
            difference1 = endingTimeList[-index][0] - endingTimeList[-index-1][0]
            endingTimeList[-index] = difference1
            print(index+1)
            difference = endingTimeList[-index][0] - endingTimeList[-index-1][0]
            endingTimeList[-index] = difference
             
        else:
            difference = endingTimeList[-index][0] - endingTimeList[-index-1][0]
            endingTimeList[-index] = difference
    print(endingTimeList)
    
getNurse()
initialList = [0,0,1]
k = 13
counter = 0
def tribonacciFunc(initialList):
    global counter
    first,second,third = initialList[counter],initialList[counter+1],initialList[counter+2]
    if counter == k-2:
        print(initialList)
    else:
        counter +=1
        summation = first+second+third
        initialList.append(summation)
        tribonacciFunc(initialList)
tribonacciFunc(initialList)
givenList = [4,4,4,2,3,2,1,1] # can be changed

numbers = set(x for x in givenList) # i use for getting the numbers at the one time

dictOfNumbers = {number: None for number in numbers} # its like {1:None,2:None,...}

occurNumbers = [] # the numbers for occurency

for key in dictOfNumbers:
    dictOfNumbers[key] = givenList.count(key) # {1:2,2:3,3:10} maybe
    occurNumbers.append(givenList.count(key)) # adding the occurence numbers to list
 
numbers = [] # the list that we want to order

while len(occurNumbers) > 0:
    minValue = min(occurNumbers) # getting the min value of numbers which is occuring
    for key,value in dictOfNumbers.items(): #getting as (1,2)  (3,1) so on
        if value == minValue: #if it is equal get the value and append to numbers as key
            numbers.append(key)
            occurNumbers.remove(minValue) # and remove the minValue and so on
print(numbers)

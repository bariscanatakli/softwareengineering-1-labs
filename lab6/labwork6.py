# we will create a function that can evolve itself respect to given algorithm method
parameterList1 = [123,1234,221,4412,5,5]
parameterList2 = [123,221,123444,4412,51,5,111]
dictionary = {"asda":13,"pss":1111,"qqww":511,"qqwwa":15,"qqwwq":16,"qqwws":17,"asdaq":13,"psss":1111,"qqwwa":511,"qxqwwa":15,"qqewwq":16,"qqwqws":17}

def primeSort(given):
    A = []
    B = []
    counter = 0
    isAsal = False
    for x in given:
        if counter > 2:
            for y in range(2,counter):
                if counter%y != 0:
                    isAsal = True
                else:
                    isAsal = False
        counter += 1
        if isAsal:
            A.append(x)
        else:
            B.append(x)
    return selection_sort((A,B))
def repeteadSet(given):
    liste = []
    for value in given:
        if given.count(value) > 1:
            if value not in liste:
                liste.append(value)
    return selection_sort(liste)
            
def reverseList(given):
    liste = []
    for k in range(1,len(given)+1):
        liste.append(given[-k])
    return selection_sort(liste)


def selection_sort(list):
    print(list)
    
primeSort(dictionary)
repeteadSet(parameterList1)
reverseList(parameterList2)
import pandas as pd

inputs = open("input.txt", "r").readlines()


xList = list()
yList = list()
messageList = list()

for line in inputs:
    line = line.split("  ")[0].split("\t")
    xList.append(line[0])
    yList.append(line[1])
    messageList.append(line[2].removesuffix("\n"))

inputDict = {"X": xList, "Y": yList, "Messages": messageList}

print(pd.DataFrame(inputDict))

# print(pd.DataFrame(inputs))
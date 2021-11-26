import sys


#sys.stdin = open("moobuzz.in", "r")
#sys.stdout = open("moobuzz.out", "w")

N = int(input())

roster = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", 
"Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]


info = []


for i in range(N):
    sentences = input().split(' ')
    info.append([sentences[0], sentences[3], sentences[4], sentences[7]])

elsieLocation = 0
relativeName = ""

importantInfo = []

for i in range(N):
    if info[i][0] == "Elsie":
        elsieLocation = i
        relativeName = info[i][3]
        importantInfo.append([info[i][1], info[i][2]])

#print(relativeName)
#Tracing purposes

#A[][0] = name
#A[][1] = negative/positive
#A[][2] = which year
#A[][3] = previous name

bessieFound = False

while (not bessieFound):
    for i in range(N):
        if info[i][0] == relativeName:
            if info[i][3] == "Bessie":
                bessieFound = True
                importantInfo.append([info[i][1],info[i][2]])
                break

            relativeName = info[i][3]
            importantInfo.append([info[i][1], info[i][2]])
            #print(relativeName)
            #tracing

importantInfo.append(["Random", "Ox"])
pathLen = len(importantInfo)
totalDifference = 0
print(importantInfo)
for j in range(pathLen):
    currentYear = roster.index(importantInfo[pathLen - j - 1][1])
    nextYear = roster.index(importantInfo[pathLen - j - 2][1])
    if importantInfo[pathLen - j - 2][0] == 'previous':
        if (nextYear > currentYear):
            totalDifference -= currentYear
            currentYear = 12
        totalDifference -= (currentYear - nextYear)
    if importantInfo[pathLen - j - 2][0] == 'next':
        if (nextYear < currentYear):
            totalDifference += (12 - currentYear)
            currentYear = 0
        totalDifference += (nextYear - currentYear)

print (abs(totalDifference))
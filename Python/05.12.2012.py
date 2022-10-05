import random
#---------------------------------------------------------------------------
someList = [random.randint(0, 10) for i in range(random.randint(7, 15))]
max = 0
print(someList)
for elem in range(len(someList) - 2):
    if(someList[elem]+someList[elem+1]+someList[elem+2] > max):
        max = someList[elem]+someList[elem+1]+someList[elem+2]
for elem in range(len(someList) - 2):
    if(someList[elem]+someList[elem+1]+someList[elem+2] == max):
        print("Три последовательных элемента в массиве, сумма которых максимальна: ", someList[elem],
              someList[elem+1], someList[elem+2])
        break
#---------------------------------------------------------------------------
countMax=0
for elem  in someList:
    if someList.count(elem) > countMax:
        countMax=someList.count(elem)

for elem  in someList:
    if someList.count(elem)==countMax:
        print("Самое часто встречающийся элемент: ", elem)
        break
#---------------------------------------------------------------------------
triMax=0
for elem in range(len(someList)):
    if (elem+1)%2!=0:
        if someList[elem]%3==0 and someList[elem]>triMax:
            triMax=someList[elem]
print("Среди элементов с нечетными номерами,наибольший элемент массива, который делится на 3:", triMax)

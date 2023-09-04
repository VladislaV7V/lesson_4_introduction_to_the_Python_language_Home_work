"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за
один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки."""

def getGarden():
    grydka = int(input("Всего кустов: "))
    list_ygod = []
    for i in range(grydka):
        list_ygod.append(int(input(f"{i+1} куст. Сколько ягод? ")))
    print (list_ygod)
    return list_ygod

def sborYagod(collection):
    count = int(len(collection)//3)
    resList = []
    for i in range (0, count*3, 3):
            resList.append(collection[i] + collection[i+1] + collection[i+2])
    if len(collection)%3 == 2:
        resList.append(collection[-1] + collection[-2])
    elif len(collection)%3 == 1:
        resList.append(collection[-1])
    print (resList)
    return resList

def largest(collection):
    maxSum = 0
    for i in range (int(len(collection))):
         if collection[i] > maxSum:
              maxSum = collection[i]
              index = i
    print (f"Наибольший сбор {maxSum} был с индекса {index+1} группы")
    return index

garden = getGarden()
# garden = [5, 3, 2, 6, 1, 4, 12] # чтобы не писать руками
sbor = sborYagod(garden)
largest(sbor)
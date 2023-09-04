"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."""

def addList (name):
    countNums = int(input(f"Введите кол-во эл-тов множества {name}: "))
    collection = []
    for _ in range(countNums):
        collection.append(int(input(f"Введите {_+1} число: ")))
    return collection

def sort (collection, name):
    print (f"{name} {collection} - исходный набор") # здесь читать удобне
    for f in range(len(collection)):
        for i in range(len(collection)-1-f):
            if collection[i] > collection[i+1]:
                a = collection[i]
                collection[i] = collection[i+1]
                collection[i+1] = a
    print (f"{name} {collection} - упорядочен")
    return collection

def deleteRecurring (collection, name):
    newCollection = []
    for i in range(len(collection)-1):
        if collection[i]!=collection[i+1]:
            newCollection.append(collection[i])
    newCollection.append(collection[len(collection)-1])
    print (f"{name} {newCollection} - без повторений")
    return newCollection

collection_a = addList("collection_a")
collection_b = addList("collection_b")

# collection_test = [9, 7, 1, 9, 3, 9, 5, 4, 1] # чтоб не прописывать верхний блок.

print()
collection_a = sort (collection_a, "a")
deleteRecurring (collection_a, "a")

print()
collection_b = sort (collection_b, "b")
deleteRecurring (collection_b, "b")

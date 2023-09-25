"""
Реализовать функцию, которая принимает 3 аргумента - min, max, count
И возвращает отсортированный массив уникальных целых чисел от min до max длиной count

Translation: "Implement a function that takes 3 arguments - min, max, count
And returns a sorted array of unique integers from min to max of length count"

I use Camel Case for variable and function names. When defining variables inside of a function i use all uppercases.

Github page: https://github.com/EchoTD/py-sortingTest/blob/main/sortingTest.py

"""
import random # for randomly generating integers

def generateRandomIntArray(MINIMUM, MAXIMUM, COUNT):
    # check for value errors that the user might set wrongfully
    if MINIMUM > MAXIMUM or COUNT > MAXIMUM - MINIMUM + 1:
        raise ValueError("Check the base arguments 'min', 'max' and 'count'. Either 'min' is greater than 'max' or 'count' is higher then the range of 'min' and 'max'.")
    
    numberList = set()
    
    while len(numberList) < COUNT:
        temp = random.randint(MINIMUM, MAXIMUM)
        if temp not in numberList:
            numberList.add(temp)
    
    return sorted(list(numberList))

# Base Arguments
min = 0
max = 1000
count = 40

print(generateRandomIntArray(min, max, count))
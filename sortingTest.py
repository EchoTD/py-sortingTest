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
    
    uniqueList = []
    numberList = list(range(MINIMUM, MAXIMUM))
    
    while COUNT > 0:
        temp = random.choice(numberList)
        uniqueList.append(temp) # adds to the list without the need for an index
        numberList.remove(temp)
        print(COUNT) # testing line, can be commented
        COUNT -= 1

    return sorted(uniqueList)

# Base Arguments
min = 0
max = 100000
count = 999

print(generateRandomIntArray(min, max, count))
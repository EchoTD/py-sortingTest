"""
Реализовать функцию, которая принимает 3 аргумента - min, max, count
И возвращает отсортированный массив уникальных целых чисел от min до max длиной count

Translation: "Implement a function that takes 3 arguments - min, max, count
And returns a sorted array of unique integers from min to max of length count"

I use Camel Case for variable and function names. When defining variables inside of a function i use all uppercases.

Github page: https://github.com/EchoTD/py-sortingTest/blob/main/sortingTest.py

"""
import random # for randomly generating integers

""" O(2(MAXIMUM-MINIMUM) + COUNT)
"""
def generateRandomIntArray(MINIMUM, MAXIMUM, COUNT):
    # check for value errors that the user might set wrongfully
    if MINIMUM > MAXIMUM or COUNT > MAXIMUM - MINIMUM + 1:
        raise ValueError("Check the base arguments 'min', 'max' and 'count'. Either 'min' is greater than 'max' or 'count' is higher then the range of 'min' and 'max'.")
    
    uniqueList = []
    numberList = list(range(MINIMUM, MAXIMUM))
    numberList = numberList.shuffle()
    numberList = numberList.slice(0, COUNT)
    
    return sorted(numberList)

    
    
def generateRandomIntArray2(MINIMUM, MAXIMUM, COUNT) // /dev/urandom

# Base Arguments
min = 0
max = 100000
count = 999

print(generateRandomIntArray(min, max, count))




"""
There is two problems:
1. In cycle random.randomInt(MINIMUM, MAXIMUM) can return not unique value
-OLD-Solution: (Line 23:25) Added an check inside the generation loop to check if a number is already inside the list or not
2. There two problems in your algorithm with arguments MINIMUM=1, MAXIMUM=1000000, COUNT=999999. But with another arguments MINIMUM=1, MAXIMUM=1000000, COUNT=9999 problem is missing
"""    


import random

def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value


    count = 0
    while True:
        random_index = random.randint(0, len(items)-1)
        count+=1
        if items[random_index] == target:
            print(f"found target after {count} tries")
            return random_index






def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.


    count = 0
    for i in range(len(items)):
        count += 1
        if items[i] == target:
            return i, count
    return -1, count





def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.

    count = 0
    start = 0
    end = len(items)-1

    while start <= end:
        count += 1
        midpoint = ((start + end)//2)
        if items[midpoint] == target:
            return midpoint, count
        elif items[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return -1, count



import data
import math
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#inputs 2 time objects
#outputs the two times added together with seconds 0-59
# adds the times then adds a minute and subtracts 60 seconds until seconds are below 60
def time_add(value1: data.Time, value2: data.Time):
    add = data.Time(value1.hour + value2.hour, value1.minute + value2.minute, value1.second + value2.second)
    while add.second > 60:
        add.second -= 60
        add.minute += 1
    return add

# Part 4
#inputs a list of float numbers
#outputs the highest value from that list
#checks each number against the number after it, if the next num is more they swap places
def is_descending(value: list[float])->True:
    for i in range (len(value)-1):
        for a in range (len(value)-1-i):
           if value[a] < value[a+1]:
              temp = value[a]
              value[a] = value[a+1]
              value[a+1] = temp
    return value

# Part 5
#inputs a list of int, an upper limit and lower limit
#outputs None if the upper limit is less than lower, otherwise highest num between limits inclusive
#function checks if each value is less than the next and in between the limits inclusive
def largest_between(value: list[int], upper, lower):
    if upper < lower:
        return None
    for i in range (len(value)-1):
        for a in range(len(value)-1-i):
            if value[a] < value[a+1] or value[a] > upper or value[a] < lower:
                temp = value[a]
                value[a] = value [a+1]
                value[a+1] = temp
    return value[0]

# Part 6
#inputs a list of points
#outputs None if an empty list, otherwise returns the point who's furthest from 0,0 than all others
#checks if a point's distance from 0,0 is further from the next point's distance, if so they swap
def furthest_from_origin(points: list[data.Point]):
    if len(points) == 0:
        return None
    for i in range(len(points)-1):
        for a in range(len(points)-1-i):
            if (math.sqrt((points[a].x-0)**2 + (points[a].y-0)**2)) < (math.sqrt(((points[a+1].x-0)**2 + (points[a+1].y-0)**2))):
                temp = points[a]
                points[a] = points[a + 1]
                points[a + 1] = temp
    return points[0]
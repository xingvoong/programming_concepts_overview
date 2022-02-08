"""
There are some spherical balloons taped onto a flat wall that represents the XY plane.  The balloons are represented as a 2D integer array points where points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches between x_start and x_end.  You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.  A ballon with x_start and x_end is burst by an arrow shot at x
if x_start <= x <= x_end.  There is no limit to the number of arrows that can be shot.  A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the mininum number of arrows that must be shot to burst all balloons.

there are 2 cases for other ballons except the first one:
1: burst together
current_start < previous_end => bust together

2: not burst together
currend_start > previous_end => increase the arrow

"""


def findMinArrayShots(points):

    # sort base on end_time, break tie on start time
    points.sort(key=lambda x: (x[1], x[0]))
    print(points)
    n = len(points)
    previous_end = points[0][1]
    arrows = 1
    for i in range(1, n):
        current_start = points[i][0]
        if current_start > previous_end:
            arrows += 1
            previous_end = points[i][1]

    return arrows


input1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
input2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
input3 = [[1, 2], [2, 3], [3, 4], [4, 5]]

print(findMinArrayShots(input1))
print(findMinArrayShots(input2))
print(findMinArrayShots(input3))

"""
Let N be the number of ballons given.
time: sorting + for loop
sorting: O(NlogN)
for loop: O(N)
=> total: O(NlogN)

space: only extra space for arrow: O(1)
"""

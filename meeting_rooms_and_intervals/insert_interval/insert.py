"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i.  You are also given an interval newInterval = [start, end] that represents the start and end of another interval

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals still does not have any overlapping intervals(merge overlapping intervals if necessary)

Return intervals after he insertion

- append the new intervals in intervals
- sort again: maybe instead of sorting, well samething, I need to shift the element anyway.  So in this case, I can just sort them.
- merge interval using a list
+ 2 cases:
- merge
previos_end > current_start:

- not merge
- return the queue
"""


def insert(intervals, newInterval):
    # append the new intervals in intervals
    intervals.append(newInterval)

    # sort them again
    intervals.sort()
    n = len(intervals)
    toReturn = [intervals[0]]
    for i in range(1, n):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        previous_start = toReturn[-1][0]
        previous_end = toReturn[-1][1]

        # merge
        if current_start <= previous_end:
            new_start = min(current_start, previous_start)
            new_end = max(current_end, previous_end)
            toReturn.pop(-1)
            toReturn.append([new_start, new_end])
        else:
            toReturn.append(intervals[i])

    return toReturn


print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))

"""
Let N be the length of intervals

time: sorting +  looping
- sorting: O(NlogN)
- looping: O(N)

space: O(N), worst case: no overlap

"""

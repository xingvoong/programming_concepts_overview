"""
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the mininum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2], [2,3], [3,4], [1, 3]]

- sort base on starting time
- use a queue, if an iterval is overlapping then I don't add it to the queue
- one potential downfall is that it may not be the mininum number tho

there are 2 possible cases:
+ overlapping
- 2 possible overlapping
  - completely overlapping
  - partialy overlap:

+ not overlapping


"""


def eraseOverlapIntervals(intervals):

    intervals.sort(key=lambda x: (x[0]))
    print(intervals)
    n = len(intervals)
    prev = 0
    count = 0

    for i in range(1, n):
        # overlapping
        # end_1 > start_2
        if intervals[prev][1] > intervals[i][0]:
            count += 1
            # overlap 1, completely overlap:
            # end_1 > end_2
            if intervals[prev][1] > intervals[i][1]:
                # pick the smaller interval
                prev = i

            # this is where greedy comes in
            # partially overlap: be greedy and keep previous, increase the count instead
        # not overlapping:
        # move to the next interval and update prev
        else:
            prev = i

    return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals2 = [[1, 2], [1, 2], [1, 2]]
intervals3 = [[1, 2], [2, 3]]


print(eraseOverlapIntervals(intervals))
print(eraseOverlapIntervals(intervals2))
print(eraseOverlapIntervals(intervals3))

"""
time: sorting +  loop
=> O(NlogN)

space:O(N)

"""

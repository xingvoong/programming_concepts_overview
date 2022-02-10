'''
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the mininum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2], [2,3], [3,4], [1, 3]]

- sort base on starting time
- use a queue, if an iterval is overlapping then I don't add it to the queue
- one potential downfall is that it may not be the mininum number tho

'''

def eraseOverlapIntervals(intervals):
  # intervals.sort()

  intervals.sort(key=lambda x: (x[1]))
  return intervals


intervals = [[1,2], [2,3], [3,4], [1, 3]]
intervals2 = [[1,2],[2,3]]

print(eraseOverlapIntervals(intervals))
print(eraseOverlapIntervals(intervals2))

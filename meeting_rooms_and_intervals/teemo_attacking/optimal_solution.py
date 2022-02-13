
'''
At every step:
- take the min of the current time, next time, or the min duration
- total + durantion
but why min(timeSeries[i+1] - timeSeries[i], duration) tho?
- because it needs to reset if there is over lap, in that case, at timeSeries[i+1], I can get the duration for the total
- but before that I can only get the interval in between by doing
timeSeries[i+1] - timesSeries[i]
- for last element, there is no overlapping, so it is just the total + duration

- the max is that: duration * n if counting overlap
'''

def findPoisonedDuration(timeSeries, duration):
  total = 0
  n = len(timeSeries)
  for i in range(n - 1):
    total += min(timeSeries[i+1] - timeSeries[i], duration)

  return total + duration

print(findPoisonedDuration([1, 4], 2))
print(findPoisonedDuration([1, 2], 2))

'''
let N be the length of timeSeries

time: O(N)
space: O(1)
'''
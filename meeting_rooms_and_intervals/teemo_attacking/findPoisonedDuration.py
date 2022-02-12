'''
Our hero Teemo is attacking an enemy Ashe with poison attacks!  When Teenmo attacks Ashe, Ashe gets poisoned for a exactly duration seconds.  More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration -1].  If Teenmo attacks again before the poision effect ends, the timer for it is resetm and the poison effect will end duration seconds after the new attack.

given: non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teenmo attacks Ashe at second timeSeries[i], and an integer duration

Return the total number of seconds that Ashe is poisoned

Example 1:

[t, t + duration - 1]
[1, 1 + 2 - 1] = [1, 2]
[4, 4 + 3 - 1] = [4, 5]

[1, 1 + 2 - 1] = [1, 2]
[2, 2 + 2 - 1] = [2, 3]
'''

def findPoisonedDuration(timeSeries, duration):

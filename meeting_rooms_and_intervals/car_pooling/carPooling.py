'''
There is a car with capacity empty seats.  The vehicle only drives east (i.e, it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengers_i, from_i, to_i] indicates that the i_th trip has numPassengers_i passengers and the locations to pick them up and drop them off are from_i to_i respectively.  The locations are given as the number of kilometers due east from the car's init location.

Return true if it is possible to pick up and drop off all passenders for all the given trips, or false otherwise.

example 1:
Input: trips = [[2, 1, 5], [3, 3, 7]], capacity = 4
Output: false

example 2:
input: trips = [[2, 1, 5], [3, 3, 7]] capacity = 5
output: true

'''

def carPooling(trips):

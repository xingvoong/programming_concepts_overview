# Meeting rooms and interval problems

Type of problems
- [x]  Meeting room II
- [x]  Meeting room
- [x]  Merge intervals
- [x]  Minimum number of arrows to burst balloons
- [x]  Car Pooling (medium)
- [ ]  Non-overlapping Intervals (Medium)
  - Did not understand greedy solution
- [ ]  Teemo Attacking (Easy)
- [ ]  Insert Interval (medium)
- [ ]  Add Bold Tag in String (medium)
- [ ]  Partition Labels (medium)
- [ ]  Interval List Intersections (medium)

```bash
Framework:
- sort base on starting time of intervals, or sometimes end time, depend on the problem, then break tie on the other.
- Often times, need to use a queue to store the result.  If needed, use a priority queue base on end time
- go to the intervals 1 by 1 using a for loop
- greedy algo, find the locally max or min, and proof that it is the globle max or min.
```

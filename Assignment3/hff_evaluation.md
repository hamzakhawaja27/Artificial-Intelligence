| Blocks | HFF          | NO HFF         | Logistics |Logistics HFF| Logistics NoHFF|
|--------|--------------|----------------|-----------|-------------|----------------|
| Task01 | 6,8,0.003    | 6,99,0.027     |           | 20,22,0.033 | 20,11907,0.61  |
| Task02 | 10,11,0.0069 | 10,66,0.021    |           | 19,22,0.031 | 19,9704,0.45   |
| Task03 | 6,8,0.0055   | 6,60,0.026     |           | 15,17,0.019 | 15,4966,0.24   |
| Task04 | 12,15,0.0072 | 12,467,0.013   |           | 27,28,0.058 | 27,113472,6.8  |
| Task05 | 14,39,0.002  | 10,464,0.013   |           | 17,19,0.037 | 17,22081,1.3   |
| Task06 | 20,36,0.019  | 16,750,0.02    |           | 8,8,0.0044  | 8,1070,0.065   |
| Task07 | 12,12,0.01   | 12,1480,0.091  |           | 25,27,0.062 | 25,480488,35   |
| Task08 | 14,25,0.022  | 10,3898,0.14   |           | 14,15,0.027 | 14,26877,1.8   |
| Task09 | 28,44,0.033  | 20,6544,0.22   |           | 26,28,0.065 | 25,494011,35   |
| Task10 | 22,31,0.042  | 22,36825,1.7   |           | 24,26,0.055 | 24,394124,28   |
| Task11 | 30,71,0.07   | 22,64524,2.9   |           | 38,50,0.32  | takes too long |
| Task12 | 38,145,0.14  | 20,58728,2.6   |           | 45,58,0.43  | takes too long |
| Task13 | 34,279,0.43  | 18,512915,30.0 |           | 31,33,0.26  | takes too long |
| Task14 | 24,175,0.25  | 20,617006,36   |           | 44,48,0.45  | takes too long |
| Task15 | 26,45,0.05   | 16,395020,24   |           | 40,48,0.4   | takes too long |




The values in the table are in the format of
plan length, Expanded Nodes, Search Time

As observed in the two experiments the number of nodes expanded decrease substantially with the use of HFF heuristic. This is because Blind Heuristic gives no estimation to the search about preferable nodes to be explored and gives a value of 0 to all the nodes except the last node. This leads to the search stategy searching every node once but has an advantage of finding an optimal plan.
On the other hand HFF gives a very good estimation of the number of actions required to reach a goal state from any current state. This helps the GBF to explore the cheapest node and reach the goal quickly, even if the plan length is not that optimized. With all the advantages of HFF, for smaller tasks it takes more time, because the decrease in the time taken to expand nodes is off set by the time taken to calculate the Heuristic.  

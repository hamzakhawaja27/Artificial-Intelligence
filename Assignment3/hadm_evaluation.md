| Blocks | HADM           | NO HADM        | Logistics | HADM           | No HADM        |
|--------|----------------|----------------|-----------|----------------|----------------|
| Task01 | 6,26,0.021     | 6,100,0.0042   |           | 20,6320,28     | 20,11868,0.66  |
| Task02 | 10,27,0.02     | 10,65,0.0017   |           | 19,5446,23     | 19,9932,0.54   |
| Task03 | 6,23,0.018     | 6,53,0.0015    |           | 15,1696,7.5    | 15,4770,0.25   |
| Task04 | 12,251,0.48    | 12,452,0.026   |           | takes too long | 27,113155,7.7  |
| Task05 | 10,219,0.28    | 10,526,0.028   |           | takes too long | 17,22047,1.4   |
| Task06 | 16,773,1.1     | 16,961,0.5     |           | 8,513,2.9      | 8,948,0.8      |
| Task07 | 12,778,1.9     | 12,2522,0.24   |           | takes too long | over 2 min     |
| Task08 | 10,2167,5.4    | 10,4660,0.43   |           | takes too long | 14,24989,1.9   |
| Task09 | 20,15494,37    | 20,30301,1.5   |           | takes too long | takes too long |
| Task10 | 22,40,10004    | 20,186397,14   |           | takes too long | takes too long |
| Task11 | 22,160,38789   | 22,1213791,88  |           | takes too long | takes too long |
| Task12 | 20,210,25460   | takes too long |           | takes too long | takes too long |
| Task13 | takes too long | takes too long |           | takes too long | takes too long |
| Task14 | takes too long | takes too long |           | takes too long | takes too long |
| Task15 | takes too long | takes too long |           | takes too long | takes too long |


For q4 I have implemented Hmax. As this heuristic is admissable, it is slower than HFF, but finds a better solution. The number of expanded nodes obviously decrease significantly with the Hadm heuristic but it takes much more time than simple blind heuristic. As calculating the heuristic it self takes alot of time, especially for smaller tasks. Since A* finds an optimal solution so it has to revisit nodes, which adds to the reason why it takes soo long to find a solution.

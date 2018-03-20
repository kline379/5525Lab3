# 5525Lab3
Our lab and the results produced are stored in the "lab3" python notebook file. 

## Required Part
The first block of code shows the generation of MFCCs and the second block the dymanic time warping algorithm.  From there, we test the DTW algorithm by calculating the distance between "a" and "b" samples of the same and different sounds.

The testing of the DTW algorithm in the third block shows that the algorithm is very accurate as pairs that are the same number always have a distance of "0" once they are time warped whereas many of the other pairings have large distances.

## Extension 3:
The fourth block contains extension 3 which demonstrates the results of using an MoG algorithm to model the differences along with a graph of how changing the number of components changes the scoring against the "b" test data.

## Extension 2:
Extension 2 is found in the last block which is a modified version of our DTW algorithm.  It traces the shortest path and maps it out on a graph.  An examples of tracing between 5 and 9 is shown. When matching 5 to 9, it appears that the algorithm attempts to map similarly sounding parts of the numbers to one another, for instance, both have the same vowel at the beginning.

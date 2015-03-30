Write a program that takes a list of integer numbers as input.
Determine the number of sets of 3 items from the list, that sum to 0.

E.g. if the list is [5, -2, 4 , -8, 3], then there is one such triplet: 5 + (-8) + 3 = 0.
For larger lists, the number of triplets probably will be much higher.

If the list would contain a value more than once, count a triplet for each item with this value.
E.g. the list [5, -2, 4, 3, -8, 3] will have two triplets:
5 + 3 + (-8) = 0 (with value 3 from position 3) and
5 + (-8) + 3 = 0 (with value 3 from the last position in the list)

What is the time complexity of your algorithm?

Suppose your algorithm works in time T(n) = a*n^b, then you can easily derive that T(2n)/T(n) = 2^b.
Measure T(n) and T(2n) for some value of n, and use these measurements to estimate the exponent b for your algorithm.

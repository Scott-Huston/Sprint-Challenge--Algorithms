#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This snippet has a maximum time complexity of O(1). The maximum time complexity would occur if n > 1. In that case, the algorithm would run twice. The first time would run because 0 is less than some number greater than 1. The second time, (n*n) < (n*n*n), but the third time, a would equal n*n*n which is equal to  n*n*n and thus the while loop would not run again.


b) The maximum time complexity of this snippet is O(n). Although the while loop adds additional complexity to this snippet, for very large numbers of n the while loop is relatively insignificant.

c) The time complexity of this recursive method is O(n). The if statement has a complexity of O(1), but the bunnies method will continue to be called on bunnies-1 until bunnies equals 0.

## Exercise II

Pseudocode

##################
Define low_break variable to keep track of lowest floor the egg has broken on. Initialize to n.

Define high_no_break variable to keep track of highest floor the egg has not broken on. Initialize to 0.

Define high_floor to n

Define low_floor to 0

While low_break-high_no_break is greater than 1:

    current_floor = (high_floor-low_floor)//2+low_floor

    Drop egg off of current_floor

    If the egg breaks, we know we need to go to a lower floor, so low_break = current_floor and high_floor = current_floor

    If the egg does not break, we know we need to go to a higher floor, so high_no_break = n//2 and low_floor = current_floor

floor_f = low_break
####################

Maximum time complexity = O(log(n))
The search space is halved with each iteration



#CFG to C: 70
Wouldn't it be cool to be able to have one of these patrol drones to do your bidding?! Figure out the correct sequence of C functions from the following control flow graphs and you should be well on your way.

Submit the correct order of functions.

##Solution
1. The control flow diagram features 4 seperate flow charts and 4 pieces of C code, we are tasked with matching them.
2. To do this I looked at the flow of each flow chart
  1. This has a loop, and we can also see subtraction. We can therefore match this to B
  2. This doesn't have a loop but does have two alternative paths. We can match this to C
  3. Again this has a loop but this time has some addition. This matches D
  4. This is a simple function with no loops or paths, we can match this to A
3. This gives us the solution `BCDA`

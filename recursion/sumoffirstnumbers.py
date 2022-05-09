##sum of firts n numbers
import sys
sys.setrecursionlimit(2000) 
def sum (nparam):
    n=nparam
    if (n == 1): 
        return 1
    else: 
        return n + sum(n-1)
print(sum(1000))

# You can improve your function performance dramatically, if your function is a [pure function](https://en.wikipedia.org/wiki/Pure_function).
# But, it will increase the memory usage, so be careful using the lru_cache.

from functools import lru_cache

@lru_cache(maxsize=100)
def greedy_fibonacci(n = 0):
    if(n<=1) : 
        return 1
    return greedy_fibonacci(n-1) + greedy_fibonacci(n-2)

if __name__=="__main__":
    print(greedy_fibonacci(120))
     

# Memoize -> To store (the result of a computation) so that it can be subsequently retrieved without repeating the computation.
import functools 
import time
@functools.lru_cache(maxsize=None)
def fx(a):
    time.sleep(5)
    return a*5

print(fx(5))
print('Done for 5')
print(fx(2))
print('Done for 2')
print(fx(4))
print('Done for 4')
print(fx(6))
print('Done for 6')
print(fx(5))
print('Done for 5')
print(fx(7))
print('Done for 7')

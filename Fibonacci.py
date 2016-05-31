def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a+b
            
            
from itertools import islice
print list(islice(fib(),5))
'''
Creating a fibonacci sequence in python.

@author: Grant Cahill
'''

fib_seq = []
fib_seq.append(0)
fib_seq.append(1)

def get_fib(position):
    if len(fib_seq) > position:
        return fib_seq[position]
    else:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return get_fib(position)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)


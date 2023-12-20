# import numpy as np
# from threading import Thread

# a = np.ones(10)

# def func(b):

#     b[0] = 0

#     return b

# x = Thread(target=func,args=(a))

# print(x)

def foo(bar, result, index):
    print ('hello {0}'.format(bar))
    result[index] = "foo"

from threading import Thread

threads = [None] * 10
results = [None] * 10

for i in range(len(threads)):
    threads[i] = Thread(target=foo, args=('world!', results, i))
    threads[i].start()

# do some other stuff

for i in range(len(threads)):
    threads[i].join()

print (" ".join(results))  # what sound does a metasyntactic locomotive make?

from functools import reduce

def f(x, y):
    return x + y

a = [1,2,3]
print(map(lambda x:x*x,range(10)))
print(reduce(lambda x,y:x*y, [1, 3, 5, 7, 9], 1))
# print(list(reduce(lambda x, y: x + y, [2, 3, 4, 5, 6], 1)))

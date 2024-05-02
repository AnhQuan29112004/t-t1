import functools
s = [1,2,3,4,5]
print(functools.reduce(lambda x,y:x+y, s, 10))

print('{0:x}'.format(1))
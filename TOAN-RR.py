import math

#Quy tắc xây dựng xâu nhị phân
def xd(n,b):
    a = [ str(i) for i in range(b+1)]
    if n==1: return a
    s = []
    for i in a:
        for j in xd(n-1,b):
            s.append(i+j)
    return s
print(xd(2,2))

def binary(n):
    if n==1:return ['0','1']
    C = []
    for i in binary(n-1):
        C.append(i+'0')
        C.append(i+'1')
    return C
print(binary(4))

from sympy import *
x, y = symbols('x y')
print(((x+y)**10).expand())

    
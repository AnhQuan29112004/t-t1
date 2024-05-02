from sympy import symbols, Sum
n, i = symbols('n i')
print(Sum(i,(i,1,n)).doit().simplify())
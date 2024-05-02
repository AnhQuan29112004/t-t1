from dataclasses import dataclass
'''@dataclass
class toado:
    x: int
    y: int
    z: int = 0
t = toado(1,2,4)
print(t);'''



def field():
    i =0
    while True:
        yield i*i
        i+=1

def tong(a,b):
    return a+b
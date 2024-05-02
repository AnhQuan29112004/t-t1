def binary(a):
    if a == 1:return ['0', '1']
    p = []
    for i in binary(a-1):
        p.append(i+ '0')
        p.append(i + '1')
    return p

print(binary(3))
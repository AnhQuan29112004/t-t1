def noibot(x):
    n = len(x)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if x[i]>x[j]:
                x[i], x[j] = x[j], x[i]
    return x
print(noibot([1,4,3]))
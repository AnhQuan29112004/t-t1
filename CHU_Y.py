Lst=[1,2,3,4,5]
a, *b, c = Lst
print(a+c)
#Giải thích: a sẽ gán phần từ đầu của list, c sẽ gán phần tử cuối, b sẽ gán các phần tử còn lại ở giữa-> a=1, c=5

d = 4
print(f'{d=}') # in ra d=4
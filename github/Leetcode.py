'''import re
haystack = 'sadbutsad'
needle='sad'
temp = re.finditer('sad',haystack)
if(re.search(needle,haystack)is not None):
    for i in temp:
        return (i.start())
else:return -1'''



'''import re
s = 'Hello World'
temp = re.findall(r'[a-z|A-Z]+',s)
print(len(temp[-1]))'''''



'''def kiemtra(num):
    soluong = f'{num:b}'.count('1')
    return (soluong,num)
def kiemtra1(num):
    return num
arr = [0,1,4,3,6,8,5,2,7]
arr.sort(key = lambda x: (f'{x:b}'.count('1'),x) )

print(arr)'''


'''s='paper'
t = 'title'
print(set(zip(s,t)))'''


'''s = 'edcab'
t = 'baca'
#a = (list(s).sort())
a = list(set(s))
a.sort()
#a.sort()
print(a)'''



#MODULE COLLECTION.COUNTER : đếm số lần các phần tử xuất hiện và đưa gia trị thành key và số lần đếm là value cho vao 1 dict
'''from collections import Counter
s = 'abcade'
t = 'cbaade'
print(Counter(s))
print(Counter(t))'''





'''
s = 'gctcxyuluxjuxnsvmomavutrrfb'
t = 'qijrjrhqqjxjtprybrzpyfyqtzf'
a={}
b={}
for i in s:
    a[i]=s.count(i)
for i in t:
    b[i]=t.count(i)
t = 0
for i in b:
    if(i not in a):t+=1
    if(i in a and (b[i]>a[i])):
        t += (b[i]-a[i])
print(t)'''





'''a = {'a':2, 'b':1}
for i in range(len(a)):
    print(i)
print(a.items())'''


# from collections import Counter
# a = [1,2,1,1,2,2,3]
# print(sorted(Counter(a).values()))

# from collections import Counter

# b = 'dog cat cat dog'
# d = 'abba'

# # Tạo Counter cho danh sách các từ trong chuỗi b
# c = Counter(b.split())
# print(c.values())

# # Tạo Counter cho chuỗi d
# d_counter = Counter(d)
# print(d_counter.values())
# # So sánh tần suất xuất hiện của các phần tử duy nhất
# if sorted(c.values()) == sorted(d_counter.values()):
#     print('true')
# else:
#     print('false')

# b = 'cat cat cat dog'
# print(b.split())
# d = 'aba'
# c = zip(b.split(),d)
# print(list(c))


# n = int(input())
# integer_list = map(int, input().split())
# print(list(integer_list))




        
from collections import Counter
o = '-+12'
p = []
for i in o:
    if(ord(i)< 48 and ord(i) != 45 or ord(i)>57 or ord == ' '):continue
    p.append(i)
print(p)
print(int(''.join(p)))











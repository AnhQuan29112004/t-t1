import re
'''s = 'foo\n'
pattern = re.findall(r'$',s)
print(pattern)'''


s = '<a> b <c>'
pattern = re.findall(r'<.*?>',s)
print(pattern)

s1 = 'aaaa'
temp = re.findall(r'a*',s1)
print(temp)


s2 = 'lazy dog'
temp1 = re.findall(r'lazy (?=dog)',s2) #tìm tất cả lazy nhưng chỉ khi có dog ở phía sau
print(temp1)



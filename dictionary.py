a= 1
b=9
a, b = b, a
print(a,b)

d2 ={'muk':'chicken', 'nisha':"veg", 'anish':{"k":'kind',"f":"funny"}}
print(d2)
print(d2['muk'])
print(d2['anish']['k'])
d2[420] = 'i love coding'
print(d2)

lst = [4, 54, 67, 92]
lst[1] = 9
print(lst)


d7 ={'ans':'q', 'rat':'m' }
d9 =d7
print(d9)
print(d7)

d7 ={'ans':'q', 'rat':'m' }
del d7['ans']
print(d7)

d7 ={'ans':'q', 'rat':'m' }
d7.update({'mom':'dad'})
print(d7)
print(d7.keys())
print(d7.items())

#d7 ={'ans':'q', 'rat':'m' }       # yo run vayena
#print(d7.get['ans'])

num =[2, 9, 4, 6]
num.insert(1,54)
print(num)

import os
os.rename('Tuple.py', 'dictionary.py')

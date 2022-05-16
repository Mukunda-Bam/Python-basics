s = 'first line. \nsecond line.'
print(s)
#use of raw string
n = r"\first\name"
print(n)
#\ paxi nospace sidhai enter otherwise newline is\n represnts in three quote
print('''\
    Usage:time
    is 
    valuable
    ''')
print(4 *'mu' + 'kunda')
word = "python"
print(word[0])
print(word[0:4])
print(word[0:-1])
print(word[-1])
print(len(word))
list =[1, 7, 18, 20]
print(list)
print(list[-3:])
t = list + [2, 5, 9]
print(t)
#replace 18 with 13 in t
t[2] = 13
print(t)
t.append(14)
print(t)
t.append(14*2)
print(t)
t[1:3] = ['A', 'B']
print(t)
t[1:3] = []
print(t)
s = 'mukunda' +'ban'
print(s)
print(s.replace('ban', 'bam'))
print(s.replace('n', 'p'))
#fibaonicca
a,b = 0,1
while a<10:
    print(a)
    a, b = b, a+b
words = ['apple', 'ball', 'cat']
for w in words:
    print(w, len(w))




















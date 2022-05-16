age = input('what is your age? ')
nam = input('enter your name: ')

#swapping the variables
a =1
b =2
a, b= b, a
print(a, b)
print("value of a after swapping: {}".format(a), "value of b after swapping: {}".format(b))

#second method to swap by using temporary variable by taking from  user
x =input('enter value of x: ')
y= input('enter value of y: ')
temp =x
x= y
y = temp
print("value of x after swapping: {}".format(x))
print("value of y after swapping: {}".format(y))


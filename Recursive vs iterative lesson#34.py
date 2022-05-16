def iter_fact(n):
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return fac
num=int(input("enter a number: "))
print(iter_fact(num))
#funct using recursive function
def rec_fact(n):
    if n==0:
        return 1
    else:
        return n *rec_fact(n-1)
nmb=int(input("enter a number:"))
print(rec_fact(nmb))




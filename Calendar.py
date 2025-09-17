
print("What year would you like to know? Calculating the date of Easter Sunday for any year between 1900 and 2099 ")
N = input()

N=int(N)

a=N % 19
b=N // 100
c=N % 100
d=b//4
e=b%4
f=(b+8)//25
g=(b- f + 1) // 3
h=(19*a+b-d-g+15)%30
i=c//4
k=c%4
l=(32+2*e+2*i-h-k)%7
m=(a+11*h+22*l)//451
month=(h+l-7*m+114)//31
day=((h+l-7*m+114)%31)+1
print("Easter Sunday in year",N, "falls on",month,"/",day)




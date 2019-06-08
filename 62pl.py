a=int(input())
c=0
for i in range(1,a+1):
    b=a//i
    if b%2==1 and a%i==0:
        print(i)
        break

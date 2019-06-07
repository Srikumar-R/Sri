a,b=input().split()
c=input().split()
c.sort(reverse=True,key=int)
print(c[-int(b)])

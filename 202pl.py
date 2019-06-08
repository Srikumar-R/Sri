a=input()
b=''
for i in a:
  if i in 'aeiou':
    b+=i
for i in a:
  if i not in 'aeiou':
    b+=i
print(b)

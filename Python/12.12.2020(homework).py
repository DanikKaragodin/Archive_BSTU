import random
n=int(input())
a = [0 for i in range(n)]
print(a)
m=int(input())
for i in range(m):
    a[i]+=1
for i in range(m,n):
        a[i]+=2
print(a)
       
for i in range(n):
    if(len(a)==1):
        break
    try: 
        a[m]+=a[m-1]
        a.pop(m-1)
    except IndexError:    
         a[-1] += a[0]
         a.pop(0)
        
    
print ("Номер последнего человека:", m-1)
print ("Всего собрано монет:", a[0])
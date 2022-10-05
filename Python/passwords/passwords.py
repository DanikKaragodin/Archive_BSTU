import statistics
from statistics import mode
def most_popular(List):
    return(mode(List))

f=open("pwd.txt")
passwords=[]
for line in f:
    passwords.append(line[line.find(';')+1:])
f.close()
top_ten=[]
for i in range(10):
    top_ten.append(mode(passwords))
    for c in range(passwords.count(top_ten[i])):
        passwords.remove(top_ten[i])
print("ТОП 10 самых популярных паролей:")
for x in top_ten: print(x,end="")
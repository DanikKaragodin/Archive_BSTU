s=input("input string: ")
if(len(s)%2!=0):
    s=s+" "
s1=s[:int(len(s)/2)]
print("first half: ",s1)
s2=s[int(len(s)/2):]
print("second half: ",s2)
j=0
i=0

while i<int(len(s)/2):

    if(i==len(s2)-1):
        s1=s1+s2[int(len(s2)-1)]
        break
    s1=s1.replace(s1[j]+s1[j+1],s1[j]+s2[i]+s1[j+1])
    j+=2
    i+=1
 
print("shivrovka: ",s1)

#-------------------------------------------------

s3=""
s4=""
i=0
while i < len(s1):
    if i%2==0:
        s3=s3+s1[i]
    else:
        s4=s4+s1[i]
    i+=1
deshifr=s3+s4
print("deshifrovka: ", deshifr)

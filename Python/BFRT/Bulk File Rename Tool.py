import os
nameOfPath=[]
directory=input("Укажите путь до файлов --> ")
formatFile= input("По какому формату переименовать файлы?(Вводите без точки) --> ")
for file in os.listdir(directory):
    if file.endswith(formatFile) or file.endswith(formatFile.upper()):
       nameOfPath+=[os.path.join(directory, file)]
c=0
for i in nameOfPath: print(i)
shablon=input("Какой шаблон использовать ? -> ")

for i in nameOfPath:
    os.rename(i,"{}\\{}{}.{}".format(directory,shablon,c,formatFile))
    c+=1
    

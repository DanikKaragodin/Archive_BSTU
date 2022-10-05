""""
text = "Meet my family. /*There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael.*/ My mum enjoys reading and my dad enjoys playing chess with my brother Ken. My mum is slim and rather tall."

while text.find('/*') != -1 or text.find("*/") != -1:# поиск подстроки в строке
    f = text.find("/*")# поиск подстроки в строке
    fi = text.find("*/")# поиск подстроки в строке
    delete = text[f: fi + 3]# удаляется расстояние
    text = text.replace("Meet", "")#Возвращает копию строки, в которой заменены все вхождения указанной строки указанным значением.
print(text)
  """"
  
s = input("Введите строку в которой надо удалить группу символов: ")
while s.find("/*") != -1:
    firstPlace = s.find("/*")
    lastPlace = s.find("*/")
    s=s.replace(s[firstPlace: lastPlace+2],"")
print("Вот готовый вариант: ",s)
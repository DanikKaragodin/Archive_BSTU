from abc import ABC,abstractmethod
class table():
    def start(self):
        global table
        table=[['☐'] * 8 for i in range(8)]
        table[0][0]='♖'
        table[0][7]='♖'
        table[7][0]='♜'
        table[7][7]='♜'
        table[0][1]='♘'
        table[0][6]='♘'
        table[7][1]='♞'
        table[7][6]='♞'
        table[0][2]='♗'
        table[0][5]='♗'
        table[7][2]='♝'
        table[7][5]='♝'
        table[0][3]='♕'
        table[7][3]='♛'
        table[0][4]='♔'
        table[7][4]='♚'
        for a in range(8):
            for b in range(8):
                table[1][b]='♙'
                table[6][b]='♟'
        for a in range(8):
            print()
            for b in range(8):
                print(table[a][b],end=" ")



class figure(ABC):
    def draw():
        pass
    def death():
        pass

    @abstractmethod
    def move():
        pass
    @abstractmethod
    # ШАХ
    def check():
        pass
    # МАТ
    @abstractmethod
    def mate():
        pass
# ПЕШКА(ПУТИНА)
class pawn(figure):
   # coordinate=
     def move(self,number):
        
     def check(self):
        pass
     def mate(self):
        pass

# КОНЬ
class chess_knight(figure):
     def move(self):
        pass
     def check(self):
        pass
     def mate(self):
        pass
# СЛОН
class chess_bishop(figure):
     def move(self):
        pass
     def check(self):
        pass
     def mate(self):
        pass
     
# ЛАДЬЯ
class rook(figure):
     def move(self):
        pass
     def check(self):
        pass
     def mate(self):
        pass
     
# ФЕРЗЬ
class queen(figure):
     def move():
        pass
     def check():
        pass
     def mate():
        pass
     
# КОРОЛЬ
class king(figure):
     def move():
        pass
     def check():
        pass
     def mate():
        pass
     
table=table()
table.start()
Endgame=False
xod=0
blackpawn=pawn()
whitepawn=pawn()


blackchess_knight[2]=chess_knight()
blackchess_bishop[2]=chess_bishop()

while Endgame==False:
    if xod%2==0:
        print("Сейчас ход белых")
    else:
        print("Сейчас ход черных")
    choise=input('''
    Какой фигурой будем ходить?
    1.Пешка
    2.Конь
    3.Слон
    4.Ладья
    5.Ферзь
    6.Король''')
    if choise=="1":
        number=input("Введите номер пешки(1-8)")
        if xod%2==0:
            whitepawn.move(number)
        else:
            blackpawn.move(number)
    if choise=="2":
        number=input("Введите номер коня(1-2)")
    if choise=="3":
        number=input("Введите номер слона(1-2)")
    if choise=="4":
        number=input("Введите номер ладьи(1-2)")
    if choise=="5":
        pass
    if choise=="6":
        pass







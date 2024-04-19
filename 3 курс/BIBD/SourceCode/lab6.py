import time
import keyboard
I1 = False 
Q1 = True
Q2 = False
Q3 = False
T1 = 0 # 25 сек
T2 = 0 # 16 cек
T3 = 0 # 3 сек
currentTime  = 0

# Функция, которую вы хотите вызвать при нажатии клавиши Space
def PressButtonWalker():
    global I1,Q1,Q2,Q3,T1,T2,T3
    if I1:
        # print("Кто-то из пешеходов повторно нажал на кнопку запроса",time.asctime())
        pass
    else:
        I1 = True
        print("Кто-то из пешеходов нажал на кнопку запроса",time.asctime())
    while(T1<25):
        pass
    if I1 and T1>=25:
        Q2 = True
        print("Светофор для водителей перешёл в желтое состояние",time.asctime())
        while(T3<3):
            time.sleep(1)
            T3+=1
    if T3 >= 3: 
        Q1 = False
        Q3 = True
        Q2 = False
        print(f'''Светофор для водителей перешёл в красное состояние.{time.asctime()}
Светофор для пешеходов перешёл в зелёное состояние.{time.asctime()}
Пешеходы переходят дорогу...{time.asctime()}''')
        T3 = 0
        WalkerTime()

def WalkerTime():
    global I1,Q1,Q2,Q3,T1,T2,T3
    while(T2<16):
        time.sleep(1)
        T2+=1
    print(f'''Время для перехода пешеходов закончилось.{time.asctime()}
Светофор для пешеходов перешёл в красное состояние.{time.asctime()}
Светофор для водителей перешёл в жёлтое состояние.{time.asctime()}''')
    Q3 = False
    Q2 = True
    T2 = 0
    while(T3<3):
        time.sleep(1)
        T3+=1
    if T3 >= 3: 
        Q1 = True
        Q2 = False
        print(f'''Светофор для водителей перешёл в зелёное состояние.{time.asctime()}
Водители начали движение...{time.asctime()}''')
        T3 = 0
        I1 = False
        T1 = 0
    


# # Функция, которая будет вызываться при нажатии клавиши
# def on_key_pressed(event):
#     if event.name == 'space':
#         my_function()
# Регистрация функции для обработки события нажатия клавиши
#keyboard.on_press(on_key_pressed)
print(f"Светофор был запущен.{time.asctime()}\nСветофор для водителей стартовал работу в зелёном состоянии.{time.asctime()}\nСветофор для пешеходов стартовал работу в красном состоянии.{time.asctime()}")
keyboard.add_hotkey('space',lambda: PressButtonWalker(),suppress=True)
while(True):
    if keyboard.is_pressed('esc'): break
    #print("Прошла секунда")
    time.sleep(1)
    T1+=1
    #print("T1: ",T1)
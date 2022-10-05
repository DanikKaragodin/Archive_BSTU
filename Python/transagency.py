from statistics import mean
import random
from time import sleep


class Imitation:
    Path = 0
    mass = 0
    ownBase = " "
    customerBase = " "
    # переменная показывающая хорошая погода ли в городах
    weather = True
    # доход компании,измеряется в усл.ед.
    doxodOnAirplane=0.0
    doxodOnTrain=0.0
    doxodOnCar=0.0
    # среднее время(все время суётся в список,потом арифметическое среднее)
    averageTime = []
    averageTimeonAirplane = []
    averageTimeonTrain = []
    averageTimeonCar = []
    
    # потери вследствии аварии
    lossAvaria = 0
    lossAvariaonAirplane = 0
    lossAvariaonTrain = 0
    lossAvariaonCar = 0
    #поездки
    poezdokOnTrain=0
    poezdokOnAvto=0
    poezdokOnAirplane=0
    
    def _init_(self, path, mass):
        self.Path = path
        self.mass = mass
        # случаная генерация нашей базы,т.е. в каком она городе
        randomINT = random.randint(1,3)
        if(randomINT == 1):
            ownBase = "Big"
        elif(randomINT == 2):
            ownBase = "Medium"
        elif(randomINT == 3):
            ownBase = "Small"
        # генерация базы заказчика,т.е. в каком она городе
        randomINT = random.randint(1,3)
        if(randomINT == 1):
            customerBase = "Big"
        elif(randomINT == 2):
            customerBase = "Medium"
        elif(randomINT == 3):
            customerBase = "Small"
        # шанс на плохую погоду
        randomWeather = random.randint(0, 100)
        if randomWeather < 6:
            self.weather = False
        else:
            self.weather = True
        # выбор транспорта
        if (self.weather == True and ownBase == "Big" and customerBase == "Big"):
            print("Самым оптимальным решением стал самолет.")
            self.airplane()
        elif((ownBase == "Big" or ownBase == "Medium") and (customerBase == "Big" or customerBase =="Medium")):
            print("Самым оптимальным решением стал поезд.")
            self.train()
        else:
            print("Самым оптимальным решением стал автомобиль.")
            self.car()

    def airplane(self):
        airplaneSpeed = 500
        path = self.Path
        # реализация пути
        while path > 0:
            # шанс на поломку,снижение дохода,резкий выход из функции,увеличивается потеря из-за аварий
            polomka = random.randint(0, 1000)
            if polomka == 55:
                print("Самолет пал во время полета,деньги идут в минус")
                self.doxodOnAirplane -= 3*self.mass
                self.lossAvaria += 1
                self.lossAvariaonAirplane += 1
                return
            path -= airplaneSpeed
        # если все закончилось успешно
        print("Ваш самолет долетел до конца и отдал груз.  ")
        # доход на этом транспорте
        self.doxodOnAirplane+=3*self.mass
        # кол-во поездок успешных
        self.poezdokOnAirplane+=1
        # в список добавляется время пути
        self.averageTime.append(self.Path/airplaneSpeed)
        self.averageTimeonAirplane.append(self.Path/airplaneSpeed)
        print("Самолет долетел за ", self.Path/(airplaneSpeed), " часов")


    def train(self):
        path = self.Path
        # кол-во магистралей было пройдено
        count_magistral = 0
        # реализация пути поезда
        while path > 0:
            trainspeed = 100
            # шанс на поломку и снижение дохода в этом случаи,резкий выход из функции,увеличивается потеря из-за аварий
            polomka = random.randint(0, 500)
            if polomka == 1:
                print("Поезд пал во время езды,деньги идут в минус")
                self.doxodOnTrain -= 1.5*self.mass
                self.lossAvaria += 1
                self.lossAvariaonTrain += 1
                return
            # шанс на выход на магистраль + увеличение скорости
            magistral = random.randint(0, 100)
            if magistral < 10:
                trainspeed += 50
                count_magistral += 1
            # снижается путь,якобы прошел час езды
            path -= trainspeed
        # если все закончилось успешно
        print("Ваш Поезд доехал до конца и отдал груз.  ")
        # доход на этом транспорте
        self.doxodOnTrain += 1.5*self.mass
        self.poezdokOnTrain+=1
        self.averageTime.append(self.Path/(trainspeed+count_magistral*50))
        self.averageTimeonTrain.append(self.Path/(trainspeed+count_magistral*50))
        print("Поезд доехал за ", self.Path /
              (trainspeed+count_magistral*50), " часов")

    def car(self):
        path = self.Path
        # кол-во магистралей было пройдено
        count_magistral = 0
        #время из-за поломки
        timePolomka=0
        # реализация пути
        while path > 0:
            avtospeed = 70
            #шанс на поломку
            polomka = random.randint(0, 500)
            if polomka < 5:
                print("Автомобиль поломался во время езды,для восстановления нужно время")
                timePolomka+=random.randint(1,3)
            # шанс на поломку или аварию,снижение дохода в этом случаи,резкий выход из функции,увеличивается потеря из-за аварий
            Avaria = random.randint(0, 1000)
            if Avaria < 5:
                print("Автомобиль пал во время езды,деньги идут в минус")
                self.doxodOnCar -= 0.5*self.mass
                self.lossAvaria += 1
                self.lossAvariaonCar += 1
                return
            # шанс на выход в магистраль
            magistral = random.randint(0, 100)
            if magistral < 10:
                avtospeed += 30
                count_magistral += 1
            # снижается путь,якобы прошел час езды
            path -= avtospeed
        # если все закончилось успешно
        print("Ваш Автомобиль доехал до конца и отдал груз.  ")
        # доход на этом транспорте
        self.doxodOnCar += 0.5*self.mass
        self.poezdokOnAvto+=1
        self.averageTime.append(self.Path/(avtospeed+count_magistral*30)+timePolomka)
        self.averageTimeonCar.append(self.Path/(avtospeed+count_magistral*30)+timePolomka)
        print("Автомобиль доехал за ", self.Path /
              (avtospeed+count_magistral*30)+timePolomka, " часов")

    def printAll(self):
        print("Среднее время поездок: ", mean(self.averageTime), " часов")
        print("Среднее время поездок на самолёте: ", mean(self.averageTimeonAirplane), " часов")
        print("Среднее время поездок на поезде: ", mean(self.averageTimeonTrain), " часов")
        print("Среднее время поездок на автомобиле: ", mean(self.averageTimeonCar), " часов\n")
        
        print("Доход на самолете(в усл.ед.):",self.doxodOnAirplane)
        print("Доход на поезде(в усл.ед.):",self.doxodOnTrain)
        print("Доход на автомобиле(в усл.ед.):",self.doxodOnCar)
        print("Итоговый доход(в усл.ед.):", self.doxodOnAirplane + self.doxodOnTrain + self.doxodOnCar,"\n")

        print("Количество аварий:", self.lossAvaria)
        print("Количество аварий на самолете:", self.lossAvariaonAirplane)
        print("Количество аварий на поезде:", self.lossAvariaonTrain)
        print("Количество аварий на автомобиле:", self.lossAvariaonCar,"\n")

        print("Поездок на самолете:",self.poezdokOnAirplane)
        print("Поездок на поезде:",self.poezdokOnTrain)
        print("Поездок на автомобиле:",self.poezdokOnAvto)
        print("Итоговое количество удачных поездок:",self.poezdokOnAirplane+self.poezdokOnTrain+self.poezdokOnAvto,"\n")


someImitation = Imitation()
a=input("Сколько тестов провести ?\n")

for i in range(int(a)):
    path = random.randint(300, 2000)
    mass = random.randint(1, 10)
    print("Был получен заказ: {} км, {} тонн".format(path, mass))
    someImitation._init_(path, mass)
    #sleep(3)
    print("-"*30)
    if i == int(a)-1:
        someImitation.printAll()

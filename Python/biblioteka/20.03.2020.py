import sqlite3
import argparse
import sys
conn = sqlite3.connect("biblioteka.sqlite")
c = conn.cursor()
try: 
    c.execute('''CREATE TABLE book
    (id_book INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name_book text, author text, yearOfPublication INTEGER, count INTEGER, theme text, FOREIGN KEY (id_book) REFERENCES book_distribution(id_book))''')
    c.execute('''CREATE TABLE book_distribution(
        id_book INTEGER ,
        id_reader INTEGER ,
        data_distribution TEXT)''')
    c.execute('''CREATE TABLE reader(
        id_reader INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        lastName TEXT,
        firstName TEXT,
        patronymic TEXT,
        telephone TEXT,
        adress TEXT,
        FOREIGN KEY (id_reader) REFERENCES book_distribution(id_reader)
        )''')
except Exception:
    print("таблицы уже созданы")
exit_from_programm=False
while exit_from_programm==False:
    vibor=input('''Выбор:
    1.Книга
    2.Выдача
    3.Читатель
    0.Выход
    ''')
    if vibor=="1":
        kolvoID = 0
        for i in c.execute('SELECT * FROM book '):
            kolvoID += 1
        id_book= kolvoID + 1
        name_book = input("Введите имя книги: ")
        author = input("Введите автор: ")
        year_of_publication = input("Введите год публикации: ")
        count = input("Введите количество: ")
        theme = input("Введите тему: ")
        table = [(id_book,name_book,author,year_of_publication,count,theme)] 
        c.executemany(
                ''' INSERT OR REPLACE INTO book VALUES (?,?,?,?,?,?)''', table)
        conn.commit()
    if vibor=="2":
       id_book=input("Введите ID Книги: ")
       id_reader=input("Введите ID Читателя: ")
       data= input("Введите дату(год\месяц\день): ")

       c.execute(
                ''' INSERT OR REPLACE INTO book_distribution VALUES (?,?,?)''', id_book,id_reader,data)
       conn.commit()
    if vibor=="3":
        kolvoID = 0
        for i in c.execute('SELECT * FROM reader '):
            kolvoID += 1
        id_reader= kolvoID + 1
        last_name = input("Введите Фамилию: ")
        first_name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")
        number = input("Введите номер телефона: ")
        adress = input("Введите адрес: ")
        
        
        table = [(id_reader,last_name,first_name,patronymic,number,adress)]
        c.executemany(
                ''' INSERT OR REPLACE INTO reader VALUES (?,?,?,?,?,?)''', table)
        conn.commit()        
    if vibor=="0":
        exit_from_programm=True

conn.close()
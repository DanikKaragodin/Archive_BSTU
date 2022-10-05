import sqlite3
import argparse
import sys
conn = sqlite3.connect("biblioteka.sqlite")
c = conn.cursor()
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

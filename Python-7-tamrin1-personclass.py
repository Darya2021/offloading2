# تمرین جلسه 7- کلاسی برای یک شخص
import sqlite3

class Person:

    def __init__(self, name, last_name, email, age):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.age = age

    def insert(self):

        connection = sqlite3.connect("1.db")

        cursor = connection.cursor()

        query = f'insert into person values("{self.name}","{self.last_name}",\
        "{self.email}", "{self.age}")'

        cursor.execute(query.format(name, last_name, email, age))
        connection.commit()
        connection.close()
        print("new record add to person table")


name = input("enter a name: \n")
last_name = input("enter lastname: \n")
email = input("enter email: \n")
age = input("enter age: \n")

person1 = Person(name, last_name, email, age)
person1.insert()

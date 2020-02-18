import sqlite3
import time

class Car():

    def __init__(self, company, model, year, kind, color):

        self.company = company
        self.model = model
        self.year = year
        self.kind = kind
        self.color = color

    def __str__(self):

        return "\nCompany: {}\nModel: {}\nYear: {}\nKind: {}\nColor: {}\n".format(self.company, self.model, self.year, self.kind, self.color)

class Garage():

    def __init__(self):

        self.create_connection()

    def create_connection(self):

        self.connection = sqlite3.connect("garage.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists cars (company TEXT, model TEXT, year INT, kind TEXT, color INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def cut_down_connection(self):

        self.connection.close()

    def show_cars(self):

        query = "select * from cars"
        self.cursor.execute(query)
        cars = self.cursor.fetchall()

        if len(cars) == 0:
            print("There is no car at garage!")

        else:

            for i in cars:
                car = Car(i[0], i[1], i[2], i[3], i[4])
                print(car)

    def query_car(self, c):

        query = "select * from cars where company = ?"
        self.cursor.execute(query, (c, ))
        cars = self.cursor.fetchall()

        if len(cars) == 0:
            print("There is no car at garage!")

        else:
            car = Car(cars[0][0], cars[0][1], cars[0][2], cars[0][3], cars[0][4])
            print(car)

    def add_car(self, car):

        query = "insert into cars values(?,?,?,?,?)"
        self.cursor.execute(query, (car.company, car.model, car.year, car.kind, car.color))
        self.connection.commit()

    def delete_car(self, name):

        query = "delete from cars where company = ?"
        self.cursor.execute(query, (name, ))
        self.connection.commit()

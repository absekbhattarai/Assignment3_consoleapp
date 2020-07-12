import csv
import pandas as pd
from time import sleep
import pickle
import os


class Academy:
    name : ''
    age : 0
    course : ''
    fee : 0
    col_names = ['name',
                 'age',
                 'course',
                 'fee']

    def admission(self):
        print("which of the course you are interested in ?")
        print("1.Python | course code - 001")
        print("2.Java | course code - 002")
        print("3.PHP | course code - 003")
        print("4.Swift | course code - 004")
        while True:
            choice = input("enter the COURSE CODE if you want to view details:  ")
            if choice in ('001', '002', '003', '004'):
                if choice == '001':
                    print("DETAILS ABOUT COURSE")
                    print("You have selected : Python")
                    print("Course Hours: 70 hours")
                    print("Time: 10:30 AM")
                    print("Lecture By: Mr. Shrwana Paudel ")
                    self.register()
                elif choice == '002':
                    print("DETAILS ABOUT COURSE")
                    print("You have selected : JAVA ")
                    print("Course Hours: 63 hours")
                    print("Time: 2 PM")
                    print("Lecture By: Mr. Nabin Paudel")
                    self.register()
                elif choice == '003':
                    print("DETAILS ABOUT COURSE")
                    print("You have selected : PHP")
                    print("Course Hours: 90")
                    print("Time:")
                    print("Lecture By: ")
                    self.register()

                elif choice == '004':
                    print("DETAILS ABOUT COURSE")
                    print("You have selected : Swift")
                    print("Course Hours: ")
                    print("Time: 7 AM")
                    print("Lecture By: Mr. Sita Ram Gautam")
                    self.register()

                break
            else:
                print("Invalid choice.")

    def register(self):
        print("Do you want to register for the course? ")
        while True:
            choice = input("Press 1 for'YES' and 0 for 'NO' :  ")
            if choice in ('0', '1'):
                if choice == '0':
                    print("BYE")
                elif choice == '1':

                    register_details()
                break
            else:
                print("Invalid choice.")
def register_details():
    print("Please fill up the form.")
    print("Registeration fee is Rs.2000 and you can pay it in two install of Rs.1000 each.")
    # self.name = input("Enter your name : ")
    # self.age = int(input("Enter your age : "))
    # self.course = input("Enter the course you have selected: ")
    # self.fee = int(input("Enter the amount you want to pay.(Remember we accept 1000 or 2000 only"))
    # print("Registered")
    # with open('details.csv', 'a', newline='') as file:
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    course = input("Enter the course you have selected: ")
    fee = int(input("Enter the amount you want to pay.(Remember we accept 1000 or 2000 only"))
    print("Registered")

        # writer = csv.writer(file)
        # writer.writerow(["Name", "Age", "Course Name", "fee", "Remaining fee"])

    info = pd.DataFrame([[name, age, course, fee]], columns=['Name', 'Age', 'Course Name', 'fee'])
    info.to_csv('details.csv', mode='a', header=False, index=False)
        # writer.writerow([name, age, course, fee])
    print("YAY you are registered.")
    print("Here's your details")

    with open('details.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    intro()

def update_details():
        up = pd.read_csv('details.csv')
        print(up)
        edit = int(input("Enter the row to be edited: "))
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        course = input("Enter your course: ")
        fee = int(input("Enter amount: "))
        if fee == 1000 or fee == 2000:
            fee1 = fee
        else:
            fee1 = int(input("Enter amount(1000or 2000): "))

        up.loc[edit] = [name, age, course, fee1]
        up.to_csv("details.csv", header=True, index=False)
        return up
def graduated():
    # n = int(input("DID YOU COMPLETE YOUR COURSE? 1 for yes 0 for no"))
    # if n == 1:
    #     up = pd.read_csv('details.csv')
    #     print(up)
    #
    # else:
    #     pass
    up1 = pd.read_csv('details.csv')
    print(up1)
    edit1 = int(input("Enter the row to be edited: "))
    up1.loc[edit1] = ["congrats", "you", "Gratdate", 0]
    up1.to_csv("details.csv", header=True, index=False)
    print(up1)
    return up1


def intro():
    print("Welcome to console application for an IT Academy\n ")
    print("Courses we offer : \n")
    print("1.Python")
    print("2.Java.")
    print("3.PHP")
    print("4.Swift")
    print("Are you interested in any of the above course?")
    print("OR if  your are already the member of the Academy")
    print("01. Update")
    print("02. Details")
    print("03. Delete")
    print("04. Graduated?")
    while True:
        choice = input(
            "Press 1 for'YES' and 0 for 'NO' for registeration, 01 to 'TO UPDATE', 02 for 'DETAILS', 03 to 'DELETE', 04 if GRATUATED ")
        if choice in ('0', '1', '01', '02', '03', '04'):
            if choice == '0':
                print("BYE")
            elif choice == '1':
                xyz = Academy()
                xyz.admission()
            elif choice == '01':
               update_details()

            elif choice == '02':
                display = pd.read_csv("details.csv")
                print(display.head())

            elif choice == '03':
                data = pd.read_csv("details.csv")
                print(data)
                name = int(input("Enter the row to be deteled:  "))

                data.drop(index = name, inplace = True)
                data.to_csv("details.csv", header=True, index=False)
                print(data)
            elif choice == '04':
                graduated()

            break
        else:
            print("Invalid choice.")

intro()



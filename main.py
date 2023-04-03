import sqlite3
from prettytable import from_db_cursor

#This creates a new database called student_test
connection = sqlite3.connect('students_test.db')

cursor = connection.cursor()

#Use this function to create a table named students
#Fields = id, name, surname, studentID

def create_table():
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS students (

    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    middle_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    student_id INTEGER NOT NULL CHECK (student_id > 0)

    )
    """)    

#Insert new student
def insert_value(name, surname, middle_name, student_id):

    cursor.execute('SELECT * FROM students ORDER BY id DESC LIMIT 1')
    last_row = cursor.fetchone()
    primary_id = 1 + (last_row[0])
   
    cursor.execute("INSERT INTO students (id, name, middle_name, surname, student_id) VALUES (?, ?, ?, ?, ?)",(primary_id, name, middle_name, surname, student_id) )
    connection.commit()

#Display all students
def display_all():
    data = cursor.execute("SELECT * FROM students")
    table = from_db_cursor(cursor)    
    print(table)

    

#Select students by full name
def select_by_name(name):
    data = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    table = from_db_cursor(cursor)    
    print(table)   

#Search student id
def select_by_id(student_id):
    data = cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    table = from_db_cursor(cursor)    
    print(table)   

#Delete By name
def delete_by_name(name):
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    connection.commit()

#Delete by name like
def select_by_name_like(name):
    name1 = "%"+name+"%"
    data = cursor.execute("SELECT * FROM students WHERE name LIKE ?", (name1,))
    table = from_db_cursor(cursor)    
    print(table)   

#Main Menu
def main_menu():  
    
    while True:
        print("""
        ----------------
        | Main Menu:
        ----------------
        |1: Dislpay All
        |2: Search Name
        |3: Search Student ID
        |4: Delete Name
        |5: Add new Student
        |6: Exit
        
        """)
        
        choice = int(input("Please choose> "))

        if choice == 1:
            display_all()

        elif choice == 2:
            print(" ")
            name = input("Enter Name> ")
            select_by_name_like(name)

        elif choice == 3:
            print(" ")
            student_id = input("Enter Student ID> ")
            select_by_id(student_id)

        elif choice == 4:
            print(" ")
            name = input("Enter Name To Delete> ")
            delete_by_name(name)

        elif choice == 5:
            print(" ")
            name = input("Enter Name> ")
            middle_name = input("Enter Middle Name> ")
            surname = input("Enter Surname> ")
            student_id = input("Enter Student ID> ")
            insert_value(name, surname, middle_name, student_id)

        elif choice == 6:
            break
            

            

main_menu()
connection.close()
import mysql.connector

# -------Sql connection-------
def connect_db():
    return mysql.connector.connect(
        host = "localhost",
        user="root",
        password = "YOUR_PASSWORD",
        database = "library_db"
        )

# ------View Students-------

def view_students(mycursor):
    mycursor.execute("SELECT * FROM students")
    rows = mycursor.fetchall()
    if not rows:
        print("No students found")
    else:
        for row in rows:
            print(row)

# --------Add Students---------
def add_student(mycursor,mydb):
    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
        if(age <= 0):
            print("Age must be Positive !")
            return
    except ValueError:
        print("Invalid age!!")
        return 
    course_id = input("Enter course_id (or leave blank): ")

    if course_id == "":
        course_id = None
        
    sql = "INSERT INTO students (name,age,course_id) VALUES (%s,%s,%s)"
    values = (name,age,course_id)

    mycursor.execute(sql,values)
    mydb.commit()

    print("Student successfully added!") 


# ---------Update Student-------------
def update_student(mycursor,mydb):
    try:
        student_id = int(input("Enter student id: "))
        new_age = int(input("Enter new age: "))
    except ValueError:
        print("Invalid Inputs!")
        return
    sql = "UPDATE students SET age = %s WHERE id = %s"
    values = (new_age,student_id)

    mycursor.execute(sql,values)
    mydb.commit()

    if mycursor.rowcount == 0:
        print("Student not found")
    else:
        print("Student updated successfully")

# ---------------Delete Student-------------
def delete_student(mycursor,mydb):
    try:
        student_id = int(input("Enter student id you want to delete:"))
    except ValueError:
        print("Invalid id!")
        return
    sql = "DELETE FROM students WHERE id = %s"
    values = (student_id,)

    mycursor.execute(sql,values)
    mydb.commit()

    if mycursor.rowcount == 0:
        print("Student not found")
    else:
        print("Student deleted successfully!!")

# ------------View Students With Course----------
def view_students_with_course(cursor):
    query = """
            SELECT students.id , students.name,students.age , courses.course_name
            FROM students LEFT JOIN courses 
            ON students.course_id = courses.course_id
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    if not rows:
        print("No records found.")
    else:
        for row in rows:
            print(row)
    

# -----------MAIN MENU--------------
def main():
    db = connect_db()
    cursor = db.cursor()
    while True:
        print("\n------Student Management System------------")
        print("1. View Students")
        print("2. Add Student")
        print("3. Update Student Age")
        print("4. Delete Student")
        print("5. View Students with Course")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_students(cursor)
        elif choice =="2":
            add_student(cursor,db)
        elif choice == "3":
            update_student(cursor,db)
        elif choice == "4":
            delete_student(cursor,db)
        elif choice == "5":
            view_students_with_course(cursor)
        elif choice == "6":
            print("Exiting Program....")
            break
        else:
            print("Invalid Choice !! Try Again.")
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

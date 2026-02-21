Student Management System (Python + MySQL)
📌 Overview
A CLI-based Student Management System built using Python and MySQL to manage student records with relational database design.

🚀 Features
Add Student

View Students

Update Student Age

Delete Student

View Students with Course (JOIN query)

Input validation and error handling

Transaction management using commit()

🛠 Technologies Used
Python

MySQL

mysql-connector-python

🗄 Database Design
students table (id, name, age, course_id)

courses table (id, course_name)

Foreign key relationship between students and courses

▶ How to Run
Install dependencies:

Code

pip install -r requirements.txt
Configure database credentials inside connect_db().

Run:

Code

python main.py

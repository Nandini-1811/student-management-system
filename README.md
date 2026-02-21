# Student Management System (Python + MySQL)

## 📌 Overview
A CLI-based Student Management System built using Python and MySQL to manage student records with relational database design and proper transaction handling.
Designed using relational database principles and normalized schema structure.

---

## 🚀 Features
- Add Student
- View Students
- Update Student Age
- Delete Student
- View Students with Course (JOIN query)
- Input validation and error handling
- Transaction management using commit()

---

## 🛠 Technologies Used
- Python
- MySQL
- mysql-connector-python

---

## 📂 Project Structure
```
student-management-system/
│
├── main.py
├── connect_db.py
├── requirements.txt
└── README.md
```

---


## 🗄 Database Design

### Students Table
- id (Primary Key)
- name
- age
- course_id (Foreign Key)

### Courses Table
- id (Primary Key)
- course_name

✔ Foreign key relationship between students and courses  
✔ Relational schema implementation  

---


## ▶ How to Run

### 1. Install Dependencies
```pip install -r requirements.txt```


### 2. Configure Database
Update your MySQL credentials inside `connect_db()` function.

### 3. Run the Application
```python main.py```


---

## 📚 Concepts Demonstrated
- CRUD Operations
- SQL JOIN
- Foreign Key Relationships
- Transaction Handling
- Structured Python Functions
- Modular Database Connection

---

Developed by Nandini Goel




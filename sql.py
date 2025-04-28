import sqlite3

## Connect to sqllite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record , create table , retrieve
cursor = connection.cursor()

# create the table 
table_info = """
Create table STUDENT(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);

"""

cursor.execute(table_info)

# Insert Some more records

cursor.execute('''Insert Into STUDENT values('kiran', 'SocialScience' , 'A' , 90)''')
cursor.execute('''Insert Into STUDENT values('Harsh', 'Hindi' , 'A' , 98)''')
cursor.execute('''Insert Into STUDENT values('Adi', 'Maths' , 'A' , 100)''')
cursor.execute('''Insert Into STUDENT values('Hina', 'Science' , 'A' , 85)''')

# Display all the record
print("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

# Close the connection

connection.commit()
connection.close()
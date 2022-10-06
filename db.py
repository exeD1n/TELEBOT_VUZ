# Подключение к базе данных

import pyodbc 

connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=85.236.170.148,444;Database=PythonBotPguty;username=stud;password=stud')
cursor = connection_to_db.cursor()
cursor.execute('SELECT subject, age FROM Subject')
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.subject)
connection_to_db.close()
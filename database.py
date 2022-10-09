# Подключение к базе данных
import pymysql

mySQLServer = 'localhost'
myDataBase = 'PgutyBot'
user = 'root'
passwodr = ''
try:
    connection = pymysql.connect(
        host = mySQLServer,
        port = 3306,
        database = myDataBase,
        user = user,
        password = passwodr,
        cursorclass = pymysql.cursors.DictCursor
        )
    print('succesfully conneted')

    try:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM Rating;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                if row['idSubject'] == 1 and row['name_group']=='ИВТ26у':
                    print(row)
    finally:
        connection.close()


except Exception as ex:
    print('Connection refused')
    print('ex')


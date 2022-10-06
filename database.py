# Подключение к базе данных
# Попытка от Егора
from select import select
import pymysql

mySQLServer = 'localhost'
myDataBase = 'sakila'
user = 'root'
passwodr = 'ForprojectPguty'
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
    print("#" * 20)

    try:
        with connection.cursor() as cursor:
            # select_all_rows = "SELECT * FROM actor;"
            # cursor.execute(select_all_rows)
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row)
            # print("#" * 20)
    finally:
        connection.close()


except Exception as ex:
    print('Connection refused')
    print('ex')


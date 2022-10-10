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
            s = []
            for row in rows:
                # print(row['name_group'])
                s.append(row['name_group'])
            n = []
            for i in s:
                if i not in n:
                    n.append(i)
            print(n)
                    
    finally:
        connection.close()


except Exception as ex:
    print('Connection refused')
    print('ex')


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
            select_name_grup = "SELECT * FROM Rating;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()
            s = []
            for row in rows:
                # print(row['name_group'])
                s.append(row['name_group'])
            name_group = []
            for i in s:
                if i not in name_group:
                    name_group.append(i)
            print(name_group)
            
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Subject;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()
            name_subject = {}
            i = 1
            for row in rows:
                print(row['Subject'])
                    
    finally:
        connection.close()


except Exception as ex:
    print('Connection refused')
    print('ex')


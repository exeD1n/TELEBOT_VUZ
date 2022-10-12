import pymysql

mySQLServer = 'localhost'
myDataBase = 'PgutyBot'
user = 'root'
passwodr = ''
try:
    connection = pymysql.connect(host = mySQLServer,port = 3306,database = myDataBase,user = user,password = passwodr,cursorclass = pymysql.cursors.DictCursor)
    print('succesfully conneted')

    try:
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Rating;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()
            all_name_group = [] # Список всех групп
            for row in rows:
                all_name_group.append(row['name_group'])
            name_group = []
            for i in all_name_group:
                if i not in name_group:
                    name_group.append(i)       
            print(name_group)
            
            
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Subject;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()
            name_subject = {}
            for row in rows:
                key, value = row['idSubject'], row['Subject']
                name_subject[key] = value
            print(name_subject)    
               
            
    finally:
        connection.close()


except Exception as ex:
    print('Connection refused')
    print('ex')


import pymysql
from config import host, port, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    print("successfully connection")
    print('#' * 20)
    try:
        cursor = connection.cursor()
        # create table
        with connection.cursor() as cursor:
            createa_table_query = "CREATE TABLE `users2`(id int AUTO_INCREMENT, name varchar(32), email varchar(32), PRIMARY KEY (id))"
            cursor.execute(createa_table_query)
            print('Table created')

        #insert
        # with connection.cursor() as cursor:
        #     insert_querty = "INSERT INTO `users2` (id, name, email) VALUES('23', 'Mia2', 'mai@gmail.com');"
        #     cursor.execute(insert_querty)
        #     connection.commit()
        #     print('insert-data')

        #select all data table
        # with connection.cursor() as cursor:
        #     select_all = "SELECT * FROM `users2`"
        #     cursor.execute(select_all)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print('#' * 20)
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

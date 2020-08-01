from conection.conection import conect_mysql

database, cursor = conect_mysql()

cursor.execute("CREATE DATABASE IF NOT EXISTS PLATOPEDIA")
cursor.close()
database.close()

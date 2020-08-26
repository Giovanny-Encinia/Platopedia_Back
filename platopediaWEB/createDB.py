import psycopg2

database = psycopg2.connect(
    user="postgres", host="localhost", password="&PA2PA6BY9&&{1605497gio}"
)
database.autocommit = True
cursor = database.cursor()
cursor.execute("CREATE DATABASE PlatopediaFoodInfo_v2;")
cursor.close()
database.close()
print("\n SE HA CREADO LA BASE DE DATOS!! \n")


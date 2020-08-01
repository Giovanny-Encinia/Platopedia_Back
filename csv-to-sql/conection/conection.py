def conect_mysql(user="root", host="127.0.01", password=":PA2PA6BY9::gio&{zai}"):
    """
    This function makes a conection with a mysql database
    We can change the user, host, and password
    """
    import mysql.connector

    database = mysql.connector.connect(user=user, host=host, password=password)
    cursor = database.cursor(buffered=True)
    return (database, cursor)


if __name__ == "__main__":
    conect_mysql()

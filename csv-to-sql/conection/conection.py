def conect_mysql():
    """
    This function makes a conection with a mysql database
    """
    import mysql.connector

    database = mysql.connector.connect(
        user="root", host="127.0.0.1", password=":PA2PA6BY9::gio&{zai}"
    )
    cursor = database.cursor(buffered=True)
    return (database, cursor)


if __name__ == "__main__":
    conect_mysql()

""" import mysql.connector

mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MxR2epTP",
) """
""" my_cursor = mysql_db.cursor() """

#line below is commented out so the db isn't accidently created again if this file runs
""" my_cursor.execute("CREATE DATABASE mapps") """

""" my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db) """
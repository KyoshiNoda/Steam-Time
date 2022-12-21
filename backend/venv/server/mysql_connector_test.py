"""
Use of mysql database containing information about films
"""
import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    port="3306",
    database="sakilav2221"
)

cursor = mydb.cursor()

query = ("SELECT filmID, title, description FROM film")

cursor.execute(query)

for (filmID, title, description) in cursor:
    print("{}\t | {}\t | {}\t".format(filmID, title, description))

cursor.close()
mydb.close()
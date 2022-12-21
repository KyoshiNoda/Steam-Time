"""
Use of mysql database containing information about films
"""
import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    port="3306",
    database="steam_user"
)

cursor = mydb.cursor()

sql = """INSERT INTO owned_games (appID, name, playtimeForever) VALUES ({}, "{}", {})""".format(122, 'new game', 192)


cursor.execute(sql)
mydb.commit()

print(cursor.rowcount, "record inserted")

cursor.close()
mydb.close()
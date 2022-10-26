import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()
try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Grapes')")
cursor.execute("insert into list (description) values ('Strawberry')")
cursor.execute("insert into list (description) values('Blueberry')")
cursor.execute("insert into list (description) values ('Raspberry')")
cursor.execute("insert into list (description) values ('Tomatoes')")
connection.commit()
connection.close()
#managing functions for database

import sqlite3

connection = sqlite3.connect("shopping_list.db")

def get_items():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    items = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return items

def add_item(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into list (description) values ('{description}')")
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()
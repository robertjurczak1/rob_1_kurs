import sqlite3

connection = sqlite3.connect("akwarium.db")
cursor = connection.cursor()
new_tank = cursor.execute("UPDATE fish SET tank_number = 3 WHERE name ='Nemo'")
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
rows2 = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name = 'Nemo'").fetchall()
usuwam = cursor.execute("DELETE FROM fish WHERE name = 'Nemo'")
print(rows)
print(rows2)
connection.commit()
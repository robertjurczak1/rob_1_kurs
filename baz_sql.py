import sqlite3

connection = sqlite3.connect("akwarium.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('Nemo', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cutterfish', 7)")
connection.commit()
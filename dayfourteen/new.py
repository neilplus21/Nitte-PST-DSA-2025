import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS movie(title,year,score)")

cursor.execute("INSERT INTO movie VALUES ('SAMPLE 1',2024,10)")

connection.commit()

res = cursor.execute("SELECT year,title FROM movie")

for row in res:
    print(row)
    
connection.close()


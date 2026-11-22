import sqlite3
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///books.db')

with engine.connect() as conn:
  result = conn.execute(text("SELECT title FROM books ORDER by title"))
  for row in result:
    print(row[0[)
    
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open('books2.csv', 'r', newline='') as file:
  reader = csv.reader(file)
  next(reader)  

for row in reader:
  cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', row)

conn.commit()
conn.close()


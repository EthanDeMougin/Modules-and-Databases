import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open('books2.csv', 'r', newline='') as file:
  reader = csv.reader(file)
  next(reader)  

for row in reader:
  cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', row)

conn.commit()
conn.close()


import mysql.connector

conn = mysql.connector.connect (host=' ', user=' ', passwd=' ', port=' ', database='chinook')

cursor = conn.cursor()

cursor.execute('SELECT * FROM albums')

records = cursor.fetchall()

print(records)

conn.close

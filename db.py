import mysql.connector

conn = mysql.connector.connect (host='mysql.cahulxfuge2f.us-east-1.rds.amazonaws.com', user='guilherme', passwd='25892589', port='3306', database='chinook')

cursor = conn.cursor()

cursor.execute('SELECT * FROM albums')

records = cursor.fetchall()

print(records)

conn.close

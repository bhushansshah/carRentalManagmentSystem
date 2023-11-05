import mysql.connector
conn = mysql.connector.connect(host='localhost', password='PetronesTower1.', user='root', database='CarRentalDB')
if conn.is_connected():
    print("Connection established...")

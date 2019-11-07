import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lulu",
    port="3302",
    database="mydatabase")

mycursor=mydb.cursor()

sql = "SELECT * FROM customers LIMIT 3"

mycursor.execute(sql)

myres=mycursor.fetchall()
for x in myres:
  print(x)


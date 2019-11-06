import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lulu",
    port="3302",
    database="mydatabase")

mycursor=mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
'''myres=mycursor.fetchall()
for x in myres:
  print(x)'''

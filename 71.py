import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lulu",
    port="3302",
    database="mydatabase")

mycursor=mydb.cursor()

sql = "SELECT * FROM customers WHERE address Like '%don%'"

'''val = ("mich", "vally")

mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)'''

mycursor.execute(sql)
myres=mycursor.fetchall()
for x in myres:
    print(x)
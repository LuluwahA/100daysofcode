#1
'''
f = open("c1.txt", "r")
print(f.read())
f.close()
f = open("c1.txt", "a")
f.write("The best way we learn anything is by practice and exercise questions")
f.close()
f = open("c1.txt", "r")
print(f.read())'''


#2

import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lulu",
    port="3302",
    database="myemployee"
   )

mycursor=mydb.cursor()

'''sql="INSERT INTO employee(firstname,lastname,age,gender,salary)VALUES(%s,%s,%s,%S,%s)"
val=[
('ahmed','ali','30','male','10000'),
('khalid','muhammad','34','male','7000'),
('nourah','saleh','29','female','7000')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"table is ready")'''

'''
mycursor.execute("SELECT firstname, gender,salary FROM employee")
r=mycursor.fetchall()
for x in r:
    print(x)'''

'''
sql="SELECT * FROM employee ORDER BY firstname DESC"
mycursor.execute(sql)
r=mycursor.fetchall()
for x in r:
    print(x)'''


sql="DELETE FROM employee WHERE age=34"
mycursor.execute(sql)
print(mycursor.rowcount, "age 34 were deleted")
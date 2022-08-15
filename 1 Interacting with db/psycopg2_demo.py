import psycopg2
#connect to the db to start connection
connection=psycopg2.connect(
    host="localhost",
    database="example",
    user="postgres",
    password="postgres"
)
#creating a cursor
#these are ways through which we interact with postgresql databases
cursor = connection.cursor()
#execute query 1
cursor.execute("INSERT INTO table1 (id, first_name, last_name) VALUES (%s, %s, %s)",(3,"Faith","Mutheu"))

#execute query 2
cursor.execute("select * from table1")

#fet all attributes in the database mentioned as desired. 
rows=cursor.fetchall()
for r in rows:
    print("id {} first_name {} last_name {}".format(r[0],r[1], r[2]))
#rem to commit the changes - transaction
connection.commit()
#rem to close the cursor
cursor.close()
#close the connection
connection.close()
import psycopg2 

#set up a connection
connection=psycopg2.connect(
    host="localhost",
    database="udacity1",
    password="postgres",
    user="postgres"
)

#set up a cursor
cursor=connection.cursor()

cursor.execute("SELECT * FROM table1;")

rows=cursor.fetchall()

for r in rows:
    print("id {} first_name {} last_name {}".format(r[0], r[1], r[2]))

#close the cursor
cursor.close()
#close the connection
connection.close()
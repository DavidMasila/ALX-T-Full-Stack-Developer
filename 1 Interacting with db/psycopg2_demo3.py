import psycopg2 

#create a connection
connection=psycopg2.connect(
    host="localhost",
    database="udacity1",
    user="postgres",
    password="postgres"
)
#create cursor
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS table1")
#create execusions
cursor.execute("""
    CREATE TABLE table1(
        id INTEGER PRIMARY KEY,
        f_name VARCHAR(15) NOT NULL,
        l_name VARCHAR(15) NOT NULL
    );
""")

cursor.execute("INSERT INTO table1 (id, f_name, l_name) VALUES (%s, %s, %s);",(1,'David','Masila'))
cursor.execute("INSERT INTO table1 (id, f_name, l_name) VALUES (%s, %s, %s);",(2,'Antony','Masila'))
cursor.execute("INSERT INTO table1 (id, f_name, l_name) VALUES (%(id)s, %(f_name)s,%(l_name)s);",{
    'id':3,
    'f_name':'Faith',
    'l_name':'Mutheu'
})

#commit the changes
connection.commit()

#close the cursor
cursor.close()

#close the connection

connection.close()



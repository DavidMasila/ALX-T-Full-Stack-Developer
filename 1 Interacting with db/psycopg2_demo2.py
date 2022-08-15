import psycopg2 

#create a connection
connection=psycopg2.connect(
    host="localhost",
    database="udacity1",
    user="postgres",
    password="postgres"
)

#create a cursor
cursor=connection.cursor()

cursor.execute("""
    CREATE TABLE table2(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT false
    );
"""
)

#execute another 

cursor.execute("INSERT INTO table2 (id, completed) VALUES (%s, %s)",(1, True))

#commit
connection.commit()

#close the cursor
cursor.close() 

#close the connection
connection.close()


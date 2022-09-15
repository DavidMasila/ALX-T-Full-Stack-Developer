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
cursor.execute("DROP TABLE IF EXISTS table3")
#create execusions
cursor.execute("""
    CREATE TABLE table3(
        id INTEGER PRIMARY KEY,
        f_name VARCHAR(15) NOT NULL,
        l_name VARCHAR(15) NOT NULL
    );
""")

SQL="INSERT INTO table3 (id, f_name, l_name) VALUES (%(id)s, %(f_name)s,%(l_name)s);"
data1={
    'id':3,
    'f_name':'Faith',
    'l_name':'Mutheu'
}

data2={
    'id':1,
    'f_name':'David',
    'l_name':'Masila'
}

data3={
    'id':2,
    'f_name':'Antony',
    'l_name':'Masila'
}

cursor.execute(SQL, data1)
cursor.execute(SQL, data2)
cursor.execute(SQL, data3)

#commit the changes
connection.commit()

#close the cursor
cursor.close()

#close the connection

connection.close()



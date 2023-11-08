import psycopg2 
from psycopg2.extras import DictCursor

db_params = {
    "dbname" : "polban",
    "user" : "postgres",
    "password" : 1234 ,
    "host" : "localhost",
    "port" : "5432"
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor(cursor_factory=DictCursor)
    
    cursor.execute("SELECT nim,nama FROM mahasiswa")
    data= cursor.fetchall()
    
    for row in data:
        print(dict(row))
        
except (Exception, psycopg2.Error) as error:
    print("Eror while conneting to PostgreSQL:",error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
        
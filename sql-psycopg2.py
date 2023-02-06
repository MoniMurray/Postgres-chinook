import psycopg2


#connect to "chinook" database using the connect()
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database
cursor = connection.cursor()

#queries
#1. cursor.execute('SELECT * FROM "Artist"')
#2. cursor.execute('SELECT "Name" FROM "Artist"')
#3. cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
#4. cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
#5. cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
#6. cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["test"])



#fetch the results(multiple)
results = cursor.fetchall()

#fetch the results(single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)


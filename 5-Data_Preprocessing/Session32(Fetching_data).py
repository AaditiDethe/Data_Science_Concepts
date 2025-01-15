
#USING  PYTHON FETCHING DATA
#After installing with pip install psycopg2
import psycopg2 as pg2

#Create a connection with PostgreSQL
#'password' is whatever password you set, we set password in the istall
conn=pg2.connect(database='dvdrental',user='postgres',password='root')

#Establish connection and start cursor to be ready to query
cur=conn.cursor()

#Pass in a PostgreSQL query as a string
cur.execute("SELECT * FROM payment")

#Return  a tuple to the first row as Python objects
cur.fetchone()

#Return N number of rows
cur.fetchmany(10)

#Return ALL rows at once
cur.fetchall()

#To save and index results, assign it to a variable
data=cur.fetchmany(10)

conn.close()

###############################


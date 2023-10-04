import psycopg2

con = psycopg2.connect(
database="example",
user="postgres",
password="cp12345",
host="localhost",
port= '5432'
)


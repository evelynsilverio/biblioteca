import psycopg2
from psycopg2 import pool

#Crear un pool de conexiones
connection_pol = pool.SimpleConnectionPool(
    1, 20,
    database="biblioteca3a",
    user="postgres",
    password="chikis03",
    host="localhost",
    port="5432"
)

def conectar():
    return connection_pol.getconn()

def desconectar(conn):
    connection_pol.putconn(conn)

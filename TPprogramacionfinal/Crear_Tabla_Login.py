import sqlite3

conn=sqlite3.connect('login.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Pass TEXT,Producto TEXT,Precio IN NOT NULL,Metodo de pago TEXT )")
	conn.commit()
	c.close()
	conn.close()

create_table()
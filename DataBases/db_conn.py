import sqlite3
from sqlite3 import Error


def sql_connection(filename = ":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Conexion realizada a ", filename)
    except Error:
        print(Error)
        con = None 
    finally:
        return con


def sql_creartabla(con):
    try:
        cur = con.cursor()
        
        cur.execute("create table empleados(id integer primary key, nombre text, salario real, departamento text, categoria text, fechacontratacion text)")
        
        con.commit()
        
        print("Tabla creada")
    
    except sqlite3.OperationalError:
        print("La tabla ya existia")
        
    
    

def insertarempleados(con):
    try:
        
        cur = con.cursor()
        
        cur.execute("insert into empleados values(1, 'Pedri', 1000, 'Desarrollo', 'analista', '01-07-2015')")
        con.commit()
        cur.execute("insert into empleados values(2, 'Ansu Fati', 5000, 'Desarrollo', 'programador', '01-07-2015')")
        con.commit()
        cur.execute("insert into empleados values(3, 'Youssef', 3000, 'Desarrollo', 'becario', '01-07-2015')")
        con.commit()
        
        cur.execute("insert into empleados values(4, 'Bono', 2345, 'Desarrollo', 'becario', '15-03-2020')")
        con.commit()
        cur.execute("insert into empleados values(5, 'Kounde', 4500, 'Desarrollo', 'programador', '15-03-2020')")
        con.commit()
        cur.execute("insert into empleados values(6, 'Navas', 12000, 'Desarrollo', 'programador', '15-03-2020')")
        con.commit()
        cur.execute("insert into empleados values(7, 'Jordan', 6788, 'Desarrollo', 'programador', '15-03-2020')")
        con.commit()
        cur.execute("insert into empleados values(8, 'Idrissi', 976, 'Desarrollo', 'programador', '15-03-2020')")
        con.commit()
        
        
        print("Registro actualizado")
        
    except sqlite3.IntegrityError:
        print("Ya existe ese registro")


def actualizarbecario(con):
    try:
        
        cur = con.cursor()
        
        
        cur.execute("update empleados set categoria = 'programador' where categoria = 'becario' and fechacontratacion = '01-07-2015' ")
        con.commit()
    
        print("Registro actualizado")
    
    except sqlite3.OperationalError:
        print("No existe registro con esas condiciones")
    

def sueldostotales(con):
    try:
        
        cur = con.cursor()
        
        cur.execute("select sum(salario) from empleados where categoria = 'programador'")
        row = cur.fetchall()
    
        print(row)
        
        cur.execute("select sum(salario) from empleados where categoria = 'analista'")
        row = cur.fetchall()
    
        print(row)
    
    except sqlite3.OperationalError:
        print("Algo salio mal")




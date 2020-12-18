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
        
        cur.execute("create table productos(id integer primary key, nombre text, precioventa real, preciocoste real, stockactual real)") 
        con.commit()
   
        cur.execute("create table ventas(id integer primary key, codigo_producto_vendido integer , cantidad integer, ciudad text, importe real, precio real, foreign key (codigo_producto_vendido) references productos(id))") 
        con.commit()
        
        cur.execute("create table stock(cdgproducto integer primary key, almacen text, stock integer, foreign key (cdgproducto) references productos(id))") 
        con.commit()
        
        print("Tabla creada")
    
    except sqlite3.OperationalError:
        print("La tabla ya existia")
        
    
    
def importeventas(con):
    try:
        
        cur = con.cursor()
        print()
        print("De todas: ")
        cur.execute("SELECT sum(importe) from ventas")
        rows = cur.fetchall()
        print(rows)     
        con.commit()
        
        print("De Huelva: ")
        cur.execute("select sum(importe) from ventas where ciudad = 'Huelva' ")
        rows = cur.fetchall()
        print(rows)
        con.commit()
        
        print("De Sevilla: ")
        cur.execute("select sum(importe) from ventas where ciudad = 'Sevilla' ")
        rows = cur.fetchall()
        print(rows)
        con.commit()
        
    except sqlite3.OperationalError:
        print("Algo fue mal")
        
        
        
def actualizarventas(con):
    try:
        
        cur = con.cursor()

        cur.execute("update ventas set importe = cantidad * precio ")
        con.commit()
            
        
    except sqlite3.OperationalError:
        print("Algo fue mal")
    
    
    

def insertarventas2(con, dic):
    try:
        cur = con.cursor()
            
        cur.execute("insert into ventas values (?,?,?,?,?,?)", dic)
        con.commit()
    
    except sqlite3.IntegrityError as err:
        print("Error --> ", err )
        print("No se aniadieron los registros")
    


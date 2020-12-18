from DataBase_2.db_clases import sql_connection, sql_creartabla,\
    importeventas, insertarventas2, actualizarventas
con = sql_connection

dic = [(1,1,100,'Huelva',"Null",15),(2,1,100,'Sevilla',"Null",15),(3,2,100,'Sevilla',"Null",18),(4,2,100,'Sevilla',"Null",18),(5,2,100,'Huelva',"Null",18),(6,3,100,'Sevilla',"Null",21),(7,3,100,'Cordoba',"Null",21),(8,4,100,'Sevilla',"Null",24),(9,4,100,'Huelva',"Null",24),(10,4,100,'Cordoba',"Null",24)]

con = sql_connection("mi_erp.db")
cur = con.cursor()

sql_creartabla(con)

ventas = []
i=0
for ventas in dic:
    ventas=dic[i]
    i=i+1
    insertarventas2(con,ventas)
    
actualizarventas(con)

print("Registros actualizados")

importeventas(con)

con.close()
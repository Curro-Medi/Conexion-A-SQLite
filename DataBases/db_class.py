from DataBases.db_conn import sql_connection, sql_creartabla, insertarempleados,\
    actualizarbecario, sueldostotales
con = sql_connection("prueba.db")
cur = con.cursor()

sql_creartabla(con)

insertarempleados(con)

actualizarbecario(con)

sueldostotales(con)

con.close()
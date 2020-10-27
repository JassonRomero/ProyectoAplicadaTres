import pymssql
import psycopg2
import _sqlite3


#CONNECTION TO SQL SERVER
_sql_server = "163.178.107.10"
_sql_database = "Proyecto3AplicadaLSJ"
_sql_server_port = 1433
_sql_user = "laboratorios"
_sql_password = "KmZpo.2796"

#Connection to postgresql
_postgre_server='163.178.107.7'
_postgre_database='MundoNovedades_B55008'
_postgre_server_port=5432
_postgre_user="laboratorios"
_postgre_password="saucr.120"



#SQLITE SERVER CONECCTION
def sqlite_connection(sp):
    try:
        con = _sqlite3.connect('C:/Users/Usuario/Desktop/Informatica Aplicada/Proyecto 3/BD_SQLite_Bitacoras/MundoNovedades.db')
        cur= con.cursor()
        cur.execute(sp)
        con.commit()
    except IOError as e:
        print("ERROR: [0] Getting data from MSSQL: [1]".format(
            e.errno, e.strerror))

    # SQLITE SERVER CONECCTION


def sqlite_extraer_nombres(sp):
    try:
        con = _sqlite3.connect(
            'C:/Users/Usuario/Desktop/Informatica Aplicada/Proyecto 3/BD_SQLite_Bitacoras/MundoNovedades.db')
        cur = con.cursor()
        cur.execute(sp)
        data_return = cur.fetchall()
        con.commit()
        return data_return
    except IOError as e:
        print("ERROR: [0] Getting data from MSSQL: [1]".format(
            e.errno, e.strerror))

def sqlite_actualizarTrasaccionBitacoraExtraccion(sp):
    try:
        con = _sqlite3.connect(
            'C:/Users/Usuario/Desktop/Informatica Aplicada/Proyecto 3/BD_SQLite_Bitacoras/MundoNovedades.db')
        cur = con.cursor()
        cur.execute(sp)
        con.commit()
    except IOError as e:
        print("ERROR: [0] Getting data from MSSQL: [1]".format(
            e.errno, e.strerror))




#SQL SERVER CONNECTION FUNCTION
def mssql_connection():
    try:
        cnx = pymssql.connect(server=_sql_server, port=_sql_server_port,
                              user=_sql_user, password=_sql_password,
                              database=_sql_database)
        return cnx
    except:
        print('ERROR: MSSQL_CONNECTION')


#CALL ESTORED PROCEDURES FROM SQL SERVER

def get_data_from_sql(sp):
    try:
        con = mssql_connection()
        cur = con.cursor()
        cur.execute("EXECUTE {} ".format(sp))
        data_return = cur.fetchall()
        con.commit()
        return data_return

    except IOError as e:
        print("ERROR: [0] Getting data from MSSQL: [1]".format(
            e.errno, e.strerror))


#CALL ELIMINAR INFORMACION DE LAS TABLAS
def elimnarInfoTablasSQL(sp):
    try:
        con = mssql_connection()
        cur = con.cursor()
        cur.execute("EXECUTE {} ".format(sp))
        con.commit()

    except IOError as e:
        print("Error [0] Eliminar fallo en MSSQL: [1]".format(e.errno, e.strerror))


#PostreSql Connection
def postgressql_connection():
    try:
        cnx = psycopg2.connect("host="+_postgre_server+" dbname="+_postgre_database+" user="+_postgre_user+" password="+_postgre_password)
        return cnx
    except:
        print('Error: postgressql_connection')
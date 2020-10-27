import sys
import csv
import _sqlite3
from datetime import datetime
from Configuration import mssql_connection, get_data_from_sql, elimnarInfoTablasSQL, sqlite_connection,sqlite_extraer_nombres,sqlite_actualizarTrasaccionBitacoraExtraccion
from MundoNovedadesInsert import loader_csv_file_postgre






#EXTRACTOR CLIENTES
def clientesExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_CLIENTES]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDCLIENTE","NOMBRE","APELLIDO","EDAD","GENERO","DIRECCION"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the client_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close





#EXTRACTOR TARJETA
def tarjetaExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_Tarjeta]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDTARJETA","TIPO","NUMERO","MONTO","MONEDA"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the Tarjeta_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close





#EXTRACTOR TARJETA CLIENTE
def tarjetaClienteExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_Cliente_Tarjeta]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDCLIENTE","IDTARJETA"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the tarjeta_cliente_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close






#EXTRACTOR COMPRA
def compraExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_Compra]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDCOMPRA","MONTO","FECHA"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the compra_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close




#EXTRACTOR COMPRA CLIENTE
def compraClienteExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_Cliente_Compra]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDCLIENTE","IDCOMPRA"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the compra_client_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close






#EXTRACTOR TELEFONO CLIENTE
def telefonoClieteExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_Cliente_Telefono]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDCLIENTE","TELEFONO"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the telefono_client_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close






#EXTRACTOR CORREO CLIENTE
def correoClienteExtractor(nombreArchivo):
    try:
        query = "[dbo].[SP_OBTENER_Cliente_Correo]"

        con_sql = mssql_connection()

        data = get_data_from_sql(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:

            access = "w"
            newline = {"newline": ""}

            with open(nombreArchivo,access,**newline) as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)
                writer.writerow(
                    ["IDCLIENTE","CORREO"])

                for row in data:
                    #print(row)
                    writer.writerow(row)

    except IOError as e:
        print ("ERROR [0]  in the correo_cliente_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close

def eliminarTablas():
    try:
        query = "[dbo].[SP_delete_Cliente_Compra]"
        con_sql = mssql_connection()
        elimnarInfoTablasSQL(query)
        return True

    except IOError as e:
        print ("ERROR [0]  in the correo_cliente_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close

def generarNombreArchivo():
    now = datetime.now()
    nombreArchivo = str(now.date()) + "_"
    nombreArchivo += str(now.hour) + "_"
    nombreArchivo += str(now.minute) + "_"
    nombreArchivo += str(now.second)
    return nombreArchivo

def actualizarBitacoraExtraccionSQLite(nombreArchivo):

    try:
        query = "INSERT INTO TB_BITACORA_EXTRACCION (nombre)VALUES ('"+nombreArchivo+"')"
        con_sql = mssql_connection()
        sqlite_connection(query)
        return True

    except IOError as e:
        print ("ERROR [0]  in the correo_cliente_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close


def importarDatosPostgre():
    try:
        query = "SELECT nombre FROM TB_BITACORA_EXTRACCION where transaccion = 'N'"
        con_sql = mssql_connection()
        data = sqlite_extraer_nombres(query)

        if len(data) <= 0:
            print("No data")
            sys.exit(0)
        else:
            for row in data:
                #split nombre archivo con fecha
                tuplaNombreArchivo= str(row)
                vectorNombreFinal = tuplaNombreArchivo.split("\'", 2)
                nombreFinal = vectorNombreFinal[1]


                # split nombre archivo SIN fecha
                tuplaNombreArchivoSinFecha = str(row)
                vectorNombreFinalSinFecha = tuplaNombreArchivoSinFecha.split("\'", 2)

                vectorNombreFinalSinFecha2 = vectorNombreFinalSinFecha[1].split("_", 5)
                nombreFinalSinFecha = vectorNombreFinalSinFecha2[4]

                #print(nombreFinalSinFecha)
                #print(nombreFinal)

                nombreTabla= ""

                if nombreFinalSinFecha == "ClientesSQL.csv" :
                    nombreTabla = "Tienda.Cliente"
                if nombreFinalSinFecha == "TarjetaSQL.csv":
                    nombreTabla = "Tienda.Tarjeta"
                if nombreFinalSinFecha == "TarjetaClienteSQL.csv":
                    nombreTabla = "Tienda.Cliente_Tarjeta"
                if nombreFinalSinFecha == "CompraSQL.csv":
                    nombreTabla = "Tienda.Compra"
                if nombreFinalSinFecha == "CompraClienteSQL.csv":
                    nombreTabla = "Tienda.Cliente_Compra"
                if nombreFinalSinFecha == "TelefonoClienteSQL.csv":
                    nombreTabla = "Tienda.Cliente_Telefono"
                if nombreFinalSinFecha == "CorreoClienteSQL.csv":
                    nombreTabla = "Tienda.Cliente_Correo"

                loader_csv_file_postgre("ArchivosSQL/" + nombreFinal,nombreTabla)

                # inserta en la bitacora los archivos cargado en la BD postgre
                queryBitacoraInsertPostgre = "INSERT INTO TB_BITACORA_IMPORTAR (nombre)VALUES ('" + nombreFinal + "');"
                con_sql = mssql_connection()
                sqlite_actualizarTrasaccionBitacoraExtraccion(queryBitacoraInsertPostgre)


        #Actualiza el estado en la tabla extraccion estableciendo que este archivo ya no se debe enviar
        queryActualiza = "update TB_BITACORA_EXTRACCION set transaccion='S'"
        con_sql = mssql_connection()
        sqlite_actualizarTrasaccionBitacoraExtraccion(queryActualiza)

        



    except IOError as e:
        print("ERROR [0]  in the correo_cliente_extractor funct".format(e.errno, e.strerror))

    finally:
        con_sql.close




#LLAMADO DE METODOS
def  trasladoDeDatos():

    nombreArchivo =generarNombreArchivo()

    clientesExtractor("ArchivosSQL/"+nombreArchivo+"_ClientesSQL.csv")
    tarjetaExtractor("ArchivosSQL/"+nombreArchivo + "_TarjetaSQL.csv")
    tarjetaClienteExtractor("ArchivosSQL/"+nombreArchivo + "_TarjetaClienteSQL.csv")
    compraExtractor("ArchivosSQL/"+nombreArchivo + "_CompraSQL.csv")
    compraClienteExtractor("ArchivosSQL/"+nombreArchivo + "_CompraClienteSQL.csv")
    telefonoClieteExtractor("ArchivosSQL/"+nombreArchivo + "_TelefonoClienteSQL.csv")
    correoClienteExtractor("ArchivosSQL/"+nombreArchivo + "_CorreoClienteSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo+ "_ClientesSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo + "_TarjetaSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo +  "_TarjetaClienteSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo + "_CompraSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo + "_CompraClienteSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo + "_TelefonoClienteSQL.csv")
    actualizarBitacoraExtraccionSQLite(nombreArchivo + "_CorreoClienteSQL.csv")

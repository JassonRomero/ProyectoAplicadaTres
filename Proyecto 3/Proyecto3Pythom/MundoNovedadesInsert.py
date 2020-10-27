
from Configuration import postgressql_connection

def loader_csv_file_postgre(nombreArchivo, nombreTabla):
    try:
        con_postgre=postgressql_connection()
        cur=con_postgre.cursor()
        with open(nombreArchivo, 'r') as f:
            #salto linea
            next(f)
            cur.copy_from(f, nombreTabla, sep=',')
            con_postgre.commit()
    except IOError as e:
        print("ERROR {0}  in the loader_csv_file_postgre: {1}".format(e.errno, e.strerror))
    finally:
        con_postgre.close()


import PySimpleGUI as sg
import sys
from MundoNovedades import trasladoDeDatos, eliminarTablas,importarDatosPostgre


def metodoSalida():
    layout = [[sg.Text('                                                               ')],
            [sg.Button('Extraer', key=('validar')) , sg.Button('Importar',key=('importar')) , sg.Button('Eliminar Datos', key =("Eliminar"))],
            [sg.Text('                                                                   ')]]

    window = sg.Window('Proyecto3LuisStevenJasson', layout)


    while True:
        event, values = window.read()
        if event == 'Exit' or event is None:
            sys.exit()
        if event == 'validar':
            trasladoDeDatos()
            OperacionExitosa()
        if event == 'Eliminar':
            eliminarExitoso(eliminarTablas())
        if event == 'importar':
            importarDatosPostgre()
            OperacionExitosa()



def OperacionExitosa():
    sg.Popup('La operacion se realizó con exito')

def eliminarExitoso(validar):
    if validar ==True:
        sg.Popup('Se elimino con exito')
    else:
        sg.Popup('Se produjo un error')





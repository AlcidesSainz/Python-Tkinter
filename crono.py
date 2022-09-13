import sqlite3
from tkinter import *

proceso = 'after#0'

def iniciar(hora = 00,minuto=00,segundo=00):
    global proceso
    global guardar_hora
    global guardar_minuto
    global guardar_segundo
    guardar_hora = hora
    guardar_minuto = minuto
    guardar_segundo = segundo
    cronometro.after_cancel(proceso)
    if segundo>59:
        segundo=0
        minuto+=1
        if minuto>59:
            minuto=0
            hora+=1
            if hora>23:
                hora=0
    cronometro.after_cancel(proceso)
    cronometro['text']=str(hora)+':'+str(minuto)+':' + str(segundo)
    proceso= cronometro.after(1090,iniciar,(hora),(minuto),(segundo+1))

def detener():
    try:
        cronometro.after_cancel(proceso)
    except ValueError:
        pass
def mostrarUsuario
def guardarTiempo():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    
    sqliteQuery = "INSERT INTO usuarios (segundos,minutos,horas) VALUES('{0}','{1}','{2}')".format(guardar_segundo.get(),
                    guardar_minuto.get(),guardar_hora.get())
    
    

def salir():
    quit()

ventana = Tk()
ventana.title("Cronometro")
ventana.geometry('340x200')
ventana.iconbitmap('crono.ico')
ventana.configure(background='silver')


cronometro = Label(ventana,fg='green',width=7,font=('verdana',50),bg='black')
cronometro.place(x=20,y=20)



btn_inicio = Button(ventana,font=('courier',10,'bold'),text='Iniciar',command=iniciar)
btn_inicio.place(x=20,y=120)

btn_detener = Button(ventana,font=('courier',10,'bold'),text='Detener',command=detener)
btn_detener.place(x=140,y=120)

btn_Guardar = Button(ventana,font=('courier',10,'bold'),text='Guardar')
btn_Guardar.place(x=252,y=120)

btn_Salir = Button(ventana,font=('courier',10,'bold'),text='Salir',command=salir)
btn_Salir.place(x=146,y=160)



ventana.mainloop()
import sys
import sqlite3
from time import time
from tkinter import *
from tkinter import messagebox


def menuPrincipal():
    # Creando ventana del menu principa;
    global ventana
    ventana = Tk()
    ventana.geometry("700x500+500+100")
    ventana.resizable(width=False, height=False)
    ventana.title("Menu Principal")
    ventana.iconbitmap("logo.ico")

    # Agregando imagen del instituto
    img = PhotoImage(file="logoImagen.png")
    Label(ventana, image=img).pack()
    # Creando texto de Acceso al Sistema
    Label(text="Acceso al Sistema", bg="#067b7a", fg="white",
          width="300", height="3", font=("Georgia", 25)).pack()
    Label(text="").pack()
    # Boton Iniciar Sesion
    Button(text="Iniciar Sesion", height="3", width="30",
           command=iniciarSesion, cursor="hand2",font=("Georgia", 12)).place(x=20, y=300)
    Label(text="").pack()
    # Boton para registrarse
    Button(text="Registrarse", height="3", width="30",
           command=registrar, cursor="hand2",font=("Georgia", 12)).place(x=400, y=300)
    Label(text="").pack()
    # Boton para salir de la app
    Button(text="Salir", height="3", width="30", cursor="hand2",
           command=sys.exit,font=("Georgia", 12)).place(x=200, y=400)

    ventana.mainloop()

def click(event):  
    iniciar()


def segundoClick(event):
    detener()
    guardar()

def ventanaCronometroFuncion(segundo=0):
    global proceso
    global ventanaCronometro
    proceso = 'after#0'
    ventanaCronometro = Toplevel(ventana1)
    ventanaCronometro.title("Cronometro")
    ventanaCronometro.geometry('340x200')
    ventanaCronometro.iconbitmap('crono.ico')
    ventanaCronometro.configure(background='silver')
    global cronometro
    global nombreUsuarioEntradaCronometro
    nombreUsuarioEntradaCronometro = nombreUsuarioEntrada
    # Creando Label Usuario
    Label(ventanaCronometro, text="Usuario: ", bg="silver").place(x=20, y=0)
    # Creando Label con el nombre de usuario
    Label(ventanaCronometro, text=nombreUsuarioEntradaCronometro.get(),
          bg="silver").place(x=69, y=0)
    cronometro = Label(ventanaCronometro, fg='green',
                       width=7, font=('verdana', 50), bg='black')
    cronometro.place(x=20, y=20)
    # Boton Iniciar
    btn_inicio = Button(ventanaCronometro, font=(
        'courier', 10, 'bold'), text='Iniciar', command=iniciar)
    if segundo==0:
        ventanaCronometro.bind("<ButtonPress-1>",click)
    btn_inicio.place(x=20, y=120)
    # Boton Detener
    btn_detener = Button(ventanaCronometro, font=(
        'courier', 10, 'bold'), text='Detener', command=detener)
    btn_detener.place(x=140, y=120)
    # Boton Guardar
    btn_Guardar = Button(ventanaCronometro, font=(
        'courier', 10, 'bold'), text='Guardar', command=guardar)
    btn_Guardar.place(x=252, y=120)
    # Boton Ver Tiempo Guardado
    Button(ventanaCronometro, font=('courier', 10, 'bold'),
           text='Ver Resultado',command=verTiempo).place(x=10, y=160)
    # Boton Salir
    btn_Salir = Button(ventanaCronometro, font=(
        'courier', 10, 'bold'), text='Salir', command=salir)
    btn_Salir.place(x=146, y=160)

 
def iniciarSesion():
    global ventana1
    ventana1 = Toplevel(ventana)
    ventana1.geometry("400x300+600+100")
    ventana1.resizable(width=False, height=False)
    ventana1.title("Inicio de sesion")
    ventana1.iconbitmap("logo.ico")

    Label(ventana1, text="Ingrese su Usuario y Contraseña", bg="#067b7a", fg="white", width="300", height="3",
          font=("Georgia", 15)).pack()
    Label(ventana1, text="").pack

    global nombreUsuarioVerificar
    global constrasenaUsuarioVerificar

    nombreUsuarioVerificar = StringVar()
    constrasenaUsuarioVerificar = StringVar()

    global nombreUsuarioEntrada
    global constrasenaUsuarioEntrada

    Label(ventana1, text="Usuario: ",font=("Georgia")).pack()
    nombreUsuarioEntrada = Entry(ventana1, textvariable=nombreUsuarioVerificar)
    nombreUsuarioEntrada.pack()
    Label(ventana1).pack()

    Label(ventana1, text="Contraseña: ",font=("Georgia")).pack()
    constrasenaUsuarioEntrada = Entry(
        ventana1, textvariable=constrasenaUsuarioVerificar, show="*")
    constrasenaUsuarioEntrada.pack()
    Label(ventana1).pack
    Label(ventana1, text="").pack()

    Button(ventana1, text="Iniciar Sesion",font=("Georgia"),
           cursor="hand2", command=verificarUsuario).pack()


def registrar():
    global ventana2
    ventana2 = Toplevel(ventana)
    ventana2.geometry("400x320+600+100")
    ventana2.title("Registrar")
    ventana2.iconbitmap("logo.ico")

    global nombreUsuarioEntrada
    global contrasenaEntrada

    nombreUsuarioEntrada = StringVar()
    contrasenaEntrada = StringVar()

    Label(ventana2, text="Por favor ingrese los datos que se solicitan \n"
                         "Para Realizar el Registro", bg="#067b7a", fg="white", width="300", height="3",
          font=("Georgia", 15)).pack()
    Label(ventana2, text="").pack()

    Label(ventana2, text="Usuario: ",font=("Georgia")).pack()
    nombreUsuarioEntrada = Entry(ventana2)
    nombreUsuarioEntrada.pack()
    Label(ventana2).pack()

    Label(ventana2, text="Contraseña: ",font=("Georgia")).pack()
    contrasenaEntrada = Entry(ventana2)
    contrasenaEntrada.pack()
    Label(ventana2).pack()

    Button(ventana2, text="Registrar",font=("Georgia"), cursor="hand2",
           command=verificarNombreUsuario).pack()


def insertarUsuarios():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    sqliteQuery = "INSERT INTO usuarios (userName_usuario,contrasena) VALUES ('{0}','{1}')".format(
        nombreUsuarioEntrada.get(), contrasenaEntrada.get())
    if nombreUsuarioEntrada.get() == "" or contrasenaEntrada.get() == "":
        messagebox.showerror(
            message="No se puede dejar en blanco ningun campo", title="ERROR", )
        ventana2.destroy()
    else:
        try:
            cursor.execute(sqliteQuery)
            conexion.commit()
            messagebox.showinfo(message="Registrado con Exito", title="Aviso")
            ventana2.destroy()
        except:
            conexion.rollback()
            messagebox.showinfo(message="Error al Registrar", title="Error")
        conexion.close()


def verificarNombreUsuario():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT userName_usuario FROM usuarios WHERE userName_usuario='" +
                   nombreUsuarioEntrada.get() + "'")
    if cursor.fetchall():
        messagebox.showerror(message="El usuario ya existe", title="ERROR")
        ventana2.destroy()
    else:
        insertarUsuarios()


def verificarUsuario():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT contrasena FROM usuarios WHERE userName_usuario='" + nombreUsuarioVerificar.get() + "'and contrasena='" + constrasenaUsuarioVerificar.get() + "'")

    if cursor.fetchall():
        ventanaCronometroFuncion()

    else:
        messagebox.showinfo(title="Inicio Sesion",
                            message="Usuario y/o Contraseña Incorrecta ")
        ventana1.destroy()
    conexion.close()


def iniciar(hora=0, minuto=0, segundo=0):
    global proceso
    global guardar_minuto
    global guardar_segundo
    global cronometro
    guardar_minuto = minuto
    guardar_segundo = segundo

    if segundo!=0:
        ventanaCronometro.bind("<ButtonPress-1>",segundoClick)
        
    cronometro.after_cancel(proceso)
    if segundo > 59:
        segundo = 0
        minuto += 1
        if minuto > 59:
            minuto = 0
            hora += 1
            if hora > 23:
                hora = 0
    cronometro.after_cancel(proceso)
    cronometro['text'] = str(hora)+':'+str(minuto)+':' + str(segundo)
    proceso = cronometro.after(1090, iniciar, (hora), (minuto), (segundo+1))



def detener():
    try:
        cronometro.after_cancel(proceso)

    except ValueError:
        pass


def guardar():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    try:
       # cronometro.after_cancel(proceso)

        sqlQuery = "UPDATE usuarios SET segundos= {0} , minutos = {1} WHERE userName_usuario='{2}'".format(
            guardar_segundo, guardar_minuto, nombreUsuarioEntradaCronometro.get())

        cursor.execute(sqlQuery)
        conexion.commit()
       
    except Exception as e:
        messagebox.showerror(
            message="Error al guardar el tiempo. {0}".format(e), title='Error')


def verTiempo():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    try:
        sqlQuery = "SELECT minutos, segundos FROM usuarios WHERE userName_usuario= '{0}'".format(
            nombreUsuarioEntrada.get())

        cursor.execute(sqlQuery)

        record=cursor.fetchone()

        messagebox.showinfo(
            message="Tu record es: {0} minutos con {1} segundos".format(record[0], record[1]), title='Tiempo')

       

    except Exception as e:
        messagebox.showerror(
            message="Error al guardar el tiempo. {0}".format(e), title='Error')


def salir():
    quit()



if __name__ == "__main__":
    menuPrincipal()

from cgitb import text
from email import message
from operator import truediv
import sys
import sqlite3
from time import time
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import width


def menuPrincipal():
    # Creando ventana del menu principa;
    global ventana
    ventana = Tk()
    ventana.geometry("750x500+400+100")
    ventana.resizable(width=False, height=False)
    ventana.title("Menu Principal")
    ventana.iconbitmap("logo.ico")

    # Agregando imagen del instituto
    img = PhotoImage(file="logoImagen.png")
    Label(ventana, image=img).pack()
    # Creando texto de Acceso al Sistema
    Label(text="Acceso al Sistema", bg="#067b7a", fg="white",
          width="300", height="3", font=("Times New Roman", 25)).pack()
    Label(text="").pack()
    # Boton Iniciar Sesion
    Button(text="Iniciar Sesion", height="2", width="20",
           command=iniciarSesion, cursor="hand2", font=("Georgia", 20)).place(x=20, y=300)
    Label(text="").pack()
    # Boton para registrarse
    Button(text="Registrarse", height="2", width="20",
           command=registrar, cursor="hand2", font=("Georgia", 20)).place(x=400, y=300)
    Label(text="").pack()
    # Boton para salir de la app
    Button(text="Salir", height="2", width="20", cursor="hand2",
           command=sys.exit, font=("Georgia", 20)).place(x=200, y=400)
    # mainloop para que la ventana no se cierre
    ventana.mainloop()
# definiendo el evento del primer click para iniciar el contador


def click(event):
    iniciar()

# definiendo el evento del segundo click para detener y guardar el tiempo


def segundoClick(event):
    detener()
    guardar()
# creando la ventana del cronometro


def ventanaCronometroFuncion(segundo=0):
    global proceso
    global ventanaCronometro
    proceso = 'after#0'
    ventanaCronometro = Toplevel(ventana1)
    ventanaCronometro.title("Cronometro")
    ventanaCronometro.iconbitmap('crono.ico')
    ventanaCronometro.configure(background="#067b7a")
    ventanaCronometro.attributes('-fullscreen', True)
    global cronometro
    global nombreUsuarioEntradaCronometro
    nombreUsuarioEntradaCronometro = nombreUsuarioEntrada
    # Creando Label Usuario
    Label(ventanaCronometro, text="Usuario: ",
          bg="silver", font=("Elephant",20)).place(x=20, y=0)
    # Creando Label con el nombre de usuario
    Label(ventanaCronometro, text=nombreUsuarioEntradaCronometro.get(),
          bg="silver", font=("Elephant",20)).place(x=146, y=0)
    cronometro = Label(ventanaCronometro, fg='green',
                       width=0, height=0, font=('verdana', 150), bg='black')
    cronometro.place(x=360, y=70)
    # Boton Iniciar
    btn_inicio = Button(ventanaCronometro, font=(
        'Elephant', 20), text='Iniciar', command=iniciar)
    # Iniciando el evento dentro del evento de presionar el primer click junto a un condicional que permite iniciar la funcion
    # cuando los segundos son igual a 0
    if segundo == 0:
        ventanaCronometro.bind("<ButtonPress-1>", click)
    btn_inicio.place(x=440, y=400)
    # Boton Detener
    btn_detener = Button(ventanaCronometro, font=(
        'Elephant', 20, ), text='Detener', command=detener)
    btn_detener.place(x=620, y=400)
    # Boton Guardar
    btn_Guardar = Button(ventanaCronometro, font=(
        'Elephant', 20), text='Guardar', command=guardar)
    btn_Guardar.place(x=820, y=400)
    # Boton Ver Tiempo Guardado
    Button(ventanaCronometro, font=('Elephant', 20),
           text='Ver Resultado', command=verTiempo).place(x=490, y=500)
    # Boton Salir
    btn_Salir = Button(ventanaCronometro, font=(
        'Elephant', 20), text='Salir', command=salir)
    btn_Salir.place(x=770, y=500)

# Creando la ventana donde el usuario va a iniciar su sesion


def iniciarSesion():
    global ventana1
    ventana1 = Toplevel(ventana)
    ventana1.geometry("400x300+600+100")
    ventana1.resizable(width=False, height=False)
    ventana1.title("Inicio de sesion")
    ventana1.iconbitmap("logo.ico")
    # Creando caja de texto que aparecera en la ventana donde se va a iniciar sesion
    Label(ventana1, text="Ingrese su Usuario y Contraseña", bg="#067b7a", fg="white", width="300", height="3",
          font=("Georgia", 15)).pack()
    Label(ventana1, text="").pack

    # Creando las variables encargadas de almacenar los datos ingresados en la base de datos
    global nombreUsuarioVerificar
    global constrasenaUsuarioVerificar

    nombreUsuarioVerificar = StringVar()
    constrasenaUsuarioVerificar = StringVar()

    global nombreUsuarioEntrada
    global constrasenaUsuarioEntrada
    # Creando el Entry donde el usuario va a insertar sus datos en este caso es para el nombre del usuario
    Label(ventana1, text="Usuario: ", font=("Georgia")).pack()
    nombreUsuarioEntrada = Entry(ventana1, textvariable=nombreUsuarioVerificar)
    nombreUsuarioEntrada.pack()
    Label(ventana1).pack()
    # Creando el Entry donde el usuario va a insertar sus datos en este caso es para la contrasenia
    Label(ventana1, text="Contraseña: ", font=("Georgia")).pack()
    constrasenaUsuarioEntrada = Entry(
        ventana1, textvariable=constrasenaUsuarioVerificar, show="*")
    constrasenaUsuarioEntrada.pack()
    Label(ventana1).pack
    Label(ventana1, text="").pack()
    # Creando el boton para iniciar sesion que llama a la funcion encargada de verificar que el usuario
    # existe en la nase de datos
    Button(ventana1, text="Iniciar Sesion", font=("Georgia"),
           cursor="hand2", command=verificarUsuario).pack()

# Creando la funcion para que el usuario se registre


def registrar():
    global ventana2
    ventana2 = Toplevel(ventana)
    ventana2.geometry("400x320+600+100")
    ventana2.title("Registrar")
    ventana2.iconbitmap("logo.ico")
    # Definiendo las variables encargadas de guardar los datos que el usuario va a ingresar
    global nombreUsuarioEntrada
    global contrasenaEntrada

    nombreUsuarioEntrada = StringVar()
    contrasenaEntrada = StringVar()
    # Creando la caja de texto donde se le pedira al usuario los datos
    Label(ventana2, text="Por favor ingrese los datos que se solicitan \n"
                         "Para Realizar el Registro", bg="#067b7a", fg="white", width="300", height="3",
          font=("Georgia", 15)).pack()
    Label(ventana2, text="").pack()
    # Creando la entrada para que el usuario ingrese su nombre de usuario
    Label(ventana2, text="Usuario: ", font=("Georgia")).pack()
    nombreUsuarioEntrada = Entry(ventana2)
    nombreUsuarioEntrada.pack()
    Label(ventana2).pack()
    # Creando la entrada para que el usuario ingrese su contrasenia
    Label(ventana2, text="Contraseña: ", font=("Georgia")).pack()
    contrasenaEntrada = Entry(ventana2)
    contrasenaEntrada.pack()
    Label(ventana2).pack()
    # Creando el boton que le indica al usuario que es para registrarse ademas de llamar la funcion
    # de verificar el nombre de usuario para saber si ese nombre de usuario se encuentra ya en la base de datos
    Button(ventana2, text="Registrar", font=("Georgia"), cursor="hand2",
           command=verificarNombreUsuario).pack()
# Creando la funcion que va a acceder a la base de datos los datos ingresados por el usuario con la finalidad de registrar
# un usuario


def insertarUsuarios():
    # Codigo necesario para crear una conexion con la base de datos
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    # Creando la solicitud que va a permitir a Python ingresar a la base de datos la informacion ingresada por el usuario
    sqliteQuery = "INSERT INTO usuarios (userName_usuario,contrasena) VALUES ('{0}','{1}')".format(
        nombreUsuarioEntrada.get(), contrasenaEntrada.get())
    # Condicional que va a verificar si existe algun espacio en blanco en la seccion de la contrasenia y el nombre de usuario
    if nombreUsuarioEntrada.get() == "" or contrasenaEntrada.get() == "":
        messagebox.showerror(
            message="No se puede dejar en blanco ningun campo", title="ERROR", )
        ventana2.destroy()
    # Caso contrario se crea un try except que va a ingresar los datos en el sqlite3 y en caso de que no funcione
    # se lanzara un messagebox que informara acerca de un error
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

# Funcion que permite verificar si el nombre del usuario ya existe en la base de datos y en caso de que si exista
# se mostrara un error que informara que ese usuario ya existe


def verificarNombreUsuario():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT userName_usuario FROM usuarios WHERE userName_usuario='" +
                   nombreUsuarioEntrada.get() + "'")
    if cursor.fetchall():
        messagebox.showerror(message="El usuario ya existe", title="ERROR")
        ventana2.destroy()
    # Caso contrario se ejecutara la funcion que va a registrar el usuario en la base de datos
    else:
        insertarUsuarios()

# Otra funcion para verificar el nombre del usuario que le permitira ingresar a la ventana del cronometro una vez
# que el nombre de usuario y la contrasenia sean correctos


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

# Funcion encargada de crear e iniciar el contador del cronometro, creado a partir de varios condicionales que permitira que los
# minutos y segundos se reinicien cuando lleguen al numero especificado


def iniciar(hora=0, minuto=0, segundo=0):
    global proceso
    global guardar_minuto
    global guardar_segundo
    global cronometro
    guardar_minuto = minuto
    guardar_segundo = segundo
    ceroMinuto = 0
    ceroSegundo = 0
    # Condicional donde si los segundos son diferentes de 0 habilitara la funcion de que se pueda presionar el
    # segundo click que permitira detener y guardar el tiempo en la base de datos y el registro del usuario
    if segundo != 0:
        ventanaCronometro.bind("<ButtonPress-1>", segundoClick)
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


# Funcion para detener el cronometro
def detener():
    try:
        cronometro.after_cancel(proceso)

    except ValueError:
        pass

# Funcion para guardar y actualizar los segundos y minutos del cronometro en la base de datos del usuario que ingreso


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

# Funcion que permite ver el tiempo que tiene el usuario guardado en su registro de la base de datos


def verTiempo():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    global record
    global message
    try:
        sqlQuery = "SELECT minutos, segundos FROM usuarios WHERE userName_usuario= '{0}'".format(
            nombreUsuarioEntrada.get())

        cursor.execute(sqlQuery)

        record = cursor.fetchone()

        messagebox.showinfo(
            message="Tu record es: {0} minutos con {1} segundos".format(record[0], record[1]), title='Tiempo')

    except Exception as e:
        messagebox.showerror(
            message="Error al guardar el tiempo. {0}".format(e), title='Error')

# Funcion para salir de la aplicacion


def salir():
   ventanaCronometro.destroy()


if __name__ == "__main__":
    menuPrincipal()
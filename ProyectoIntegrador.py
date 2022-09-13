import sys
import sqlite3
from tkinter import *
from tkinter import messagebox


def menuPrincipal():
    global ventana
    ventana = Tk()
    ventana.geometry("500x400+600+100")
    ventana.resizable(width=False, height=False)
    ventana.title("Menu Principal")
    ventana.iconbitmap("logo.ico")

    img = PhotoImage(file="logoImagen.png")
    Label(ventana, image=img).pack()

    Label(text="Acceso al Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Button(text="Iniciar Sesion", height="3", width="30", command=iniciarSesion, cursor="hand2").place(x=20,y=250)
    Label(text="").pack()
    Button(text="Registrarse", height="3", width="30", command=registrar, cursor="hand2").place(x=260,y=250)
    Label(text="").pack()
    Button(text="Salir", height="3", width="30", cursor="hand2",
           command=sys.exit).place(x=130,y=320)

    ventana.mainloop()


def iniciarSesion():
    global ventana1
    ventana1 = Toplevel(ventana)
    ventana1.geometry("300x250+600+100")
    ventana1.resizable(width=False, height=False)
    ventana1.title("Inicio de sesion")
    ventana1.iconbitmap("logo.ico")

    Label(ventana1, text="Ingrese su Usuario y Contraseña", bg="navy", fg="white", width="300", height="3",
          font=("Calibri", 15)).pack()
    Label(ventana1, text="").pack

    global nombreUsuarioVerificar
    global constrasenaUsuarioVerificar

    nombreUsuarioVerificar = StringVar()
    constrasenaUsuarioVerificar = StringVar()

    global nombreUsuarioEntrada
    global constrasenaUsuarioEntrada

    Label(ventana1, text="Usuario: ").pack()
    nombreUsuarioEntrada = Entry(ventana1, textvariable=nombreUsuarioVerificar)
    nombreUsuarioEntrada.pack()
    Label(ventana1).pack()

    Label(ventana1, text="Contraseña: ").pack()
    constrasenaUsuarioEntrada = Entry(ventana1, textvariable=constrasenaUsuarioVerificar, show="*")
    constrasenaUsuarioEntrada.pack()
    Label(ventana1).pack
    Label(ventana1, text="").pack()

    Button(ventana1, text="Iniciar Sesion", cursor="hand2", command=verificarUsuario).pack()
    
def registrar():
    global ventana2
    ventana2 = Toplevel(ventana)
    ventana2.geometry("400x280+600+100")
    ventana2.title("Registrar")
    ventana2.iconbitmap("logo.ico")

    global nombreUsuarioEntrada
    global contrasenaEntrada

    nombreUsuarioEntrada = StringVar()
    contrasenaEntrada = StringVar()

    Label(ventana2, text="Por Favor Ingrese los datos que se solicitan \n"
                         "Para Realizar el Registro", bg="navy", fg="white", width="300", height="3",
          font=("Calibri", 15)).pack()
    Label(ventana2, text="").pack()

    Label(ventana2, text="Usuario: ").pack()
    nombreUsuarioEntrada = Entry(ventana2)
    nombreUsuarioEntrada.pack()
    Label(ventana2).pack()

    Label(ventana2, text="Contraseña: ").pack()
    contrasenaEntrada = Entry(ventana2)
    contrasenaEntrada.pack()
    Label(ventana2).pack()

    Button(ventana2, text="Registrar", cursor="hand2", command=verificarNombreUsuario).pack()


def insertarUsuarios():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    sqliteQuery = "INSERT INTO usuarios (userName_usuario,contrasena) VALUES ('{0}','{1}')".format(
        nombreUsuarioEntrada.get(), contrasenaEntrada.get())
    if nombreUsuarioEntrada.get() == "" or contrasenaEntrada.get() == "":
        messagebox.showerror(message="No se puede dejar en blanco ningun campo", title="ERROR", )
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

    cursor.execute("SELECT userName_usuario FROM usuarios WHERE userName_usuario='" + nombreUsuarioEntrada.get() + "'")
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
        ventanaCronometro()
        ventana.withdraw()
        ventana1.withdraw()
    else:
        messagebox.showinfo(title="Inicio Sesion", message="Usuario y/o Contraseña Incorrecta ")
        ventana1.destroy()
    conexion.close()

if __name__ == "__main__":
    menuPrincipal()
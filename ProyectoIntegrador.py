import datetime
import sys
import sqlite3
from tkinter import *
from tkinter import messagebox


def menuPrincipal():
    global ventana
    ventana = Tk()
    ventana.geometry("370x640+600+100")
    ventana.resizable(width=False, height=False)
    ventana.title("Menu Principal")
    ventana.iconbitmap("logo.ico")

    img = PhotoImage(file="logoImagen.png")
    Label(ventana, image=img).pack()

    Label(text="Acceso al Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Button(text="Iniciar Sesion", height="3", width="30", command=iniciarSesion, cursor="hand2").pack()
    Label(text="").pack()
    Button(text="Registrarse", height="3", width="30", command=registrar, cursor="hand2").pack()
    Label(text="").pack()
    Button(text="Eliminar Mi Cuenta", height="3", width="30", cursor="hand2", command=eliminarCuentaVentana).pack()
    Label(text="").pack()
    Button(text="¿Olvidó su Contraseña?", height="3", width="30", cursor="hand2",
           command=editarContrasenaVentana).pack()
    Label(text="").pack()
    Button(text="Salir", height="3", width="30", cursor="hand2",
           command=sys.exit).pack()

    ventana.mainloop()


def iniciarSesion():
    global ventana1
    ventana1 = Toplevel(ventana)
    ventana1.geometry("300x300+600+100")
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


def ventanaCronometro():
    ventanaCronometro = Toplevel(ventana1)
    ventanaCronometro.geometry("370x640+600+100")
    ventanaCronometro.resizable(width=False, height=False)
    ventanaCronometro.title("Cronometro")
    ventanaCronometro.iconbitmap("crono.ico")


def registrar():
    global ventana2
    ventana2 = Toplevel(ventana)
    ventana2.geometry("400x350+600+100")
    ventana2.title("Registrar")
    ventana2.iconbitmap("logo.ico")

    global nombreUsuarioEntrada
    global emailUsuarioEntrada
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

    Label(ventana2, text="Email: ").pack()
    emailUsuarioEntrada = Entry(ventana2)
    emailUsuarioEntrada.pack()
    Label(ventana2).pack()

    Label(ventana2, text="Contraseña: ").pack()
    contrasenaEntrada = Entry(ventana2)
    contrasenaEntrada.pack()
    Label(ventana2).pack()

    Button(ventana2, text="Registrar", cursor="hand2", command=verificarNombreUsuario).pack()


def insertarUsuarios():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    sqliteQuery = "INSERT INTO usuarios (userName_usuario,contrasena,email_usuario) VALUES ('{0}','{1}','{2}')".format(
        nombreUsuarioEntrada.get(), contrasenaEntrada.get(), emailUsuarioEntrada.get())
    if nombreUsuarioEntrada.get() == "" or contrasenaEntrada.get() == "" or emailUsuarioEntrada.get() == "":
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


def verificarEmailEliminar():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT contrasena FROM usuarios WHERE email_usuario='" + emailUsuarioVerificar.get() + "'and contrasena='" + constrasenaUsuarioVerificar.get() + "'")

    if cursor.fetchall():
        confirmarEliminar()

    else:
        messagebox.showinfo(title="ELIMINAR", message="Email y/o Contraseña Incorrecta ")
        ventana5.destroy()
    conexion.close()


def eliminarCuentaVentana():
    global ventana5
    ventana5 = Toplevel(ventana)
    ventana5.geometry("300x300+600+100")
    ventana5.resizable(width=False, height=False)
    ventana5.title("Eliminar")
    ventana5.iconbitmap("logo.ico")

    Label(ventana5, text="Ingrese su Email y Contraseña \n para Eliminar la Cuenta", bg="#E21111", fg="white",
          width="300",
          height="3",
          font=("Calibri", 15)).pack()
    Label(ventana5, text="").pack

    global emailUsuarioVerificar
    global constrasenaUsuarioVerificar

    emailUsuarioVerificar = StringVar()
    constrasenaUsuarioVerificar = StringVar()

    global emailUsuarioEntrada
    global constrasenaUsuarioEntrada

    Label(ventana5, text="Email Usuario: ").pack()
    emailUsuarioEntrada = Entry(ventana5, textvariable=emailUsuarioVerificar)
    emailUsuarioEntrada.pack()
    Label(ventana5).pack()

    Label(ventana5, text="Contraseña: ").pack()
    constrasenaUsuarioEntrada = Entry(ventana5, textvariable=constrasenaUsuarioVerificar, show="*")
    constrasenaUsuarioEntrada.pack()
    Label(ventana5).pack
    Label(ventana5, text="").pack()

    Button(ventana5, text="Eliminar", cursor="hand2", command=verificarEmailEliminar).pack()


def confirmarEliminar():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()
    pregunta = messagebox.askyesno(message="¿Seguro que desea eliminar?", title="Peligro")
    if pregunta:
        try:
            cursor.execute("DELETE FROM usuarios WHERE email_usuario='" + emailUsuarioVerificar.get() + "'")
            conexion.commit()
            messagebox.showinfo(message="Eliminado con Exito", title="Eliminar")
        except:
            conexion.rollback()
            messagebox.showinfo(message="Fallo al Eliminar", title="Error")
    else:
        messagebox.showinfo(message="Eliminacion Cancelada", title="Eliminar")
        ventana5.destroy()


def verificarEmail():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT email_usuario FROM usuarios WHERE email_usuario='" + emailUsuarioVerificar.get() + "'")

    if cursor.fetchall():
        editarContrasena()
    else:
        messagebox.showinfo(title="Actualizar", message="Email no Existe ")
        ventana6.destroy()
    conexion.close()


def editarContrasenaVentana():
    global ventana6
    ventana6 = Toplevel(ventana)
    ventana6.geometry("300x200+600+100")
    ventana6.resizable(width=False, height=False)
    ventana6.title("Cambiar Contraseña")
    ventana6.iconbitmap("logo.ico")

    Label(ventana6, text="Ingrese su Email \n Para cambiar la contraseña", bg="navy", fg="white",
          width="300",
          height="3",
          font=("Calibri", 15)).pack()
    Label(ventana6, text="").pack

    global emailUsuarioVerificar

    emailUsuarioVerificar = StringVar()

    global emailUsuarioEntrada

    Label(ventana6, text="Email Usuario: ").pack()
    emailUsuarioEntrada = Entry(ventana6, textvariable=emailUsuarioVerificar)
    emailUsuarioEntrada.pack()
    Label(ventana6).pack()

    Button(ventana6, text="Cambiar Contraseña", cursor="hand2", command=verificarEmail).pack()


def editar():
    conexion = sqlite3.connect("Base de Datos/proyecto_db.db")
    cursor = conexion.cursor()

    querySqlite = "UPDATE usuarios SET contrasena='" + contrasenaNuevaEntrada.get() + "' WHERE email_usuario = '" + emailUsuarioEntrada.get() + "'"
    try:
        cursor.execute(querySqlite)
        conexion.commit()
        messagebox.showinfo(message="Cambio de Contraseña con Exito", title="Actualizacion")
        ventana6.destroy()
    except:
        conexion.rollback()
        messagebox.showinfo(message="Cambio de Contraseña Fallido", title="Actualizacion")
        conexion.close()


def editarContrasena():
    global ventana7
    ventana7 = Toplevel(ventana6)
    ventana7.geometry("300x200+600+100")
    ventana7.resizable(width=False, height=False)
    ventana7.title("Cambiar Contraseña")
    ventana7.iconbitmap("logo.ico")

    Label(ventana7, text="Ingrese la nueva \nContraseña de su cuenta", bg="navy", fg="white",
          width="300",
          height="3",
          font=("Calibri", 15)).pack()
    Label(ventana7, text="").pack

    global contrasenaNuevaEntrada
    Label(ventana7, text="Nueva Constraseña: ").pack()
    contrasenaNuevaEntrada = Entry(ventana7)
    contrasenaNuevaEntrada.pack()
    Label(ventana7).pack()

    Button(ventana7, text="Cambiar Contraseña", cursor="hand2", command=editar).pack()


if __name__ == "__main__":
    menuPrincipal()

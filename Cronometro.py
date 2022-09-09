from datetime import datetime
import tkinter as tk

INTERVALO_REFRESCO = 500  # En milisegundos

hora_inicio = datetime.now()


def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas * 60 * 60
    minutos = int(segundos / 60)
    segundos -= minutos * 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


def obtener_tiempo_transcurrido_formateado():
    segundos_transcurridos = (datetime.now() - hora_inicio).total_seconds()
    return segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))


def refrescar_tiempo_transcurrido():
    variable_hora_actual.set(obtener_tiempo_transcurrido_formateado())
    raiz.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido)


raiz = tk.Tk()
raiz.geometry("600x500")
variable_hora_actual = tk.StringVar(raiz, value=obtener_tiempo_transcurrido_formateado())
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Cronómetro")
raiz.iconbitmap("crono.ico")

app.pack()
tk.Button(raiz, text="Iniciar", cursor="hand2", height="3", width="30", command=refrescar_tiempo_transcurrido).pack()
tk.Label(text="").pack()
tk.Button(raiz, text="Parar", cursor="hand2", height="3", width="30").pack()
tk.Label(text="").pack()
tk.Button(raiz, text="Guardar Record", cursor="hand2", height="3", width="30").pack()
tk.Label(text="").pack()

app.mainloop()

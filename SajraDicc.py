from lista_palabras import dicc_esp_qu
from tkinter import *
from tkinter import filedialog, messagebox, Label
import sqlite3


# ----------------------------------------Funciones--------------------------------------------

def buscarPalabra(event):
    """
    :param event: el parametro no tiene ninguna aplicación mas que permitir que al presionar 'enter' se ejecute
    la funcion. Por eso en el bind del entry, el parametro event tiene solo un string de relleno.
    :return: La funcion no devuelve ningun valor, sino mas bien, rellena el widge Text() con la definicion y traducción
    de la palabra buscada.
    """
    try:
        palabraBuscada = (miBusqueda.get()).lower()
        if palabraBuscada != "":
            palabra_y_definicion = palabraBuscada + ". " + dicc_esp_qu[palabraBuscada.lower()]
            resultado.delete(1.0, END)
            resultado.insert(1.0, palabra_y_definicion)
        else:
            resultado.delete(1.0, END)
            resultado.insert(1.0, "Por favor, escribe una palabra...")
    except KeyError:
        resultado.delete(1.0, END)
        resultado.insert(1.0, "No hay resultado para la palabra que buscas. Por favor, asegurate de"
                              " no haber escrito con errores ortográficos...")


def avisoSalir():

    valor = messagebox.askokcancel("Salir de la aplicación",
                                   "¿Deseas salir de la aplicación?")
    if valor == True:
        raiz.destroy()


def infoAdicional():
    messagebox.showinfo("Diccionario Español - Quechua",
                        "Versión: 1.1"
                        "\nFecha: 12/03/2020"
                        "\nDesarrollador: MarkOut"
                        "\nCompatiblilidad: SO Windows"
                        )


def infoLicencia():
    messagebox.showinfo("Diccionario Español - Quechua",
                        """GNU General Public License v3.0
                        Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
                        """
                        )

# -----------------------------------Variables-----------------------------------------------

color_fondo = "#FFF6C7"
color_cuadro_texto = "#E4CFB0"

# ----------------------------------- Interfaz ----------------------------------------------

raiz = Tk()
raiz.title("QhechuaDicc")
raiz.iconbitmap("imgs/llama2.ico")
raiz.config(bg=color_fondo)
raiz.resizable(0, 0)

# ----------------------------------Barra de Menú-----------------------------------------

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Salir", command=avisoSalir)
herramientasMenu = Menu(barraMenu, tearoff=0)
herramientasMenu.add_command(label="Buscar", command=lambda: buscarPalabra("parametro_de_relleno"))
ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=infoLicencia)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------------------------------Frame para el titulo-----------------------------------------

frameTitulo = Frame()
frameTitulo.pack()
frameTitulo.config(bg=color_fondo, width="850", height="350", bd=15)

# Frame Imagen
frameImagen = Frame(frameTitulo)
frameImagen.grid(row=0, column=0, rowspan=2)
frameImagen.config(bg=color_fondo)

llamita = PhotoImage(file="imgs/llama3.png")
vista_llamita = Label(frameImagen, image=llamita)
vista_llamita.grid(row=0, column=0)
vista_llamita.config(bg=color_fondo)

# Frame Texto
frameTexto = Frame(frameTitulo)
frameTexto.grid(row=0, column=1)
frameTexto.config(bg=color_fondo)

titulo = Label(frameTexto, text="QhechuaDicc")
titulo.grid(row=0, column=0, padx=5, pady=5)
titulo.config(font=('bold', 20), bg=color_fondo)

subtitulo = Label(frameTexto, text="Diccionario Español - Quechua")
subtitulo.grid(row=1, column=0, padx=5, pady=5)
subtitulo.config(bg=color_fondo)

# ------------------------------Frame para el contenido-----------------------------------------

frameContenido = Frame()
frameContenido.pack()
frameContenido.config(bg=color_fondo, width="850", height="350", bd=20)

# -----------------Sección donde se coloca la palabra que se quiere buscar-------------------

miBusqueda = StringVar()

cuadroTexto1 = Entry(frameContenido, textvariable=miBusqueda, width=35)
cuadroTexto1.grid(row=0, column=0, columnspan=4)
cuadroTexto1.config(fg="#261201", bg=color_cuadro_texto)
#  Esto es para que, cuando se apreta 'enter', se ejecute la misma función que con el botón 'buscar'
cuadroTexto1.bind('<Return>', buscarPalabra)

# --------------------------------------Botón----------------------------------------------

img = PhotoImage(file='imgs/buscar.png')

# El parámetro de relleno de la siguiente línea es explicado en la documentacion de la función buscarPalabra()
calcularBoton = Button(frameContenido, image=img, command=lambda: buscarPalabra("parametro_de_relleno"))
calcularBoton.grid(row=0, column=4, padx=5, pady=10, sticky="w")
calcularBoton.config(bg=color_fondo, relief="flat")

# -----------------Cuadro donde se muestra el resultado de la búsqueda---------------------
resultado = Text(frameContenido, width=40, height=12)
resultado.grid(row=1, column=0, padx=0, pady=10, columnspan=5)
resultado.config(bg=color_cuadro_texto, font="comic", wrap=WORD)  # wrap=WORD es para que haga los saltos de línea sin
# cortar una palabra por la mitad

resultado.insert(1.0, "Busca una palabra en Español...")

raiz.mainloop()

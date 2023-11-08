from tkinter import Tk

from claseInterfaz import SistemaClinicaApp

if __name__ == "__main__":
    ventana = Tk()
    app = SistemaClinicaApp(ventana)
    app.inicioApp()

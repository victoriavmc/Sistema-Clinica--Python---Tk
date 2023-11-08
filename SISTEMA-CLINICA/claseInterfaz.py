from tkinter import Tk, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import json
####################################
import os
from PIL import ImageTk, Image
from dotenv import load_dotenv
####################################
from classInventarioCRUD import Inventario
from classLoginCRUD import Login
from classMedicosCRUD import Medicos
from classUsuario import Usuario
from classProfDeLaSalud import ProfDeLaSalud
from classProducto import Producto
####################################
from email.message import EmailMessage
import ssl
import smtplib
####################################
import keyboard as kb
####################################
login = Login()
instanciaInventario = Inventario()
instanciaProfesional = Medicos()
####################################
# -*- coding: utf-8 -*-


class SistemaClinicaApp:
    intentos = 0
    intentosVerificacion = 0

    def __init__(self, root):
        self.ventana = root
        self.ventana.geometry("1080x720")
        self.ventana.title("Sistema Clinica")
        # Inicializa self.intentos solo si es None
        if SistemaClinicaApp.intentos is None:
            SistemaClinicaApp.intentos = 0
        if SistemaClinicaApp.intentosVerificacion is None:
            SistemaClinicaApp.intentosVerificacion = 0

        self.usuarioVar = StringVar()
        self.contraVar = StringVar()
        self.contraVisible = False
        self.correoVar = StringVar()
        self.pinVar = StringVar()

        self.nombreVar = StringVar()
        self.apellidoVar = StringVar()
        self.edadVar = StringVar()
        self.cuilCuitVar = StringVar()
        self.telefonoVar = StringVar()

        self.codBarrasVar = StringVar()
        self.farmacoUtensiliosVar = StringVar()
        self.cantidadExistenteVar = StringVar()
        self.cantidadMinVar = StringVar()
        self.cantidadMaxVar = StringVar()

        # Establecer el icono de la ventana
        carpetaDeTodosLosArchivos = os.path.dirname(__file__)
        self.carpetaImagenes = os.path.join(
            carpetaDeTodosLosArchivos, "Imagenes")
        iconoLogo = os.path.join(self.carpetaImagenes, "Logo.ico")
        self.ventana.iconbitmap(iconoLogo)
        self.ventana.resizable(False, False)

    ##########################
    # FONDOS E IMAGENES
    def mostrarFondoApp(self):
        # Establecer el fondo de la ventana
        imagenFondo = os.path.join(self.carpetaImagenes, "Fondo.png")
        fondoImage = Image.open(imagenFondo).resize((1080, 720))
        self.ponerFondo = ImageTk.PhotoImage(fondoImage)

        fondoMostrar = tk.Label(self.ventana, image=self.ponerFondo)
        fondoMostrar.place(x=0, y=0, relwidth=1, relheight=1)

    def mostrarLogoInicio(self):
        # Agregar un marco blanco
        Label(self.ventana, background="WHITE", width=65, borderwidth=4,
              relief="groove", height=35).place(x=580, y=110)

        # Mostrar una imagen (posiblemente un logotipo)
        imagenFoto = os.path.join(self.carpetaImagenes, "Logo.png")
        fotoImage = Image.open(imagenFoto).resize((170, 160))
        self.ponerFoto = ImageTk.PhotoImage(fotoImage)

        fotoMostrar = tk.Label(self.ventana, image=self.ponerFoto)
        fotoMostrar.place(x=200, y=200)

        # Agregar un título
        Label(self.ventana, anchor="nw", text="Sistema Clinica", bg="white",
              font=("Poppins Medium", 36)).place(x=100, y=400)

    def mostrarAdmin(self):
        # Mostrar otra imagen (posiblemente representando un usuario o administrador)
        loginImagen = os.path.join(self.carpetaImagenes, "Adm.png")
        imagenLogin = Image.open(loginImagen).resize((150, 150))
        self.ponerLogin = ImageTk.PhotoImage(imagenLogin)

        mostrarLogin = tk.Label(self.ventana, image=self.ponerLogin)
        mostrarLogin.place(x=745, y=130)

    def mostrarNewAdmin(self):
        # Mostrar otra imagen (posiblemente representando un usuario o administrador)
        loginImagen = os.path.join(self.carpetaImagenes, "msnMod.png")
        imagenLogin = Image.open(loginImagen).resize((150, 150))
        self.ponerLogin = ImageTk.PhotoImage(imagenLogin)

        mostrarLogin = tk.Label(self.ventana, image=self.ponerLogin)
        mostrarLogin.place(x=750, y=130)

    def mostrarMenu(self):
        # Agregar un marco blanco
        Label(self.ventana, background="WHITE", width=138, borderwidth=8,
              relief="groove", height=41).place(x=50, y=40)

    def mostrarLogoCostado(self):
        # Mostrar una imagen (posiblemente un logotipo)
        imagenFoto = os.path.join(self.carpetaImagenes, "Logo.png")
        fotoImage = Image.open(imagenFoto).resize((70, 60))
        self.ponerFoto = ImageTk.PhotoImage(fotoImage)

        fotoMostrar = tk.Label(self.ventana, image=self.ponerFoto)
        fotoMostrar.place(x=920, y=75)

    def mostrarFotoPerfil(self):
        imagenPerfil = Image.open(os.path.join(
            self.carpetaImagenes, "fotoPerfil.png"))
        imagenPerfil = imagenPerfil.resize((170, 160))
        self.ponerPerfil = ImageTk.PhotoImage(imagenPerfil)
        Label(self.ventana, image=self.ponerPerfil).place(x=460, y=180)

    def mostrarMenuFondo(self):
        self.mostrarFondoApp()
        self.mostrarMenu()
        self.mostrarLogoCostado()

    def mostrarTitulo(self, pParametro):
        # Agregar un título
        Label(self.ventana, anchor="nw", text=f"{pParametro}", fg="black",
              font=("Poppins Medium", 42), bg="white").place(x=280, y=80)

    def menuFondo(self, pParametro):
        self.mostrarMenuFondo()
        self.mostrarTitulo(pParametro)

    def iconoBR(self):
        # Icono de la ventana
        iconFile = os.path.join(self.carpetaImagenes, 'perropepsi.ico')
        return iconFile

    def imagenContrasenia(self):
        imagenContra = os.path.join(self.carpetaImagenes, "verContraseña.png")
        contraImage = Image.open(imagenContra).resize((40, 35))
        self.ponerContra = ImageTk.PhotoImage(contraImage)
        return self.ponerContra

    def imagenNoContrasenia(self):
        imagenNoContra = os.path.join(
            self.carpetaImagenes, "noVerContraseña.png")
        contraNo = Image.open(imagenNoContra).resize((40, 35))
        self.ponerNoContra = ImageTk.PhotoImage(contraNo)
        return self.ponerNoContra

    def mostrarContrasenia(self):
        if self.contraVisible:
            self.contrasenia.config(show="*")
            imagen = self.imagenContrasenia()
            self.botonMostrar.config(image=imagen)
            self.contraVisible = False
        else:
            self.contrasenia.config(show="")
            imagen = self.imagenNoContrasenia()
            self.botonMostrar.config(image=imagen)
            self.contraVisible = True
    #########################
    # UTILIDAD

    def enviarCorreoElectronico(self, pReceptor, pPin):
        try:
            load_dotenv()
            correoEmisor = "testingcodevictoriavmc@gmail.com"
            password = os.getenv("PASSWORD")
            em = EmailMessage()
            em["Subject"] = "Pin de Recuperacion"
            em["From"] = correoEmisor
            em["To"] = pReceptor
            em.set_content(f"PIN PARA RECUPERAR LA CUENTA {pPin}")

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(user=correoEmisor, password=password)
                smtp.sendmail(correoEmisor, pReceptor, em.as_string())
            messagebox.showwarning(
                "GUARDAR", f"PIN PARA RECUPERAR LA CUENTA {pPin}. (Enviado tambien al correo. Revise bandeja spam)")
        except:
            messagebox.showerror(
                "GUARDAR", f"Error al enviar Correo")

    def mostrarVentana(self):
        self.ventana.withdraw()   # Oculta la ventana 1
        self.ventana.deiconify()  # Muestra la ventana 2

    def muchosIntentos(self):
        messagebox.showerror(
            "Error", "Demasiados intentos. Su cuenta está bloqueada.")
        messagebox.showerror("ERROR EN LA CUENTA",
                             "COMUNIQUESE CON SERVICIO TECNICO")

    def volverAtras(self):
        self.mostrarVentana()
        self.inicioApp()

    def volverAtrasIni(self):
        self.menuApp()
    #########################

    def entryUsuarioContraseña(self):
        self.usuarioVar.set("Ingrese su usuario")
        self.contraVar.set("Ingrese contraseña")

        Label(self.ventana, text="Usuario:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=315)
        self.usuario = Entry(self.ventana, font=("Poppins Medium", 14),
                             highlightbackground="deep sky blue", highlightthickness=5, textvariable=self.usuarioVar)
        self.usuario.place(x=690, y=350)

        Label(self.ventana, text="Contraseña:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=415)
        self.contrasenia = Entry(self.ventana, font=("Poppins Medium", 14),
                                 highlightbackground="deep sky blue", show="*", highlightthickness=5, textvariable=self.contraVar)
        self.contrasenia.place(x=690, y=450)

        def funcionInicioSesion():
            usuario = self.usuarioVar.get()
            contrasenia = self.contraVar.get()
            if self.intentos < 3:
                if login.iniciarSesion(usuario, contrasenia):
                    messagebox.showinfo("Inicio de Sesion",
                                        "Inicio sesion correctamente")
                    self.mostrarVentana()
                    self.menuApp()

                elif not usuario or not contrasenia:
                    self.intentos += 1
                    messagebox.showerror(
                        "Error", "Por favor, complete todos los campos.")
                else:
                    self.intentos += 1
                    messagebox.showerror(
                        "Error", "Credenciales incorrectas. Por favor, inténtelo de nuevo.")

            elif self.intentos == 3:
                self.usuario.config(state="disabled")
                self.contrasenia.config(state="disabled")
                self.muchosIntentos()

        def funcionRegistrar():
            self.mostrarVentana()
            self.registrarApp()

        def funcionOlvidoContrasena():
            self.mostrarVentana()
            self.verificar()

        def ejecutarInicioSesion(event):
            funcionInicioSesion()

        # Bind the <Return> key event to the function that calls the button"s function
        self.ventana.bind("<Return>", ejecutarInicioSesion)

        imagenNoVe = self.imagenContrasenia()
        self.botonMostrar = Button(
            self.ventana, image=imagenNoVe, command=self.mostrarContrasenia)
        self.botonMostrar.place(x=950, y=453)
        botonRestablecer = Button(self.ventana, text="Olvidó su contraseña?", fg="blue", font=(
            "Poppins Medium", 8), command=funcionOlvidoContrasena, borderwidth=0, bg="white")
        botonRestablecer.place(x=690, y=500)
        botonInicio = Button(self.ventana, text="Iniciar Sesion", font=(
            "Poppins Medium", 12), width=13, command=funcionInicioSesion)
        botonInicio.place(x=670, y=550)
        botonRegistrar = Button(self.ventana, text="Registrarse", font=(
            "Poppins Medium", 12), width=13, command=funcionRegistrar)
        botonRegistrar.place(x=820, y=550)

    def entryRegistracion(self):
        self.usuarioVar.set("Ingrese su usuario")
        self.contraVar.set("Ingrese contraseña")
        self.correoVar.set("Ingrese su correo")

        Label(self.ventana, text="Usuario:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=300)
        self.usuario = Entry(self.ventana, font=("Poppins Medium", 14),
                             highlightbackground="deep sky blue", highlightthickness=5, textvariable=self.usuarioVar)
        self.usuario.place(x=690, y=330)

        Label(self.ventana, text="Contraseña:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=380)
        self.contrasenia = Entry(self.ventana, font=("Poppins Medium", 14),
                                 highlightbackground="deep sky blue", show="*", highlightthickness=5, textvariable=self.contraVar)
        self.contrasenia.place(x=690, y=410)

        Label(self.ventana, text="Correo:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=460)
        self.correo = Entry(self.ventana, font=("Poppins Medium", 14),
                            highlightbackground="deep sky blue", highlightthickness=5, textvariable=self.correoVar)
        self.correo.place(x=690, y=490)

        def funcionCrearUsuario():
            usuario = self.usuarioVar.get()
            contrasenia = self.contraVar.get()
            correo = self.correoVar.get()
            usuario.title()

            pin = random.randint(100000, 999999)
            while pin in Usuario.listaUsuarios:
                pin = random.randint(100000, 999999)

            if login.registrarUsuario(usuario, contrasenia, correo, pin):
                self.enviarCorreoElectronico(correo, pin)
                messagebox.showinfo("Registro de Usuario",
                                    "Se registro al usuario correctamente")
            else:
                messagebox.showerror(
                    "Registro de usuario", "Error al registrar el usuario, intente nuevamente")

        def ejecutarFCU(event):
            funcionCrearUsuario()  # Call the button"s function

        # Bind the <Return> key event to the function that calls the button"s function
        self.ventana.bind("<Return>", ejecutarFCU)

        imagenNoVe = self.imagenContrasenia()
        self.botonMostrar = Button(
            self.ventana, image=imagenNoVe, command=self.mostrarContrasenia)
        self.botonMostrar.place(x=950, y=413)
        botonAtras = Button(self.ventana, text="<-", font=(
            "Poppins Medium", 12), command=self.volverAtras)
        botonAtras.place(x=600, y=120)
        botonCrear = Button(self.ventana, text="Crear Usuario", font=(
            "Poppins Medium", 12), width=13, command=funcionCrearUsuario)
        botonCrear.place(x=750, y=550)

    def entryConfirmarUsuario(self):
        Label(self.ventana, text="Verifique:", font=(
            "Poppins Medium", 14), bg="white").place(x=770, y=290)
        self.correoVar.set("Ingrese su correo")
        self.pinVar.set("Ingrese su pin")

        Label(self.ventana, text="Correo:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=315)
        self.correo = Entry(self.ventana, font=("Poppins Medium", 14),
                            highlightbackground="deep sky blue", highlightthickness=5, textvariable=self.correoVar)
        self.correo.place(x=690, y=350)

        Label(self.ventana, text="Pin:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=415)
        self.pin = Entry(self.ventana, font=("Poppins Medium", 14),
                         highlightbackground="deep sky blue", highlightthickness=5, textvariable=self.pinVar)
        self.pin.place(x=690, y=450)

        def funcionCorreoPin():
            correo = self.correoVar.get()
            pin = self.pinVar.get()
            valor = 0

            if self.intentosVerificacion < 3:
                for usuario in Usuario.listaUsuarios:
                    if usuario.getPin() == int(pin) and usuario.getCorreo() == correo:
                        self.mostrarVentana()
                        self.cambioContraApp()
                        break
                else:
                    if not correo or not pin:
                        self.intentosVerificacion += 1
                        valor = 1
                    else:
                        self.intentosVerificacion += 1
                        valor = 2

                if valor == 1:
                    messagebox.showerror(
                        "Error", "Por favor, complete todos los campos.")
                elif valor == 2:
                    messagebox.showerror(
                        "ERROR DE INFORMACIÓN", "No se ha podido verificar la información ingresada")

            elif self.intentosVerificacion == 3:
                self.correo.config(state="disabled")
                self.pin.config(state="disabled")
                self.muchosIntentos()

        def funcionCP(event):
            funcionCorreoPin()

        # Asociar la tecla "Enter" a la función funcionInicioSesion
        self.ventana.bind("<Return>", funcionCP)
        botonAtras = Button(self.ventana, text="<-", font=(
            "Poppins Medium", 12), command=self.volverAtras)
        botonAtras.place(x=600, y=120)
        botonCrear = Button(self.ventana, text="Verificar", font=(
            "Poppins Medium", 12), width=13, command=funcionCorreoPin)
        botonCrear.place(x=750, y=550)

    def entryCambiosUser(self):
        Label(self.ventana, text="Modifique:", font=(
            "Poppins Medium", 14), bg="white").place(x=770, y=290)
        self.usuarioVar.set("Ingrese su nuevo usuario")
        self.contraVar.set("Ingrese su contraseña")

        Label(self.ventana, text="Usuario:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=315)
        self.usuario = Entry(self.ventana, font=("Poppins Medium", 14),
                             highlightbackground="deep sky blue", highlightthickness=5, textvariable=self.usuarioVar)
        self.usuario.place(x=690, y=350)

        Label(self.ventana, text="Contraseña:", font=(
            "Poppins Medium", 14), bg="white").place(x=690, y=415)
        self.contrasenia = Entry(self.ventana, font=("Poppins Medium", 14),
                                 highlightbackground="deep sky blue", show="*", highlightthickness=5, textvariable=self.contraVar)
        self.contrasenia.place(x=690, y=450)

        def funcionCambiosLogin():
            correo = self.correoVar.get()
            newUser = self.usuarioVar.get()
            newContra = self.contraVar.get()

            newPin = random.randint(100000, 999999)
            while newPin in Usuario.listaUsuarios:
                newPin = random.randint(100000, 999999)

            if login.reestablecerContrasenia(newUser, newContra, correo, newPin):
                self.enviarCorreoElectronico(correo, newPin)

                messagebox.showinfo("Reestablecer Cuenta",
                                    "Reestablecimiento realizado con exito!.")
                self.mostrarVentana()
                self.menuApp()
            else:
                messagebox.showerror("Reestablecer Cuenta",
                                     "Error al reestablecer la cuenta")

        def funcionCL(event):
            funcionCambiosLogin()

        self.ventana.bind("<Return>", funcionCL)
        imagenNoVe = self.imagenContrasenia()
        self.botonMostrar = Button(
            self.ventana, image=imagenNoVe, command=self.mostrarContrasenia)
        self.botonMostrar.place(x=950, y=453)
        botonAtras = Button(self.ventana, text="<-", font=(
            "Poppins Medium", 12), command=self.volverAtras)
        botonAtras.place(x=600, y=120)
        botonCrear = Button(self.ventana, text="Modificar", font=(
            "Poppins Medium", 12), width=13, command=funcionCambiosLogin)
        botonCrear.place(x=750, y=550)

        def inicioApp(self):
            ventana = Tk()
            self.app.mostrarFondoApp()
            self.app.mostrarLogoCostado()
            self.app.mostrarLogoInicio()
            self.app.mostrarAdmin()
            self.app.entryUsuarioContraseña()
            ventana.mainloop()

        def registrarApp(self):
            ventana = Tk()
            self.app.mostrarFondoselfApp()
            self.app.mostrarLogoCostado()
            self.app.mostrarLogoInicio()
            self.app.mostrarNewAdmin()
            self.app.entryRegistracion()
            ventana.mainloop()

        def ConfirmarUsuario(self):
            ventana = Tk()
            self.app.mostrarFondoApp()
            self.app.mostrarLogoCostado()
            self.app.mostrarLogoInicio()
            self.app.mostrarAdmin()
            self.app.entryConfirmarUsuario()
            ventana.mainloop()

        def CambioContra(self):
            ventana = Tk()
            self.app.mostrarFondoApp()
            self.app.mostrarLogoCostado()
            self.app.mostrarLogoInicio()
            self.app.mostrarAdmin()
            self.app.entryCambiosUser()
            ventana.mainloop()

        def menuApp(self):
            ventana = Tk()
            self.app.mostrarFondoApp()
            self.app.mostrarMenu()
            self.app.mostrarLogoCostado()
            self.app.mostrarTitulo()
            ventana.mainloop()
    #########################

    def correoMensaje(self):
        usuario = self.usuarioVar.get()
        for user in Usuario.listaUsuarios:
            if user.getUsuario() == usuario:
                self.enviarCorreoElectronico(user.getCorreo(), user.getPin())

    # Mostrar LOGIN
    def mostrarLogin(self):
        self.mostrarFotoPerfil()
        usuario = self.usuarioVar.get()
        for user in Usuario.listaUsuarios:
            if user.getUsuario() == usuario:
                Label(self.ventana, font=("Poppins Medium", 18),
                      text=f"Usuario: {user.getUsuario()}", bg="white").place(x=70, y=350)
                asteriscoContra = "*" * len(user.getContrasenia())
                Label(self.ventana, font=("Poppins Medium", 18),
                      text=f"Contraseña: {asteriscoContra}", bg="white").place(x=70, y=450)
                Label(self.ventana, font=("Poppins Medium", 18),
                      text=f"Correo: {user.getCorreo()}", bg="white").place(x=70, y=550)

                asteriscoPin = "*" * len(str(user.getPin()))
                Label(self.ventana, font=("Poppins Medium", 18),
                      text=f"Pin: {asteriscoPin}", bg="white").place(x=640, y=450)
                break

        botonAtras = Button(self.ventana, text="<-", font=(
            "Poppins Medium", 12), command=self.volverAtrasIni)
        botonAtras.place(x=60, y=50)
        botonCorreoEnvia = Button(self.ventana, text="Enviar al correo", font=(
            "Poppins Medium", 12), command=self.correoMensaje)
        botonCorreoEnvia.place(x=800, y=450)

    # CRUD PSalud
    def CRUDPSalud(self):

        def cargarDatosEnTreeView():
            for row in tree.get_children():
                tree.delete(row)
            with open('medicos.json', 'r') as archivo:
                medicoData = json.load(archivo)
                for data in medicoData:
                    # Inserta los valores en el orden correcto
                    tree.insert("", END, values=(
                        data['nombre'],  # Nombre
                        data['apellido'],  # Apellido
                        data['edad'],  # Edad
                        data['cuilCuit'],  # Cuil/Cuit
                        data['telefono'],  # Teléfono
                        data['sexo'],  # Sexo
                        data['titulo'],  # Título
                        data['especialidad']))  # Especialidad

        botonAtras = Button(self.ventana, text="<-", font=(
            "Poppins Medium", 12), command=self.volverAtrasIni)
        botonAtras.place(x=60, y=50)

        sexoCombobox = ttk.Combobox(
            self.ventana, values=["Femenino", "Masculino", "Otros"])
        sexoCombobox.place(x=790, y=205)

        tituloCombobox = ttk.Combobox(
            self.ventana, values=["Medico", "Lic en Enfermeria"])
        tituloCombobox.place(x=790, y=260)

        def onTituloComboboxSelect(event):
            seleccionadoTitulo = tituloCombobox.get()
            if seleccionadoTitulo == "Medico":
                especialidadesCombobox['values'] = [
                    "Medico General"] + listaEspecialidadesMedico
            elif seleccionadoTitulo == "Lic en Enfermeria":
                especialidadesCombobox['values'] = [
                    "Enfermeria General"] + listaLicenciadosEnfermero
            especialidadesCombobox['state'] = 'readonly'

        listaLicenciadosEnfermero = ["Enfermeria en Emergentologia",
                                     "Unidad Terapia Intensiva Adulto", "Enfermería Unidad Terapia Intensiva Pediátrica y Neonatal", "Enfermería Clínica y Familiar"]
        listaLicenciadosEnfermero = sorted(
            listaLicenciadosEnfermero, reverse=False)
        listaEspecialidadesMedico = ["Cardiología", "Dermatología", "Gastroenterología", "Neurología", "Psiquiatría", "Pediatría", "Ortopedia", "Oftalmología", "Otorrinolaringología", "Endocrinología",
                                     "Urología", "Nefrología", "Hematología", "Reumatología", "Infectología", "Cirugía General", "Cirugía Cardiovascular", "Anestesiología", "Oncología", "Neumología", "Medico Clinico", "Tocoginecologia"]
        listaEspecialidadesMedico = sorted(
            listaEspecialidadesMedico, reverse=False)

        especialidadesCombobox = ttk.Combobox(
            self.ventana, values=listaEspecialidadesMedico, state='disabled')
        especialidadesCombobox.place(x=790, y=315)

        tituloCombobox.bind("<<ComboboxSelected>>", onTituloComboboxSelect)

        tree = ttk.Treeview(self.ventana, height=10, columns=(
            "#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7"))
        tree.place(x=130, y=350)

        columnas = ["Nombre", "Apellido", "Edad", "Cuil/Cuit",
                    "Telefono", "Sexo", "Titulo", "Especialidad"]
        tree["columns"] = columnas
        tree["show"] = "headings"
        for columna in columnas:
            tree.column(columna, width=110)
            tree.heading(columna, text=columna)

        tree.column("Edad", width=45, anchor=CENTER)
        tree.column("Especialidad", width=200, anchor=CENTER)
        tree.column("Sexo", width=75, anchor=CENTER)
        tree.column("Cuil/Cuit", width=80, anchor=CENTER)
        tree.column("Telefono", width=80, anchor=CENTER)
        tree.column("Nombre", width=120, anchor=CENTER)
        tree.column("Apellido", width=120, anchor=CENTER)
        tree.column("Titulo", width=105, anchor=CENTER)

        self.nombreVar.set("Ingrese su nombre")
        self.apellidoVar.set("Ingrese su apellido")
        self.edadVar.set("Ingrese su edad")
        self.cuilCuitVar.set("Ingrese Sin - ni . XXXXXXXXXXX")
        self.telefonoVar.set("Ingrese XXXXXXXXXX")

        def seleccionarItem(event):
            item = tree.selection()
            if item:
                item = item[0]
                values = tree.item(item, 'values')
                self.nombreVar.set(values[0])  # Nombre
                self.apellidoVar.set(values[1])  # Apellido
                self.edadVar.set(values[2])  # Edad
                self.cuilCuitVar.set(values[3])  # Cuil/Cuit
                self.telefonoVar.set(values[4])  # Teléfono
                sexoCombobox.set(values[5])  # Sexo
                tituloCombobox.set(values[6])  # Título
                especialidadesCombobox.set(values[7])  # Especialidad
                botonModificar.config(state='active')
                botonEliminar.config(state='active')
            else:
                # Si no se selecciona un elemento, deshabilita los botones
                botonModificar.config(state='disabled')
                botonEliminar.config(state='disabled')

        tree.bind('<ButtonRelease-1>', seleccionarItem)

        # Labels
        Label(self.ventana, text="Nombre", font=(
            "Poppins Medium", 10), bg="white").place(x=150, y=175)
        Label(self.ventana, text="Apellido", font=(
            "Poppins Medium", 10), bg="white").place(x=150, y=250)
        Label(self.ventana, text="Edad", font=(
            "Poppins Medium", 10), bg="white").place(x=350, y=175)
        Label(self.ventana, text="Cuil/Cuit",
              font=("Poppins Medium", 10), bg="white").place(x=350, y=250)
        Label(self.ventana, text="Teléfono", font=(
            "Poppins Medium", 10), bg="white").place(x=550, y=175)
        Label(self.ventana, text="Sexo", font=(
            "Poppins Medium", 10), bg="white").place(x=788, y=175)
        Label(self.ventana, text="Título", font=(
            "Poppins Medium", 10), bg="white").place(x=788, y=230)
        Label(self.ventana, text="Especialidad", font=(
            "Poppins Medium", 10), bg="white").place(x=788, y=285)

        # Entrys
        nombreEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.nombreVar)
        nombreEntry.place(x=150, y=200)

        apellidoEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.apellidoVar)
        apellidoEntry.place(x=150, y=275)

        edadEntry = Entry(self.ventana, font=("Poppins Medium", 10),
                          highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.edadVar)
        edadEntry.place(x=350, y=200)

        cuilCuitEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.cuilCuitVar)
        cuilCuitEntry.place(x=350, y=275)

        telefonoEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.telefonoVar)
        telefonoEntry.place(x=550, y=200)

        def agregarMedicoInterfaz():
            nombre = self.nombreVar.get().title()
            apellido = self.apellidoVar.get().title()
            edad = self.edadVar.get()
            cuilCuit = self.cuilCuitVar.get()
            telefono = self.telefonoVar.get()
            sexo = sexoCombobox.get()
            titulo = tituloCombobox.get()
            especialidades = especialidadesCombobox.get()

            if titulo == 'Medico' and not especialidades:
                especialidades = "Medico General"
            elif titulo == 'Lic en Enfermeria' and not especialidades:
                especialidades = "Enfermeria General"

            if instanciaProfesional.agregarMedico(nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidades):
                messagebox.showinfo(
                    "Agregar Medico", "Se agregó el médico correctamente")
                cargarDatosEnTreeView()
            else:
                messagebox.showerror(
                    "Agregar Medico", "Hubo un error al agregar el médico, verifique los datos")

        def modificarMedicoInterfaz():
            nombre = self.nombreVar.get().title()
            apellido = self.apellidoVar.get().title()
            edad = self.edadVar.get()
            cuilCuit = self.cuilCuitVar.get()
            telefono = self.telefonoVar.get()
            sexo = sexoCombobox.get()
            titulo = tituloCombobox.get()
            especialidades = especialidadesCombobox.get()

            if instanciaProfesional.modificarMedico(nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidades):
                messagebox.showinfo("Modificar Medico",
                                    "Se modificó el médico correctamente")
                cargarDatosEnTreeView()
            else:
                messagebox.showerror(
                    "Modificar Medico", "Hubo un error al modificar el médico, verifique los datos")

        def buscarMedicoInterfaz():
            ventanaBuscar = Toplevel(self.ventana)
            ventanaBuscar.title("Buscar Medico por CUIL/CUIT")
            ventanaBuscar.config(bg="white")
            icono = self.iconoBR()
            ventanaBuscar.iconbitmap(icono)

            ventanaBuscar.geometry("250x120")

            Label(ventanaBuscar, text="CUIL/CUIT:", font=(
                "Poppins Medium", 10), bg="white").pack()
            cuilCuitEntry = Entry(ventanaBuscar,  font=(
                "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3)
            cuilCuitEntry.pack()

            def buscarMedico():
                cuilCuit = cuilCuitEntry.get()
                medicoInfo = instanciaProfesional.mostrarMedico(cuilCuit)
                if medicoInfo:
                    messagebox.showinfo("Información del Médico", medicoInfo)

                    for item in tree.get_children():
                        values = tree.item(item, 'values')
                        if values[3] == cuilCuit:
                            tree.selection_set(item)
                            tree.focus(item)
                            tree.see(item)
                            break

                    botonModificar.config(state='active')
                    botonEliminar.config(state='active')
                else:
                    messagebox.showerror(
                        "Buscar Médico", "No se encontró el médico con el CUIL/CUIT proporcionado")
                    botonModificar.config(state='disabled')
                    botonEliminar.config(state='disabled')

                ventanaBuscar.destroy()

            botonBuscar = Button(ventanaBuscar, text="Buscar", font=(
                "Poppins Medium", 10), bg="white", command=buscarMedico)
            botonBuscar.place(x=100, y=70)

        def eliminarMedicoInterfaz():
            cuilCuit = self.cuilCuitVar.get()
            if messagebox.askyesno("ADVERTENCIA", "¿Realmente quiere borrar el Médico?"):
                if instanciaProfesional.eliminarMedico(cuilCuit):
                    messagebox.showinfo("Eliminar Médico",
                                        "Se eliminó el médico correctamente")
                    cargarDatosEnTreeView()
                else:
                    messagebox.showerror(
                        "Eliminar Médico", "No se encontró el médico con el CUIL/CUIT proporcionado")

        # Botones
        botonAgregar = Button(self.ventana, text="Agregar", font=(
            "Poppins Medium", 10), command=agregarMedicoInterfaz, width=10)
        botonAgregar.place(x=150, y=600)

        botonModificar = Button(self.ventana, text="Modificar", font=(
            "Poppins Medium", 10), command=modificarMedicoInterfaz, state='disabled', width=10)
        botonModificar.place(x=250, y=600)

        botonBuscar = Button(self.ventana, text="Buscar", font=(
            "Poppins Medium", 10), command=buscarMedicoInterfaz, width=10)
        botonBuscar.place(x=350, y=600)

        botonEliminar = Button(self.ventana, text="Eliminar", font=(
            "Poppins Medium", 10), state='disabled', command=eliminarMedicoInterfaz, width=10)
        botonEliminar.place(x=450, y=600)

        cargarDatosEnTreeView()
    #########################

    def seleccionarOpcion(self):
        seleccion = self.opcionVar.get()
        if seleccion == 1:
            self.mostrarVentana()
            self.menuFondo("Datos de Perfil:")
            self.mostrarLogin()

        elif seleccion == 2:
            self.mostrarVentana()
            self.menuFondo("Personal Clínico")
            self.CRUDPSalud()

        elif seleccion == 3:
            self.mostrarVentana()
            self.menuFondo("Inventario")
            self.CRUDInventario()

        elif seleccion == 4:
            self.mostrarVentana()
            self.inicioApp()

    def seleccionarCrud(self):
        self.menuFondo("Sistema Clinica")
        self.opcionVar = IntVar()

        opcionLogin = Radiobutton(
            self.ventana, text="Mi Cuenta", variable=self.opcionVar, value=1, command=self.seleccionarOpcion, font=("Poppins Medium", 24), bg="white")
        opcionProDeSalud = Radiobutton(
            self.ventana, text="Medicos / Enfermeros", variable=self.opcionVar, value=2, command=self.seleccionarOpcion, font=("Poppins Medium", 24), bg="white")
        opcionInventario = Radiobutton(
            self.ventana, text="Inventario", variable=self.opcionVar, value=3, command=self.seleccionarOpcion, font=("Poppins Medium", 24), bg="white")
        opcionSalir = Radiobutton(
            self.ventana, text="Cerrar Sesion", variable=self.opcionVar, value=4, command=self.seleccionarOpcion, font=("Poppins Medium", 24), bg="white")

        opcionLogin.place(x=120, y=180)
        opcionProDeSalud.place(x=120, y=280)
        opcionInventario.place(x=120, y=380)
        opcionSalir.place(x=120, y=480)
        self.ventana.mainloop()
    #########################
    # INICIO REGISTRO

    def inicioApp(self):
        self.mostrarFondoApp()
        self.mostrarLogoInicio()
        self.mostrarAdmin()
        self.entryUsuarioContraseña()
        self.ventana.mainloop()

    # REGISTRAR
    def registrarApp(self):
        self.mostrarFondoApp()
        self.mostrarLogoCostado()
        self.mostrarLogoInicio()
        self.mostrarNewAdmin()
        self.entryRegistracion()
        self.ventana.mainloop()

    # CORREO PIN
    def verificar(self):
        self.mostrarFondoApp()
        self.mostrarLogoCostado()
        self.mostrarLogoInicio()
        self.mostrarAdmin()
        self.entryConfirmarUsuario()
        self.ventana.mainloop()

    # USUARIO CONTRASEÑA NUEVA
    def cambioContraApp(self):
        self.mostrarFondoApp()
        self.mostrarLogoCostado()
        self.mostrarLogoInicio()
        self.mostrarAdmin()
        self.entryCambiosUser()
        self.ventana.mainloop()

    # INICIO ELEGIR CRUD
    def menuApp(self):
        self.seleccionarCrud()
    #########################

    def CRUDInventario(self):
        def cargarDatosEnTreeView():
            for row in tree.get_children():
                tree.delete(row)
            with open('inventario.json', 'r') as archivo:
                medicoData = json.load(archivo)
                for data in medicoData:
                    # Inserta los valores en el orden correcto
                    tree.insert("", END, values=(
                        data['codBarras'],
                        data['farmacoUtensilios'],
                        data['cantidadExistente'],
                        data['cantidadMin'],
                        data['cantidadMax']))

        botonAtras = Button(self.ventana, text="<-", font=(
            "Poppins Medium", 12), command=self.volverAtrasIni)
        botonAtras.place(x=60, y=50)

        tree = ttk.Treeview(self.ventana, height=10,
                            columns=("#0", "#1", "#2", "#3", "#4"))
        tree.place(x=130, y=350)

        columnas = ["Codigo de Barras", "Producto",
                    "Cantidad Existente", "Cantidad Minima", "Cantidad Maxima"]
        tree["columns"] = columnas
        tree["show"] = "headings"
        for columna in columnas:
            tree.column(columna, width=164, anchor=CENTER)
            tree.heading(columna, text=columna)

        self.farmacoUtensiliosVar.set("Nombre del Producto")
        self.cantidadExistenteVar.set("Cantidad Existente")
        self.cantidadMinVar.set("Cantidad Minima")
        self.cantidadMaxVar.set("cantidad Maxima")

        def seleccionarItem(event):
            item = tree.selection()
            if item:
                item = item[0]
                values = tree.item(item, 'values')
                # Código de barras (desactivado)
                self.codBarrasVar.set(values[0])
                self.farmacoUtensiliosVar.set(values[1])
                self.cantidadExistenteVar.set(values[2])
                self.cantidadMinVar.set(values[3])
                self.cantidadMaxVar.set(values[4])
                # Habilita los botones de modificar y eliminar
                botonModificar.config(state='normal')
                botonEliminar.config(state='normal')
            else:
                # Si no se selecciona un elemento, deshabilita los botones
                botonModificar.config(state='disabled')
                botonEliminar.config(state='disabled')

        tree.bind('<ButtonRelease-1>', seleccionarItem)

        # Labels
        Label(self.ventana, text="CodBarra", font=(
            "Poppins Medium", 10), bg="white").place(x=150, y=175)
        Label(self.ventana, text="Producto", font=(
            "Poppins Medium", 10), bg="white").place(x=150, y=250)
        Label(self.ventana, text="Cantidad Existente", font=(
            "Poppins Medium", 10), bg="white").place(x=350, y=175)
        Label(self.ventana, text="Cantidad Minima",
              font=("Poppins Medium", 10), bg="white").place(x=350, y=250)
        Label(self.ventana, text="Cantidad Maxima", font=(
            "Poppins Medium", 10), bg="white").place(x=550, y=175)

        # Entrys
        codBarraEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.codBarrasVar, state="disabled")
        codBarraEntry.place(x=150, y=200)

        farmacoUtensilioEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.farmacoUtensiliosVar)
        farmacoUtensilioEntry.place(x=150, y=275)

        cantidadExistenteEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10),
            highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.cantidadExistenteVar)
        cantidadExistenteEntry.place(x=350, y=200)

        cantidadMinEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.cantidadMinVar)
        cantidadMinEntry.place(x=350, y=275)

        cantidadMaxEntry = Entry(self.ventana, font=(
            "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3, textvariable=self.cantidadMaxVar)
        cantidadMaxEntry.place(x=550, y=200)

        def agregarProductoInterfaz():
            codBarras = self.codBarrasVar.get()
            producto = self.farmacoUtensiliosVar.get().title()
            cantidadExistente = self.cantidadExistenteVar.get()
            cantidadMin = self.cantidadMinVar.get()
            cantidadMax = self.cantidadMaxVar.get()

            if instanciaInventario.agregarProducto(producto, cantidadExistente, cantidadMin, cantidadMax):
                messagebox.showinfo("Agregar Producto",
                                    "Se agregó el producto correctamente")
                cargarDatosEnTreeView()
            else:
                messagebox.showerror(
                    "Agregar Producto", "Hubo un error al agregar el producto, verifique los datos")

        def modificarProductoInterfaz():
            codBarras = self.codBarrasVar.get()
            producto = self.farmacoUtensiliosVar.get().title()
            cantidadExistente = self.cantidadExistenteVar.get()
            cantidadMin = self.cantidadMinVar.get()
            cantidadMax = self.cantidadMaxVar.get()

            if instanciaInventario.modificarProducto(codBarras, producto, cantidadExistente, cantidadMin, cantidadMax):
                messagebox.showinfo("Modificar Producto",
                                    "Se modificó el producto correctamente")
                cargarDatosEnTreeView()
            else:
                messagebox.showerror(
                    "Modificar Producto", "Hubo un error al modificar el producto, verifique los datos")

        def buscarProductoInterfaz():
            ventanaBuscar = Toplevel(self.ventana)
            ventanaBuscar.title("Buscar Producto por Código de Barras")
            ventanaBuscar.config(bg="white")
            icono = self.iconoBR()
            ventanaBuscar.iconbitmap(icono)
            ventanaBuscar.geometry("250x120")

            Label(ventanaBuscar, text="Código de Barras:", font=(
                "Poppins Medium", 10), bg="white").pack()
            codigoBarrasEntry = Entry(ventanaBuscar, font=(
                "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3)
            codigoBarrasEntry.pack()

            def buscarProducto():
                codigoBarras = codigoBarrasEntry.get()
                productoInfo = instanciaInventario.mostrarProducto(codigoBarras)
                if productoInfo:
                    messagebox.showinfo("Información del Producto", productoInfo)

                    for item in tree.get_children():
                        values = tree.item(item, 'values')
                        if values[0] == codigoBarras:
                            tree.selection_set(item)
                            tree.focus(item)
                            tree.see(item)
                            break
                    
                    botonModificar.config(state='active')
                    botonEliminar.config(state='active')
                else:
                    messagebox.showerror(
                    "Buscar Producto", "No se encontró el producto con el código de barras proporcionado")

                    botonModificar.config(state='disabled')
                    botonEliminar.config(state='disabled')

                ventanaBuscar.destroy()

            botonBuscar = Button(ventanaBuscar, text="Buscar", font=(
                "Poppins Medium", 10), bg="white", command=buscarProducto)
            botonBuscar.place(x=100, y=70)

        def eliminarProductoInterfaz():
            codBarras = self.codBarrasVar.get()
            if messagebox.askyesno("ADVERTENCIA", "¿Realmente quiere borrar el Producto?"):
                if instanciaInventario.eliminarProducto(codBarras):
                    messagebox.showinfo("Eliminar Producto",
                                        "Se eliminó el producto correctamente")
                    cargarDatosEnTreeView()
                else:
                    messagebox.showerror(
                        "Eliminar Producto", "Error al eliminar el producto")

        def registrarUsoProductoInterfaz():
            ventanaRegistrarUso = Toplevel(self.ventana)
            ventanaRegistrarUso.title("Registrar Uso del Producto")
            ventanaRegistrarUso.config(bg="white")
            icono = self.iconoBR()
            ventanaRegistrarUso.iconbitmap(icono)

            ventanaRegistrarUso.geometry("365x240")

            Label(ventanaRegistrarUso, text="Nombre del Producto:", font=(
                "Poppins Medium", 10), bg="white").place(x=100, y=20)
            Label(ventanaRegistrarUso, text="Productos Utilizados:", font=(
                "Poppins Medium", 10), bg="white").place(x=100, y=90)

            nombreEntry = Entry(ventanaRegistrarUso, font=(
                "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3)
            nombreEntry.place(x=100, y=50)

            cantidadUsadaEntry = Entry(ventanaRegistrarUso, font=(
                "Poppins Medium", 10), highlightbackground="deep sky blue", highlightthickness=3)
            cantidadUsadaEntry.place(x=100, y=120)

            def registrarUso():
                nombre = nombreEntry.get()
                cantidadUsada = cantidadUsadaEntry.get()
                if not cantidadUsada:
                    messagebox.showerror("Error", "Por favor, ingrese la cantidad utilizada.")
                else:
                    cantidadUsada = int(cantidadUsada)  # Solo convierte si es un valor numérico
                    resultado = instanciaInventario.usoUtensilio(nombre, cantidadUsada)
                    cargarDatosEnTreeView()
                    if resultado == 1:
                        messagebox.showinfo(
                            "Registrar Producto", f"Se usaron {cantidadUsada} existencias del Producto '{nombre}'")
                    elif resultado == 2:
                        messagebox.showinfo(
                            "Registrar Producto", f"Se usaron {cantidadUsada} existencias del Producto '{nombre}'")
                        respuesta = messagebox.askquestion(
                            "Advertencia", "La cantidad existente es igual o menor a la cantidad mínima. ¿Desea comprar más productos?")
                        if respuesta == "yes":
                            producto = instanciaInventario.encontrarProductoPorNombre(
                                nombre)
                            if instanciaInventario.comprarUtensilio(producto):
                                messagebox.showinfo(
                                    "Registrar Producto", f"Se relleno las existencias del Producto '{nombre}'")
                                cargarDatosEnTreeView()
                            else:
                                messagebox.showerror(
                                    "Error de Compra", "No se pudo realizar la compra.")
                    elif resultado == 3:
                        messagebox.showerror(
                            "Registrar Producto", "No se pueden usar más productos de los que existen")
                    else:
                        messagebox.showerror(
                            "Registrar Producto", "No se encontró el producto con ese nombre")
                    ventanaRegistrarUso.destroy()
            botonRegistrar = Button(ventanaRegistrarUso, text="Registrar", font=(
                "Poppins Medium", 10), bg="white", command=registrarUso)
            botonRegistrar.place(x=150, y=160)

        # Botones
        botonAgregar = Button(self.ventana, text="Agregar", font=(
            "Poppins Medium", 10), command=agregarProductoInterfaz, width=10)
        botonAgregar.place(x=150, y=600)

        botonModificar = Button(self.ventana, text="Modificar", font=(
            "Poppins Medium", 10), command=modificarProductoInterfaz, width=10, state='disabled')
        botonModificar.place(x=250, y=600)

        botonBuscar = Button(self.ventana, text="Buscar", font=(
            "Poppins Medium", 10), command=buscarProductoInterfaz, width=10)
        botonBuscar.place(x=350, y=600)

        botonEliminar = Button(self.ventana, text="Eliminar", font=(
            "Poppins Medium", 10), command=eliminarProductoInterfaz, width=10, state='disabled')
        botonEliminar.place(x=450, y=600)

        botonRegistrarUso = Button(self.ventana, text="Registrar Uso", font=(
            "Poppins Medium", 10), command=registrarUsoProductoInterfaz, width=12)
        botonRegistrarUso.place(x=550, y=600)

        cargarDatosEnTreeView()
    #########################

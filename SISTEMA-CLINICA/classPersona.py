#-*- coding: utf-8 -*-
class Persona:
    def __init__(self, nombre='', apellido='', edad=0, cuilCuit=0, telefono = 0, sexo = ''):
        # Constructor de la clase Persona, inicializa los atributos nombre y apellido
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__cuilCuit = cuilCuit
        self.__telefono=telefono
        self.__sexo = sexo
        
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getEdad(self):
        return self.__edad

    def getCUILCUIT(self):
        return self.__cuilCuit

    def getSexo(self):
        return self.__sexo

    def getTelefono(self):
        return self.__telefono

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setEdad(self, edad):
        self.__edad = edad

    def setCUILCUIT(self, cuilCuit):
        self.__cuilCuit = cuilCuit

    def setSexo(self, sexo):
        self.__sexo = sexo

    def setTelefono(self, telefono):
        self.__telefono = telefono

    # Método de Polimorfismo
    def mostrar(self):
        # Muestra todos los atributos de la persona
        return(f'''
        Nombre: {self.getNombre()}
        Apellido: {self.getApellido()}
        Edad: {self.getEdad()}
        CUIL/CUIT: {self.getCUILCUIT()}
        Teléfono: {self.getTelefono()}
        Sexo: {self.getSexo()}''')

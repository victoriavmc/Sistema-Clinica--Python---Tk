#-*- coding: utf-8 -*-
class Usuario:
    listaUsuarios = []
    def __init__(self, usuario, contrasenia, correo, pin) -> None:
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.__correo = correo
        self.__pin = pin
        Usuario.listaUsuarios.append(self) 
        
    def getUsuario(self):
        return self.__usuario
    
    def getContrasenia(self):
        return self.__contrasenia
    
    def getCorreo(self):
        return self.__correo
    
    def getPin(self):
        return self.__pin
    
    def setUsuario(self, usuario):
        self.__usuario = usuario
    
    def setContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
        
    def setCorreo(self, correo):
        self.__correo = correo
        
    def setPin(self, pin):
        self.__pin = pin
    
    # Método de Polimorfismo
    def mostrar(self):
        return f"""Usuario: {self.getUsuario()}
        Contraseña: {self.getContrasenia()}
        Correo: {self.getCorreo()}
        PIN: {self.getPin()}"""
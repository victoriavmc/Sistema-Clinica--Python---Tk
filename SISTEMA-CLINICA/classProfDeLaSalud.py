from classPersona import Persona
#-*- coding: utf-8 -*-
class ProfDeLaSalud(Persona):
    listaPSalud = []
    def __init__(self, nombre='', apellido='', edad=0, cuilCuit=0, telefono=0, sexo='', titulo='', especialidades=''):
        super().__init__(nombre, apellido, edad, cuilCuit, telefono, sexo)
        self.__titulo = titulo
        self.__especialidades = especialidades
        ProfDeLaSalud.listaPSalud.append(self)
        
        
    def getTitulo(self):
        return self.__titulo
    
    def getEspecialidad(self):
        return self.__especialidades
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setEspecialidad(self, especialidad):
        self.__especialidades = especialidad 
    
    # Método de Polimorfismo
    def mostrar(self):
        return (f'''
        {super().mostrar()}
        Título: {self.getTitulo()}
        Especialidades: {self.getEspecialidad()}
        ''')

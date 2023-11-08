#-*- coding: utf-8 -*-
class Producto:
    listaProductos = []
    def __init__(self, codBarras=0, farmacoUtensilios='', cantidadExistente=0, cantidadMin=40, cantidadMax=200):
        self.__codBarras = codBarras
        self.__farmacoUtensilios = farmacoUtensilios
        self.__cantidadExistente = cantidadExistente
        self.__cantidadMin = cantidadMin
        self.__cantidadMax = cantidadMax
        Producto.listaProductos.append(self)

    def getCodBarras(self):
        return self.__codBarras

    def getFarmacoUtensilios(self):
        return self.__farmacoUtensilios

    def getCantidadExistente(self):
        return self.__cantidadExistente

    def getCantidadMin(self):
        return self.__cantidadMin

    def getCantidadMax(self):
        return self.__cantidadMax

    def setCodBarras(self, codBarras):
        self.__codBarras = codBarras

    def setFarmacoUtensilios(self, farmacoUtensilios):
        self.__farmacoUtensilios = farmacoUtensilios

    def setCantidadExistente(self, cantidadExistente):
        self.__cantidadExistente = cantidadExistente

    def setCantidadMin(self, cantidadMin):
        self.__cantidadMin = cantidadMin

    def setCantidadMax(self, cantidadMax):
        self.__cantidadMax = cantidadMax

    # Método de Polimorfismo
    def mostrar(self):
        return (f'''
            Cod barras: {self.getCodBarras()}
            Farmaco utensilios: {self.getFarmacoUtensilios()}
            Cantidad existente: {self.getCantidadExistente()}
            Cantidad minima: {self.getCantidadMin()}
            Cantidad maxima: {self.getCantidadMax()}''')
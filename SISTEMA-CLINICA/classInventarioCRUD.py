import json
import random
from classValidacion import Validacion
from classProducto import Producto
#-*- coding: utf-8 -*-
# Crear una instancia de la clase Validacion
validacion = Validacion()

def cargarInventario():
    """
    Carga datos del inventario desde un archivo JSON.

    Returns:
        list: Una lista de objetos Producto cargados desde el archivo JSON.
    """
    try:
        with open('inventario.json', 'r') as archivo:
            inventarioData = json.load(archivo)
            for data in inventarioData:
                producto = Producto(data['codBarras'], data['farmacoUtensilios'], data['cantidadExistente'], data['cantidadMin'], data['cantidadMax'])
    except FileNotFoundError:
        pass

class Inventario:
    """
    Clase para gestionar un inventario de productos y realizar operaciones relacionadas con ellos.

    """
    def __init__(self):
        """
        Inicializa una instancia de Inventario cargando datos de inventario existentes, si los hay.

        """
        self.__listaInventario = cargarInventario()

    def guardarInventario(self):
        """
        Guarda los datos del inventario en un archivo JSON.

        Args:
            listaInventario (list): Una lista de objetos Producto a ser guardados en el archivo JSON.
        """
        data = []
        for producto in Producto.listaProductos:
            productoData = {
                'codBarras': producto.getCodBarras(),
                'farmacoUtensilios': producto.getFarmacoUtensilios(),
                'cantidadExistente': producto.getCantidadExistente(),
                'cantidadMin': producto.getCantidadMin(),
                'cantidadMax': producto.getCantidadMax()
            }
            data.append(productoData)

        with open('inventario.json', 'w') as archivo:
            json.dump(data, archivo, indent=4)
        
    def agregarProducto(self, nombreUtensilio, cantidadExistente, cantidadMin, cantidadMax):
        """
        Agrega un nuevo producto al inventario.

        Args:
            nombreUtensilio (str): Nombre o descripción del producto.
            cantidadExistente (int): Cantidad existente en el inventario.
            cantidadMin (int): Cantidad mínima permitida en el inventario.
            cantidadMax (int): Cantidad máxima permitida en el inventario.

        Returns:
            bool: True si el producto se agrega con éxito, False en caso contrario.
        """
        if validacion.validarNumero(cantidadExistente) and validacion.validarNumero(cantidadMin) and validacion.validarNumero(cantidadMax):
            codBarra = random.randint(100000, 999999)
            codBarra = str(codBarra)
            cantidadExistente = int(cantidadExistente)
            cantidadMin =  int(cantidadMin)
            cantidadMax = int(cantidadMax)
            producto = Producto(codBarra, nombreUtensilio, cantidadExistente, cantidadMin, cantidadMax)
            self.guardarInventario()
            return True
        else:
            return False

    def modificarProducto(self, codBarras, nuevoFarmacoUtensilios, nuevaCantidadExistente, nuevaCantidadMin, nuevaCantidadMax):
        """
        Modifica los datos de un producto en el inventario.

        Args:
            codBarras (int): El código de barras del producto a modificar.
            nuevoFarmacoUtensilios (str): El nuevo nombre o descripción del producto.
            nuevaCantidadExistente (int): La nueva cantidad existente en el inventario.
            nuevaCantidadMin (int): La nueva cantidad mínima permitida en el inventario.
            nuevaCantidadMax (int): La nueva cantidad máxima permitida en el inventario.

        Returns:
            bool: True si los datos del producto se modifican con éxito, False en caso contrario.
        """
        if validacion.validarNumero(codBarras):
            producto = self.buscarProducto(codBarras)
            if producto is not None:
                producto.setFarmacoUtensilios(nuevoFarmacoUtensilios)
                producto.setCantidadExistente(nuevaCantidadExistente)
                producto.setCantidadMin(nuevaCantidadMin)
                producto.setCantidadMax(nuevaCantidadMax)
                self.guardarInventario()
                return True
        else:
            return False

    def eliminarProducto(self, codBarras):
        """
        Elimina un producto del inventario.

        Args:
            codBarras (int): El código de barras del producto a eliminar.

        Returns:
            bool: True si el producto se elimina con éxito, False en caso contrario.
        """
        producto = self.buscarProducto(codBarras)
        if producto is not None:
            Producto.listaProductos.remove(producto)
            self.guardarInventario()
            return True
        else:
            return False

    def buscarProducto(self, codBarras):
        """
        Busca un producto en el inventario por su código de barras.

        Args:
            codBarras (int): El código de barras del producto a buscar.

        Returns:
            Producto: El objeto Producto si se encuentra, None en caso contrario.
        """
        if validacion.validarNumero(codBarras):
            for producto in Producto.listaProductos:
                if producto.getCodBarras() == codBarras:
                    return producto
            return None

    def mostrarProducto(self, codBarras):
        """
        Muestra la información de un producto por su código de barras.

        Args:
            codBarras (int): El código de barras del producto cuya información se desea mostrar.

        Returns:
            None: None si el producto no se encuentra, la información del producto si se encuentra.
        """
        if validacion.validarNumero(codBarras):
            producto = self.buscarProducto(codBarras)
            if producto is not None:
                return producto.mostrar()
            else:
                return None
        else:
            return None
        
    def usoUtensilio(self, nombreUtensilio, cantidadUsada):
        """
        Registra el uso de un utensilio y ajusta el stock en el inventario.

        Args:
            nombreUtensilio (str): El nombre o descripción del utensilio a utilizar.
            cantidadUsada (int): La cantidad de unidades del utensilio utilizadas.

        Returns:
            bool: True si el uso se registra con éxito y se ajusta el stock, False en caso contrario.
        """
        cantidadUsada = int(cantidadUsada)
        for producto in Producto.listaProductos:
            if producto.getFarmacoUtensilios() == nombreUtensilio:
                if producto.getCantidadExistente() >= cantidadUsada:
                    producto.setCantidadExistente(producto.getCantidadExistente() - cantidadUsada)
                    self.guardarInventario()
                    if producto.getCantidadExistente() <= producto.getCantidadMin():
                        return 2
                    else:
                        return 1 
                else:
                    return 3
        return 4

    def comprarUtensilio(self, producto):
        """
        Compra más unidades del utensilio hasta que el stock alcance el stock máximo.

        Args:
            producto (Producto): El objeto Producto que representa el utensilio.
        """
        cantidadFaltante = producto.getCantidadMax() - producto.getCantidadExistente()
        if cantidadFaltante > 0:
            cantidadAComprar = producto.getCantidadExistente() + cantidadFaltante
            producto.setCantidadExistente(cantidadAComprar)
            self.guardarInventario()
            return True
        return False
    
    def encontrarProductoPorNombre(self, nombre):
        """
        Busca un producto en el inventario por su nombre.

        Args:
            nombre (str): El nombre del producto a buscar.

        Returns:
            Producto: El objeto Producto si se encuentra, None en caso contrario.
        """
        for producto in Producto.listaProductos:
            if producto.getFarmacoUtensilios() == nombre:
                return producto
        return None
from classProfDeLaSalud import ProfDeLaSalud
from classValidacion import Validacion
import json

# Crear una instancia de la clase Validacion
validacion = Validacion()

def cargarMedico():
    """
    Carga datos de médicos desde un archivo JSON.

    Returns:
        list: Una lista de objetos ProfDeLaSalud cargados desde el archivo JSON.
    """
    try:
        with open('medicos.json', 'r') as archivo:
            medicoData = json.load(archivo)
            for data in medicoData:
                # Crear objetos ProfDeLaSalud a partir de los datos del archivo JSON
                medico = ProfDeLaSalud(data['nombre'], data['apellido'], data['edad'], data['cuilCuit'],
                                       data['telefono'], data['sexo'], data['titulo'], data['especialidad'])
    except FileNotFoundError:
        pass

cargarMedico()

class Medicos:
    def __init__(self) -> None:
        pass

    def guardarMedico(self):
        """
        Guarda datos de médicos en un archivo JSON.
        """
        data = []
        for medico in ProfDeLaSalud.listaPSalud:
            medicoData = {
                'nombre': medico.getNombre(),
                'apellido': medico.getApellido(),
                'edad': medico.getEdad(),
                'cuilCuit': medico.getCUILCUIT(),
                'telefono': medico.getTelefono(),
                'sexo': medico.getSexo(),
                'titulo': medico.getTitulo(),
                'especialidad': medico.getEspecialidad()
            }
            data.append(medicoData)

        with open('medicos.json', 'w') as archivo:
            json.dump(data, archivo, indent=4)

    def noRepetircuilCuit(self, cuilCuit):
        """
        Comprueba si el número de CUIL/CUIT ya existe en la lista de profesionales de la salud.

        Args:
            cuilCuit (str): Número de CUIL/CUIT a verificar.

        Returns:
            bool: True si no se encuentra repetido, False en caso contrario.
        """
        for profesional in ProfDeLaSalud.listaPSalud:
            if profesional.getCUILCUIT() == cuilCuit:
                return False
        return True

    def noRepetirTelefono(self, telefono):
        """
        Comprueba si el número de teléfono ya existe en la lista de profesionales de la salud.

        Args:
            telefono (str): Número de teléfono a verificar.

        Returns:
            bool: True si no se encuentra repetido, False en caso contrario.
        """
        for profesional in ProfDeLaSalud.listaPSalud:
            if telefono == profesional.getTelefono():
                return False
        return True

    def agregarMedico(self, nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidad):
        """
        Agrega un nuevo médico a la lista de profesionales de la salud si cumple con las validaciones.

        Args:
            nombre (str): Nombre del médico.
            apellido (str): Apellido del médico.
            edad (int): Edad del médico.
            cuilCuit (str): Número de CUIL/CUIT del médico.
            telefono (str): Número de teléfono del médico.
            sexo (str): Género del médico.
            titulo (str): Título del médico.
            especialidad (str): Especialidad del médico.

        Returns:
            bool: True si el médico se agregó con éxito, False si no se pudo agregar.
        """
        nombre = nombre.title()
        apellido = apellido.title()
        if self.noRepetircuilCuit(cuilCuit) and self.noRepetirTelefono(telefono):
            if validacion.validarMedico(nombre, apellido, edad, cuilCuit, telefono):
                medico = ProfDeLaSalud(
                    nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidad)
                self.guardarMedico()
                return True
        else:
            return False

    def buscarMedico(self, cuilCuit):
        """
        Busca un médico por su número de CUIL/CUIT.

        Args:
            cuilCuit (str): Número de CUIL/CUIT a buscar.

        Returns:
            ProfDeLaSalud or None: El objeto ProfDeLaSalud si se encuentra, None si no se encuentra.
        """
        if validacion.validarContarNumero(cuilCuit, 11):
            for medico in ProfDeLaSalud.listaPSalud:
                if medico.getCUILCUIT() == cuilCuit:
                    return medico
            return None

    def modificarMedico(self, nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidad):
        """
        Modifica los datos de un médico si cumple con las validaciones.

        Args:
            nombre (str): Nuevo nombre del médico.
            apellido (str): Nuevo apellido del médico.
            edad (int): Nueva edad del médico.
            cuilCuit (str): Nuevo número de CUIL/CUIT del médico.
            telefono (str): Nuevo número de teléfono del médico.
            sexo (str): Nuevo género del médico.
            titulo (str): Nuevo título del médico.
            especialidad (str): Nueva especialidad del médico.

        Returns:
            bool: True si la modificación se realizó con éxito, False si no se pudo modificar.
        """
        nombre = nombre.title()
        apellido = apellido.title()
        if validacion.validarMedico(nombre, apellido, edad, cuilCuit, telefono):
            medico = self.buscarMedico(cuilCuit)
            if medico is not None:
                medico.setNombre(nombre)
                medico.setApellido(apellido)
                medico.setEdad(edad)
                medico.setTelefono(telefono)
                medico.setCUILCUIT(cuilCuit)
                medico.setSexo(sexo)
                medico.setTitulo(titulo)
                medico.setEspecialidad(especialidad)
                self.guardarMedico()
                return True
            else:
                return False
        else:
            return False

    def mostrarMedico(self, cuilCuit):
        """
        Muestra los datos de un médico por su número de CUIL/CUIT.

        Args:
            cuilCuit (str): Número de CUIL/CUIT del médico a mostrar.

        Returns:
            str or False: Los datos del médico en forma de cadena si se encuentra, False si no se encuentra.
        """
        medico = self.buscarMedico(cuilCuit)
        if medico is not None:
            return medico.mostrar()
        else:
            return False

    def eliminarMedico(self, cuilCuit):
        """
        Elimina un médico de la lista de profesionales de la salud por su número de CUIL/CUIT.

        Args:
            cuilCuit (str): Número de CUIL/CUIT del médico a eliminar.

        Returns:
            bool: True si la eliminación se realizó con éxito, False si no se pudo eliminar.
        """
        medico = self.buscarMedico(cuilCuit)
        if medico is not None:
            ProfDeLaSalud.listaPSalud.remove(medico)
            self.guardarMedico()
            return True
        else:
            return False
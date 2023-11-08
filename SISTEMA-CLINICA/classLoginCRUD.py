import json
import random
from classValidacion import Validacion
from classUsuario import Usuario
# -- coding: utf-8 --
# Crear una instancia de la clase Validacion
Validacion = Validacion()


def cargarUsuarios():
    """
    Carga datos de usuarios desde un archivo JSON.

    Returns:
        list: Una lista de objetos Usuario cargados desde el archivo JSON.
    """
    try:
        with open("usuarios.json", "r") as file:
            data = json.load(file)
            for userData in data:
                usuario = Usuario(
                    userData['usuario'], userData['contrasenia'], userData['correo'], userData['pin'])
    except FileNotFoundError:
        pass


cargarUsuarios()


class Login:
    """
    Clase para gestionar el proceso de inicio de sesión, registro y gestión de usuarios.
    """

    def _init_(self) -> None:
        """
        Inicializa una instancia de Login cargando datos de usuarios existentes, si los hay.
        """

    def guardarUsuarios(self):
        """
        Guarda los datos de usuarios en un archivo JSON.

        Args:
            usuarios (list): Una lista de objetos Usuario a ser guardados en el archivo JSON.
        """
        data = []
        for usuario in Usuario.listaUsuarios:
            userData = {
                'usuario': usuario.getUsuario(),
                'contrasenia': usuario.getContrasenia(),
                'correo': usuario.getCorreo(),
                'pin': usuario.getPin()
            }
            data.append(userData)

        with open("usuarios.json", "w") as file:
            json.dump(data, file, indent=4)

    def verificarExistencia(self, usuario, correo):
        """
        Verifica si un nombre de usuario ya existe en el sistema.

        Args:
            usuario (str): Nombre de usuario a verificar.

        Returns:
            bool: True si el usuario ya existe, False en caso contrario.
        """
        for user in Usuario.listaUsuarios:
            if user.getUsuario() == usuario or user.getCorreo() == correo:
                return True
        return False

    def verificarExistenciaUser(self, usuario):
        """
        Verifica si un nombre de usuario ya existe en el sistema.

        Args:
            usuario (str): Nombre de usuario a verificar.

        Returns:
            bool: True si el usuario ya existe, False en caso contrario.
        """
        for user in Usuario.listaUsuarios:
            if user.getUsuario() == usuario:
                return True
        return False

    def registrarUsuario(self, usuario, contrasenia, correo, pin):
        """
        Registra un nuevo usuario en el sistema.

        Args:
            usuario (str): Nombre de usuario.
            contrasenia (str): Contraseña del usuario.
            correo (str): Correo electrónico del usuario.

        Returns:
            bool: True si el usuario se registra con éxito, False en caso contrario.
        """
        if Validacion.validarUsuario(usuario, contrasenia, correo):
            existencia = self.verificarExistencia(usuario, correo)
            if not existencia:
                usuario = Usuario(usuario, contrasenia, correo, pin)
                self.guardarUsuarios()
                return True
        else:
            return False

    def iniciarSesion(self, usuario, contrasenia):
        """
        Inicia sesión de un usuario en el sistema.

        Args:
            usuario (str): Nombre de usuario.
            contrasenia (str): Contraseña del usuario.

        Returns:
            bool: True si la sesión se inicia con éxito, False en caso contrario.
        """
        for user in Usuario.listaUsuarios:
            if user.getUsuario() == usuario and user.getContrasenia() == contrasenia:
                return True
        return False

    def verificarExistenciaCorreo(self, pin, correo):
        """
        Verifica si un nombre de usuario ya existe en el sistema.

        Args:
            usuario (str): Nombre de usuario a verificar.

        Returns:
            bool: True si el usuario ya existe, False en caso contrario.
        """
        for usuario in Usuario.listaUsuarios:
            if usuario.getPin() == pin and usuario.getCorreo() == correo:
                return True
        return False

    def reestablecerContrasenia(self, pUsuario, contrasenia, correo, pin):
        """
        Restablece la contraseña de un usuario utilizando su PIN.

        Args:
            pin (int): PIN del usuario.
            contrasenia (str): Nueva contraseña del usuario.

        Returns:
            bool: True si la contraseña se restablece con éxito, False en caso contrario.
        """
        if Validacion.validarUsuario(pUsuario, contrasenia, correo):
            for usuario in Usuario.listaUsuarios:
                if usuario.getCorreo() == correo:
                    if usuario.getUsuario() == pUsuario:
                        usuario.setContrasenia(contrasenia)
                        usuario.setPin(pin)
                        self.guardarUsuarios()
                        return True
                    else:
                        if not self.verificarExistenciaUser(pUsuario):
                            usuario.setUsuario(pUsuario)
                            usuario.setContrasenia(contrasenia)
                            usuario.setPin(pin)
                            self.guardarUsuarios()
                            return True
                        else:
                            return False
        return False


    def eliminarCuenta(self, pin):
        """
        Elimina la cuenta de un usuario utilizando su PIN.

        Args:
            pin (int): PIN del usuario.

        Returns:
            bool: True si la cuenta se elimina con éxito, False en caso contrario.
        """
        if Validacion.validarNumero(pin):
            usuario = self.buscarUsuario(pin)
            if usuario is not None:
                Usuario.listaUsuarios.remove(usuario)
                self.guardarUsuarios()
                return True
        else:
            return False

    def buscarUsuario(self, pin):
        """
        Busca un usuario por su PIN.

        Args:
            pin (int): PIN del usuario a buscar.

        Returns:
            Usuario: El objeto Usuario si se encuentra, None en caso contrario.
        """
        if Validacion.validarNumero(pin):
            for usuario in Usuario.listaUsuarios:
                if usuario.getPin() == pin:
                    return usuario
            return None
        else:
            return False

    def mostrarUsuario(self, pin):
        """
        Muestra la información de un usuario por su PIN.

        Args:
            pin (int): PIN del usuario cuya información se desea mostrar.

        Returns:
            None: None si el usuario no se encuentra, la información del usuario si se encuentra.
        """
        if Validacion.validarNumero(pin):
            usuario = self.buscarUsuario(pin)
            if usuario is not None:
                return usuario.mostrar()
            else:
                return None
        else:
            return None
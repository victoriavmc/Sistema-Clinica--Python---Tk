import re

class Validacion:

    def validarUsuario(self, usuario, contrasenia, correo):
        """
        Valida un usuario, contraseña y correo.

        Args:
            usuario (str): Nombre de usuario.
            contrasenia (str): Contraseña.
            correo (str): Dirección de correo.

        Returns:
            bool: True si la validación es exitosa, False si no cumple con los requisitos.
        """
        if len(usuario) >= 4 and len(contrasenia) >= 8:
            if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                return True
        return False

    def validarMedico(self, nombre, apellido, edad, cuilCuit, telefono):
        """
        Valida los datos de un médico.

        Args:
            nombre (str): Nombre del médico.
            apellido (str): Apellido del médico.
            edad (str): Edad del médico.
            cuilCuit (str): Número de CUIL/CUIT del médico.
            telefono (str): Número de teléfono del médico.

        Returns:
            bool: True si la validación es exitosa, False si no cumple con los requisitos.
        """
        if not self.validarNumero(nombre) and not self.validarNumero(apellido):
            if self.validarNumero(edad) and self.validarNumero(cuilCuit) and self.validarNumero(telefono):
                if self.validarContarNumero(cuilCuit, 11) and self.validarContarNumero(telefono, 8):
                    return True
        return False

    def validarNumero(self, parametro):
        """
        Valida si un parámetro es un número.

        Args:
            parametro (str): El valor a validar.

        Returns:
            bool: True si es un número, False si no lo es.
        """
        if parametro.isdigit():
            return True
        return False

    def validarContarNumero(self, num, cantidad):
        """
        Valida si un número tiene una longitud específica.

        Args:
            num (str): El número a validar.
            cantidad (int): La longitud deseada.

        Returns:
            bool: True si tiene la longitud deseada, False si no.
        """
        if len(num) == cantidad:
            return True
        return False

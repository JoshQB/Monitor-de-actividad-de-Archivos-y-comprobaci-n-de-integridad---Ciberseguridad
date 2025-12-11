import hashlib

class ArchivoMonitoreado:
    def __init__(self, ruta):
        self.ruta = ruta  # Guarda la ruta del archivo que se va a monitorear

    def calcular_hash(self):
        try:
            # Abre el archivo en modo binario y lee su contenido
            with open(self.ruta, "rb") as f:
                contenido = f.read()
                # Calcula el hash SHA-256 del contenido y lo devuelve como cadena hexadecimal
                return hashlib.sha256(contenido).hexdigest()
        except FileNotFoundError:
            # Si el archivo no existe, devuelve None
            return None

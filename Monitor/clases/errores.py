# Define una excepción personalizada para violaciones de integridad
class IntegridadVioladaError(Exception):
    def __init__(self, archivo, mensaje="Integridad del archivo violada."):
        # Guarda el nombre del archivo que causó la excepción
        self.archivo = archivo

        # Llama al constructor de la clase base 'Exception' con un mensaje personalizado
        super().__init__(f"{mensaje} Archivo: {archivo}")

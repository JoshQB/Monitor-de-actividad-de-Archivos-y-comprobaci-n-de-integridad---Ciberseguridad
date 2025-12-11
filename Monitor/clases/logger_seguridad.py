# Importa el módulo logging para registrar mensajes en archivos de texto
import logging

# Clase que se encarga de registrar eventos de seguridad en un archivo de log
class LoggerSeguridad:
    def __init__(self, archivo_log="alertas.log"):
        # Crea un logger con el nombre "LoggerSeguridad"
        self.logger = logging.getLogger("LoggerSeguridad")

        # Establece el nivel mínimo de registro (INFO en este caso)
        self.logger.setLevel(logging.INFO)

        # Crea un manejador que escribe los logs en el archivo especificado
        handler = logging.FileHandler(archivo_log)

        # Define el formato de los mensajes de log: fecha, nivel y mensaje
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Aplica el formato al manejador
        handler.setFormatter(formatter)

        # Añade el manejador al logger
        self.logger.addHandler(handler)

    # Método para registrar una alerta (nivel WARNING)
    def log_alerta(self, mensaje):
        self.logger.warning(mensaje)

    # Método para registrar información general (nivel INFO)
    def log_info(self, mensaje):
        self.logger.info(mensaje)

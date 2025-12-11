# Importa módulos necesarios para trabajar con archivos JSON, rutas del sistema y fechas
import json
import os
from datetime import datetime

# Importa clases personalizadas para monitorear archivos, registrar eventos y manejar errores
from clases.archivo_monitoreado import ArchivoMonitoreado
from clases.logger_seguridad import LoggerSeguridad
from clases.errores import IntegridadVioladaError

# Clase principal que se encarga de verificar la integridad de los archivos
class Verificador:
    def __init__(self, config_path="monitoreo_config.json", hash_guardado="hashes.json"):
        # Ruta del archivo de configuración que contiene la lista de archivos a monitorear
        self.config_path = config_path

        # Ruta del archivo donde se guardan los hashes previos de los archivos
        self.hash_guardado = hash_guardado

        # Instancia del logger para registrar eventos de seguridad
        self.logger = LoggerSeguridad()

        # Lista de archivos a monitorear, cargada desde el archivo de configuración
        self.archivos = self.cargar_configuracion()

        # Diccionario con los hashes previamente guardados
        self.hashes_previos = self.cargar_hashes()

    # Carga la lista de archivos a monitorear desde el archivo JSON de configuración
    def cargar_configuracion(self):
        with open(self.config_path, "r") as f:
            datos = json.load(f)
        return datos["archivos"]

    # Carga los hashes guardados previamente desde el archivo JSON
    def cargar_hashes(self):
        if os.path.exists(self.hash_guardado):
            with open(self.hash_guardado, "r") as f:
                return json.load(f)
        return {}  # Si no existe el archivo, devuelve un diccionario vacío

    # Guarda los hashes actualizados en el archivo JSON
    def guardar_hashes(self):
        with open(self.hash_guardado, "w") as f:
            json.dump(self.hashes_previos, f, indent=4)

    # Verifica la integridad de cada archivo monitoreado
    def verificar(self):
        for archivo in self.archivos:
            monitor = ArchivoMonitoreado(archivo)  # Crea un objeto para monitorear el archivo
            hash_actual = monitor.calcular_hash()  # Calcula el hash actual del archivo

            # Si el archivo no se encuentra, registra una alerta y continúa con el siguiente
            if hash_actual is None:
                self.logger.log_alerta(f"Archivo no encontrado: {archivo}")
                continue

            # Obtiene el hash anterior guardado para este archivo
            hash_anterior = self.hashes_previos.get(archivo)

            # Si el hash anterior existe y es diferente al actual, se detecta una violación de integridad
            if hash_anterior and hash_anterior != hash_actual:
                mensaje = f"¡ALERTA! Integridad violada en {archivo}"
                self.logger.log_alerta(mensaje)  # Registra la alerta
                raise IntegridadVioladaError(archivo)  # Lanza una excepción personalizada

            else:
                # Si no hay cambios, registra que la verificación fue exitosa
                self.logger.log_info(f"Verificación exitosa: {archivo}")

            # Actualiza el hash guardado con el nuevo valor
            self.hashes_previos[archivo] = hash_actual

        # Guarda todos los hashes actualizados en el archivo JSON
        self.guardar_hashes()

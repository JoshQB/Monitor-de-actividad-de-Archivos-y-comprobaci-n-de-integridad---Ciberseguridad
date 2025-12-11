#Programacion 1
# grupo 3
# integrantes : 
# JOSEPH DAVID QUESADA BONILLA
# DARREN JOSUE NUÑEZ PARRA 
# MARIA PAULA QUIROS VARGAS
# CAMILA CASTILLO CASTRO

# proyecto final: Monitor de actividad de Archivos y comprovacion de integridad - Ciberseguridad

# Importa la clase Verificador, que se encarga de revisar la integridad de los archivos
from clases.verificador import Verificador

# Importa una excepción personalizada que se lanza si se detecta una violación de integridad
from clases.errores import IntegridadVioladaError

# Importa la clase que representa un archivo que se puede monitorear (calcular su hash, etc.)
from clases.archivo_monitoreado import ArchivoMonitoreado

# Función principal del programa
def main():
    # Crea una instancia del verificador de integridad
    verificador = Verificador()

    # Bucle infinito para mostrar el menú hasta que el usuario decida salir
    while True:
        # Muestra el menú de opciones
        print("\n--- Menú de Monitor de Integridad ---")
        print("1. Calcular y mostrar hash SHA-256 de cada archivo")
        print("2. Comparar cambios de hash y detectar modificaciones")
        print("3. Ver alertas de integridad")
        print("4. Salir")

        # Solicita al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        # Opción 1: Mostrar el hash SHA-256 actual de cada archivo monitoreado
        if opcion == "1":
            print("\n--- Hash SHA-256 de archivos críticos ---")
            for archivo in verificador.archivos:
                monitor = ArchivoMonitoreado(archivo)  # Crea un objeto para monitorear el archivo
                hash_actual = monitor.calcular_hash()  # Calcula el hash actual del archivo
                print(f"Archivo: {archivo}\nSHA-256: {hash_actual}\n")

        # Opción 2: Verificar si algún archivo ha sido modificado
        elif opcion == "2":
            print("\n--- Comparación de hashes y detección de modificaciones ---")
            try:
                verificador.verificar()  # Compara los hashes actuales con los esperados
                print("Verificación completada sin alteraciones.")
            except IntegridadVioladaError as e:
                # Si se detecta una modificación, se lanza una alerta
                print(f"¡ALERTA! Error de integridad detectado: {e}")

        # Opción 3: Mostrar las alertas registradas en el archivo "alertas.log"
        elif opcion == "3":
            print("\n--- Alertas de integridad ---")
            try:
                with open("alertas.log", "r", encoding="latin-1") as f:
                    print(f.read())
            except FileNotFoundError:
                print("No hay alertas registradas.")

        # Opción 4: Salir del programa
        elif opcion == "4":
            print("Saliendo del monitor de integridad.")
            break

        # Si el usuario ingresa una opción inválida
        else:
            print("Opción inválida.")

# Punto de entrada del programa: se ejecuta la función main si el archivo se corre directamente
if __name__ == "__main__":
    main()

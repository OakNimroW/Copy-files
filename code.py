import os
import shutil

# Ruta de la carpeta de origen y destino
carpeta_origen = "/path/to/origen"
carpeta_destino = "/path/to/destino"

# Prefijo y extensión de los archivos de destino
prefijo = "Prefijo_Titulo-"
extension_destino = ".JPG"

# Obtener la lista de archivos en la carpeta de origen
archivos = os.listdir(carpeta_origen)

# Contador para el número de archivo
contador = 1

# Recorrer los archivos y copiarlos con el nuevo nombre
for archivo in archivos:
    # Obtener la ruta completa del archivo de origen
    ruta_origen = os.path.join(carpeta_origen, archivo)

    # Verificar si es un archivo y no una carpeta
    if os.path.isfile(ruta_origen):
        # Generar el nuevo nombre de archivo con el número de contador
        nuevo_nombre = prefijo + str(contador).zfill(3) + extension_destino

        # Obtener la ruta completa del archivo de destino
        ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)

        # Copiar el archivo de origen al destino con el nuevo nombre
        shutil.copy2(ruta_origen, ruta_destino)

        # Incrementar el contador
        contador += 1

print("Archivos copiados con éxito.")

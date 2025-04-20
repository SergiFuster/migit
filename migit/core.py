import os
from migit.utils import hide
import hashlib

MIGIT_DIR = ".migit"
OBJECTS_DIR = os.path.join(MIGIT_DIR, "objects")
INDEX_FILE = os.path.join(MIGIT_DIR, "index")


def init():
    if os.path.exists(".migit"):
        print("El directorio de .migit ya existe.")
        return
    os.mkdir(".migit")
    os.mkdir(".migit/objects")
    os.mkdir(".migit/refs")
    with open(".migit/HEAD", "w") as f:
        f.write("ref: refs/heads/master\n")

    hide(".migit")
    print("Repositorio .migit creado con éxito.")


def hash_archivo(contenido):
    sha1 = hashlib.sha1()
    sha1.update(contenido)
    return sha1.hexdigest()


def guardar_objeto(contenido, nombre):
    objeto_path = os.path.join(OBJECTS_DIR, nombre)
    if not os.path.exists(objeto_path):
        with open(objeto_path, "wb") as f:
            f.write(contenido)
            print(f"Objeto guardado en {objeto_path}.")
    else:
        print(f"El objeto {nombre} ya existe en {objeto_path}.")


def actualizar_index(ruta_archivo, hash_objeto):
    index = {}
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as f:
            for linea in f:
                archivo, objeto = linea.strip().split(" ")
                index[archivo] = objeto
    index[ruta_archivo] = hash_objeto

    with open(INDEX_FILE, "w") as f:
        for archivo, objeto in index.items():
            f.write(f"{archivo} {objeto}\n")

    print(f"Archivo {ruta_archivo} agregado al índice con hash {hash_objeto}.")


def agregar_archivo(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print(f"El archivo {ruta_archivo} no existe.")
        return

    with open(ruta_archivo, "rb") as f:
        contenido = f.read()

    hash_objeto = hash_archivo(contenido)

    guardar_objeto(contenido, hash_objeto)

    actualizar_index(ruta_archivo, hash_objeto)

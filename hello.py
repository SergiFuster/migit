import os
import sys


def init():
    if os.path.exists(".migit"):
        print("El directorio de .migit ya existe.")
        return
    os.mkdir(".migit")
    os.mkdir(".migit/objects")
    os.mkdir(".migit/refs")
    with open(".migit/HEAD", "w") as f:
        f.write("ref: refs/heads/master\n")

    print("Repositorio .migit creado con éxito.")


if __name__ == "__main__":
    args = sys.argv[1:]
    eval(args[0] + "()")

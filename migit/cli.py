from migit.core import init
from migit.core import agregar_archivo
from migit.core import hacer_commit
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="migit", description="Programa de control de versiones"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Crear un nuevo repositorio.")

    add_parser = subparsers.add_parser(
        "add", help="Agregar un archivo al staging area."
    )
    add_parser.add_argument("file", help="Archivo a agregar.")

    commit_parser = subparsers.add_parser("commit", help="Guardar cambios.")
    commit_parser.add_argument(
        "-m", "--message", required=True, help="Mensaje del commit."
    )

    return parser.parse_args()


def main():
    args = parse_args()
    match args.command:
        case "init":
            init()
        case "add":
            agregar_archivo(args.file)
        case "commit":
            hacer_commit(args.message)


if __name__ == "__main__":
    main()

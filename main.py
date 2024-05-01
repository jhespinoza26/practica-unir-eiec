"""
License: Apache
Organization: UNIR
"""

import os
import sys
from deep_translator import GoogleTranslator

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, order):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    asc = True if order == "asc" else False
    return sorted(items, reverse=(not asc))


def remove_duplicates_from_list(items):
    return list(set(items))

def traducir_lista(items):
    traductor = GoogleTranslator(source='es', target='en')
    resultado = traductor.translate_batch(items)
    return resultado


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)


    print("Texto de la lista ordenado: ", sort_list(word_list))
    print("Texto de la lista traducido: " , traducir_lista(sort_list(word_list)))


import os
# Muestra directoro
def mostrar_directorio():
    directorio = os.getcwd()
    return directorio

# Lista un directorio
def listar_directorio(path):
     lista_directorios = os.listdir(path)
     print("Lista directorios")
     for directorio in lista_directorios:
          print(directorio)

# Crea un directorio
def crear_directorio(name_directorio):
     os.mkdir(name_directorio)
     print(f"Nuevo directorio '{name_directorio}' creado")

# Comprueba si un fichero existe

def comprobar_fichero(name):
    if os.path.exists(name):
          print(f"El fichero '{name}' existe")
    else:
         print(f"El fichero '{name}' no existe")


# Se ejecutan las funciones si este fichero es el main
if __name__ == "__main__":
     print("Directorio actual: ", mostrar_directorio())
     listar_directorio(mostrar_directorio())
     #crear_directorio("prueba")
     comprobar_fichero(".git")
     comprobar_fichero("fichero_inexistente.txt")
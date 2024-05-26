class Libro:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = True
    
    def prestamo(self):
        if self.estado:
            self.estado = False
            return True
        else:
            print("No quedan existencias para prestar de este libro")
            return False

    def devolucion(self):
        if not self.estado:
            self.estado = True
            return True
        else:
            print("Este libro ya habia sido devuelto con anterioridad")
            return False

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_libros = [] 
    
    def pedir_libro(self, libro):
        if libro.prestamo():
            self.lista_libros.append(libro)
            return True
        else:
            return False
        
    def devolver_libro(self, libro):
        if libro.devolucion():
            self.lista_libros.remove(libro)
            return True
        else:
            return False

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def prestar_libro(self, usuario, titulo_libro):
        for libro in self.libros_disponibles:
            if(libro.titulo == titulo_libro):
                if(usuario.pedir_libro(libro)):
                    self.libros_disponibles.remove(libro)
                    return True
                else:
                    return False
            else:
                return False
            
    def devolver_libro(self, usuario, titulo_libro):
        for libro in usuario.lista_libros:
            if(libro.titulo == titulo_libro):
                if(usuario.devolver_libro(libro)):
                    self.libros_disponibles.append(libro)
                    return True
                else:
                    return False
            else:
                return False
            
    def mostrar_libros_disponibles(self):
        if(len(self.libros_disponibles) > 0):
            print("libros disponibles: ")
            for libro in self.libros_disponibles:
                print(f"- {libro.titulo} por {libro.autor}")
        else:
            print("No hay libros disponibles")

### Ejemplo de uso 
libro1 = Libro("El Alquimista", "Paulo Coelho") 
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez") 
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry") 
biblioteca = Biblioteca() 

biblioteca.agregar_libro(libro1) 
biblioteca.agregar_libro(libro2) 
biblioteca.agregar_libro(libro3) 
usuario1 = Usuario("Alice") 
usuario2 = Usuario("Bob") 
biblioteca.prestar_libro(usuario1, "El Alquimista") 
biblioteca.prestar_libro(usuario2, "Cien años de soledad") 
biblioteca.mostrar_libros_disponibles() 
biblioteca.devolver_libro(usuario1, "El Alquimista") 
biblioteca.mostrar_libros_disponibles() 



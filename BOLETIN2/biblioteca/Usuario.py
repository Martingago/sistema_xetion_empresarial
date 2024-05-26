from Libro import Libro

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_libros = [] 
    
    def pedir_libro(self, Libro):
        if Libro.prestamo():
            self.lista_libros.append(Libro)
            return True
        else:
            return False
        
    def devolver_libro(self, Libro):
        if Libro.devolucion():
            self.lista_libros.remove(Libro)
            return True
        else:
            return False
            

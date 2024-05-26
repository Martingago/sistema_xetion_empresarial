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

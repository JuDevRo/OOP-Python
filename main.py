class Libro:
    pass
    def __init__(self, titulo, autor, isbn, available):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.available = available
        self.lended_count = 0

        def __str__(self):
            return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {'Disponible' if self.available else 'No disponible'}"

        def cambiar_disponibilidad(self, disponible):
            if self.available:
                self.available = False
            return "El libro no está disponible para prestar."
        
        def devolver(self):
            self.available = True
        return "El libro ha sido devuelto y ahora está disponible."

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-84-376-0494-7", True)
otro_libro = Libro("El Coronel no tiene quien le escriba", "Gabriel García Márquez", "978-84-376-0495-4", True)

mi_libro.prestar()
mi_libro.devolver()

print(mi_libro.titulo)
print(mi_libro.autor)
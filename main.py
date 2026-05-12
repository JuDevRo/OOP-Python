class Libro:
    pass
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez")
otro_libro = Libro("El Coronel no tiene quien le escriba", "Gabriel García Márquez")

print(mi_libro.titulo)
print(mi_libro.autor)
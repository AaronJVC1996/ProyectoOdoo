class Libro:
    def __init__(self, precio, tiempoTotal, fecha, titulo, ISBN):
        self.precio = precio
        self.tiempoTotal = tiempoTotal
        self.fecha = fecha
        self.titulo = titulo
        self.ISBN = ISBN

    def calcularPrecioTotal(self):
        return self.precio * self.tiempoTotal
    
    
        
class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        if nivel > 100 or nivel < 1: 
            raise ValueError("El nivel del pokemon debe estar entre los niveles 1 a 100")
        self.nivel = nivel

    def subir_nivel(self):
        
        if self.nivel == 100: 
            print("Tu pokemon ya alcanzo su maximo nivel! - Intenta subir de nivel otro!")
        else:
            self.nivel += 1

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"       
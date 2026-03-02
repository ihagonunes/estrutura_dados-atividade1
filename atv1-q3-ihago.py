
from random import randint

class Livro: 
    def __init__(self, titulo: str, autor: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel        
        
    def __str__(self):
        if self.disponivel: return f'Livro {self.titulo} de {self.autor} (disponível)'
        else: return f'Livro {self.titulo} de {self.autor} (indisponível)'
        
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"Livro {self.titulo} emprestado com sucesso!")
        else: print(f"Livro {self.titulo} não está disponível para empréstimo")
        
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
        else: print(f"Livro {self.titulo} não foi emprestado")
        
class Usuario:
    def __init__(self, ra: int, nome:  str, livrosEmprestados: list):
        self.ra = ra
        self.nome = nome
        self.livrosEmprestados = livrosEmprestados
    

class Biblioteca:
    def __init__(self, listaLivros: list, listaUsuarios: list):
        self.listaLivros = listaLivros
        self.listaUsuarios = listaUsuarios
        
livro1 = Livro("Meu Livro", "Franz Kafka")
livro1.emprestar()

print(livro1)
livro1.devolver()
print(livro1)
livro1.devolver()

        

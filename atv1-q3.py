from random import randint

class livro:
    def __init__(self,titulo = "", autor = "", disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
        
    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Disponivel: {self.disponivel}"
    
class Usuario:
    def __init__(self, ra = randint(100,999), nome = "", lista= []):
        self.ra = ra
        self.nome = nome
        self.lista = lista

class Biblioteca:
    def __init__(self, listLivros = [], listUsuario = []):
        self.listLivros = listLivros
        self.listUsuario = listUsuario
        
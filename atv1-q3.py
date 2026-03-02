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
    
    def emprestar_livro(self, livro):
        self.livrosEmprestados.append(livro)
        
        
    def devolver_livro(self, livro):
        if livro in self.livrosEmprestados:
            self.livrosEmprestados.remove(livro)
            
    def listar_livros(self):
        if not self.livrosEmprestados:
            print(f"O usuário não possui livros emprestados")  
        else:
            for livro in self.livrosEmprestados:
                print(livro)
    
class Biblioteca:
    def __init__(self, listaLivros: list, listaUsuarios: list):
        self.listaLivros = listaLivros
        self.listaUsuarios = listaUsuarios
        
    def cadastrar_livro(self, livro: Livro):
        for livroCadastrado in self.listaLivros:
            if livroCadastrado.titulo == livro.titulo:
                print(f"O livro de título {livro.titulo} já foi cadastrado")
                return
        self.listaLivros.append(livro)
        print(f"Cadastro de livro realizado com sucesso")
        
    def cadastrar_usuario(self, usuario: Usuario):
        for usuarioCadastrado in self.listaUsuarios:
            if usuarioCadastrado.ra == usuario.ra:
                print(f"Usuário com o RA {usuario.ra} já existe")
                return
        self.listaUsuarios.append(usuario)
        print(f"Cadastro de usuário realizado com sucesso")
        
    def realizar_emprestimo(self, ra: int, tituloLivro: str):
        usuarioEncontrado = None
        
        for usuarioCadastrado in self.listaUsuarios:
            if usuarioCadastrado.ra == ra:
                usuarioEncontrado = usuarioCadastrado
                break
            
        livroEncontrado = None
        for livroCadastrado in self.listaLivros:
            if livroCadastrado.titulo == tituloLivro:
                livroEncontrado = livroCadastrado
                break
        
        if usuarioEncontrado and livroEncontrado:
            if livroEncontrado.disponivel:
                livroEncontrado.emprestar()
                usuarioEncontrado.emprestar_livro(livroEncontrado)
            else: print(f"O livro '{tituloLivro}' já está emprestado")
        else: print("Usuário ou Livro não existe")
        
    def realizar_devolucao(self, ra: int, tituloLivro: str):
        usuarioEncontrado = None
        for usuarioCadastrado in self.listaUsuarios:
            if usuarioCadastrado.ra == ra:
                usuarioEncontrado = usuarioCadastrado
                break
        
        if usuarioEncontrado:
            livroEncontrado = None
            for livroCadastrado in self.listaLivros:
                if livroCadastrado == tituloLivro:
                    livroEncontrado = livroCadastrado
                    break
            
            if livroEncontrado:
                livroEncontrado.devolver()
                usuarioEncontrado.devolver_livro(livroEncontrado)
                print(f"Livro {tituloLivro} devolvido")
            else: print(f"O usuário {usuarioEncontrado.nome} não possui esse livro")
        else:
            print(f"Usuário não encontrado.")
    
    def listar_livros_disponiveis(self):
        print("\nLivros Disponíveis:")
        verificacaoEncontrou = False
        for livro in self.listaLivros:
            if livro.disponivel:
                print(livro)
                verificacaoEncontrou = True
        if not verificacaoEncontrou:
            print("Não há livros disponíveis")
    
    def listar_livros_emprestados_usuario(self, ra: int):
        for usuarioCadastrado in self.listaUsuarios:
            if usuarioCadastrado.ra == ra:
                print(f"\nLivros emprestados por {usuarioCadastrado.nome}:")
                usuarioCadastrado.listar_livros()
                return
        print(f"Usuário não cadastrado")
        
aBiblioteca = Biblioteca([], [])

while True:
    print(f"\nLista de funções: ")
    
    print(f"1. Cadastrar livro")
    print(f"2. Cadastrar usuário")
    print(f"3. Realizar empréstimo")
    print(f"4. Realizar devolução")
    print(f"5. Listar livros disponíveis")
    print(f"6. Listar livros emprestados ao usuário")
    print(f"7. Finalizar")
    
    opcao = input(f"Digite o número da funcao desejada: ")
    
    if opcao == "1": # Cadastrar Livro
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        novo_livro = Livro(titulo, autor)
        aBiblioteca.cadastrar_livro(novo_livro)

    elif opcao == "2": # Cadastrar usuário
        ra = int(input("RA do usuário: "))
        nome = input("Nome do usuário: ")
        novo_usuario = Usuario(ra, nome, [])
        aBiblioteca.cadastrar_usuario(novo_usuario)

    elif opcao == "3": # Realizar empréstimo
        ra = int(input("RA do usuário: "))
        titulo = input("Título do livro: ")
        aBiblioteca.realizar_emprestimo(ra, titulo)

    elif opcao == "4": # Realizar devolução
        ra = int(input("RA do usuário: "))
        titulo = input("Título do livro: ")
        aBiblioteca.realizar_devolucao(ra, titulo)

    elif opcao == "5": # Listar livros disponíveis
        aBiblioteca.listar_livros_disponiveis()

    elif opcao == "6": # Listar livros emprestador por usuário
        ra = int(input("Informe o RA para consulta: "))
        aBiblioteca.listar_livros_emprestados_usuario(ra)

    elif opcao == "7": 
        print("Sistema Encerrado")
        break
    else:
        print("Opção inválida, digite outro número")
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(livros, ano):
        return [livro for livro in livros if livro.ano_publicacao == ano and livro.disponivel]

# Criando duas instâncias da classe Livro e imprimindo as instâncias
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)

print(livro1)
print(livro2)

# Emprestando um livro e verificando sua disponibilidade
livro1.emprestar()
print(f"O livro '{livro1.titulo}' está disponível? {'Sim' if livro1.disponivel else 'Não'}")

# Verificando disponibilidade de livros por ano
livros = [livro1, livro2]
ano = 1949
livros_disponiveis = Livro.verificar_disponibilidade(livros, ano)
print(f"Livros disponíveis publicados em {ano}: {[livro.titulo for livro in livros_disponiveis]}")

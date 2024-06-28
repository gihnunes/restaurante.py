# biblioteca.py
from livro import Livro

# Criando uma instância da classe Livro e emprestando
livro = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro.emprestar()
print(f"O livro '{livro.titulo}' está disponível? {'Sim' if livro.disponivel else 'Não'}")

# Utilizando o método estático verificar_disponibilidade
livros = [livro, Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)]
ano = 1997
livros_disponiveis = Livro.verificar_disponibilidade(livros, ano)
print(f"Livros disponíveis publicados em {ano}: {[livro.titulo for livro in livros_disponiveis]}")

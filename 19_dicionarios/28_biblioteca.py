# %%
livros = {
    "Dom Casmurro": "Machado de Assis",
    "O Hobbit": "J. R. R. Tolkien",
    "1984": "George Orwell",
    "A Hora da Estrela": "Clarice Lispector"
}
soma = 0
titulos = []

cadastrar = input("Digite o título:")

if cadastrar in livros:
    print("O livro já foi cadastrado.")
else: 
    autor = input("Digite o autor:")
    livros[cadastrar] = autor

pesquisar_titulo = input("Digite um livro para pesquisar:")

if pesquisar_titulo in livros:
    print("Seu livro está no dicionário.",livros[pesquisar_titulo])
else:
    print("Seu livro não está no dicionário.")

soma = len(livros)

autor = input("Digite o autor:")

for chave, valor in livros.items():
    if autor == valor:
        print("Seu autor está no dicionário.",chave,valor)
        break
else:
    print("Não está no dicionário.")

    titulos.append(chave)

print(f"""
Livros: {livros}
Qtd livros: {soma}
Títulos: {titulos}
""")
# %%

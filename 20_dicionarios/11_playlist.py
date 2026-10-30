# %%

playlist = {    
    "The Summoning": "Sleep Token",    
    "Just Pretend": "Bad Omens",    
    "Do I Wanna Know?": "Arctic Monkeys",    
    "Rain": "Sleep Token",    
    "Like a Villain": "Bad Omens"
}
pesquisa_artistas = []
total_musicas = 0
qtd_por_artistas = {}

cadastrar = input("Deseja cadastrar uma musica:")

if cadastrar == "sim":
    nome_musica = input("Digite o nome da musica:")
    if nome_musica not in playlist:
        artistas = input("Digite o artista:")
        playlist[nome_musica] = artistas
    else:
     print("A musica já está na playlist.")
else:
     print("Sem novas musicas.")

nome_artista = input("Digite o nome do artista:")
for chave, valor in playlist.items():
    if valor == nome_artista:
        pesquisa_artistas.append(chave)

if pesquisa_artistas == []:
    print("não encontrado.")

for chave_soma, valor_soma in playlist.items():
    if valor_soma not in qtd_por_artistas:
            qtd_por_artistas[valor_soma] = 1
    else:
            qtd_por_artistas[valor_soma] += 1

total_musicas = len(playlist)

print(f"""
Playlist completa: {playlist}
Total musica: {total_musicas}
Qtd de musicas por artistas: {qtd_por_artistas}
Resultado pesquisa: {pesquisa_artistas}
""")
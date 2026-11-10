# %%

personagens = {
    "Arin": {"nivel": 5, "forca": 20, "magia": 10},
    "Mira": {"nivel": 7, "forca": 12, "magia": 30},
    "Toren": {"nivel": 4, "forca": 25, "magia": 5},
    "Luna": {"nivel": 7, "forca": 15, "magia": 25}
}
chave_maior = 0
maior = 0
maior_magia = 0
media = 0
soma = 0
maior_igual_6 = []
loop_forca = 0
loop_nivel = 0
loop_magia = 0
chave_maior_magia = 0
maior_nivel = 0
chave_maior_nivel = 0
empate = []

print(personagens)

pesquisa_personagem = input("Digite o nome do personagem:")

if pesquisa_personagem in personagens:
    print("Seu personagem é:" , personagens[pesquisa_personagem])
else:
    print("Seu personagem não existe.")


for chave, valor in personagens.items():
    if loop_forca == 0:
        maior = valor["forca"]
        chave_maior = chave
    else:
        if valor["forca"] > maior:
            maior = valor["forca"]
            chave_maior = chave
    loop_forca += 1

for chave_magica, valor_magica in personagens.items():
    if loop_magia == 0:
        maior_magia = valor_magica["magia"]
        chave_maior_magia = chave_magica
    else:
        if valor_magica["magia"] > maior_magia:
            maior_magia = valor_magica["magia"]
            chave_maior_magia = chave_magica
    loop_magia += 1

for chave_nivel, valor_nivel in personagens.items():
    if loop_nivel == 0:
        maior_nivel = valor_nivel["nivel"]
        chave_maior_nivel = chave_nivel
    else:
        if valor_nivel["nivel"] > maior_nivel:
            maior_nivel = valor_nivel["nivel"]
            chave_maior_nivel = chave_nivel

    loop_nivel += 1


    soma = soma + valor_nivel["nivel"]

media = soma / len(personagens)

for chave_empate, valor_empate in personagens.items():
    if valor_empate["nivel"] == maior_nivel:
        empate.append(chave_empate)

    if valor_empate["nivel"] >= 6:
        maior_igual_6.append(chave_empate)

if len(empate) >= 2:
    print("Houve empate.",empate)
else:
    print("sem empate.", chave_maior_nivel, maior_nivel)



print(f"""
Maior força: {chave_maior} {maior}
Maior magia: {chave_maior_magia} {maior_magia}
Média nível: {media}
Nível maior igual á 6: {maior_igual_6}
""")


# %%

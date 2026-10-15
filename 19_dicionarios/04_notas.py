# %%
soma = 0
media = 0
boletim_nome = {
    "nome": "Carlos"
}

boletim = {
    "Artes": 10,
    "Biolagia": 7,
    "Matematica": 9
}

for chave, valor in boletim.items():
    soma += valor

media = soma / 3

print(boletim_nome, boletim)
print(media)
# %%
jogadores = {
    "Ana": 850,
    "Carlos": 1200,
    "Pedro": 950,
    "Mariana": 1500,
    "Lucas": 700
}

maior = max(jogadores, key=lambda chave: jogadores[chave])

print("O jogador com maior pontuação foi: ",maior, jogadores[maior])




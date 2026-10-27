# %%
tarefas = {
    "Estudar Python": "concluída",
    "Fazer exercícios": "pendente",
    "Organizar arquivos": "concluída",
    "Estudar dicionários": "pendente",
    "Revisar código": "pendente"
}
qtd_concluida = 0
qtd_pendente = 0
qtd_pendente_lista =  []
porcentagem = 0
total = 0

for chave, valor in tarefas.items():
    if valor == "concluída":
        qtd_concluida += 1
    else:
        qtd_pendente += 1
        qtd_pendente_lista.append(chave)

if qtd_concluida > qtd_pendente:
    print("as tarefas concluidas são maiores.")
elif qtd_concluida < qtd_pendente:
    print("as tarefas pendentes são maiores.")
else:
    print("a quantidade de pendentes e concluidas são as mesmas.")

total = qtd_concluida / len(tarefas)
porcentagem = total * 100

print(f"""
Concluidas: {qtd_concluida}
Pendentes: {qtd_pendente}
Lista pendentes: {qtd_pendente_lista}
Porcentagem concluidas: {porcentagem}%

""")


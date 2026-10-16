# %%
candidatos = {
    "can_a": 0,
    "can_b": 0,
    "can_c": 0
}
loop = 0
maior = 0
invalidos = 0
chave_maior = 0
empate = ""
qtd_maiores =0

while True:
    opcao = input("Digite seu voto ou fim para encerrar:")

    if opcao == "fim":
        print("Votação encerrada.")
        break
    else:
        if opcao in candidatos:
            candidatos[opcao] += 1
        else:
            print("Candidato invalido.")
            invalidos += 1

for chave, valor in candidatos.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    loop += 1

for nome, votos in candidatos.items():
    if votos == maior:
        qtd_maiores += 1

if maior == 0:
    empate = "sem votos"
elif qtd_maiores == 1:
    empate = "não"
    print("O vencedor foi:", chave_maior)
elif qtd_maiores > 1:
    empate = "sim"



print(candidatos)
print(invalidos)
print("Empate:", empate)


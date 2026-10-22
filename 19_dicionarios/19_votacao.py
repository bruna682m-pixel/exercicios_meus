# %%

votos = {
    "Pizza": 0,
    "Hambúrguer": 0,
    "Sushi": 0
}

invalidos = 0
loop = 0
maior = 0
empate = 0
chave_maior = 0
maior_0 = 0

while True:
    opcao = input("Digite um voto ou fim para encerrar:")

    if opcao == "fim":
        print("Saindo...")
        break
    elif opcao not in votos:
        print("Opção invalida.")
        invalidos += 1
    else:
        votos[opcao] += 1

for chave, valor in votos.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave
    loop += 1

for chave_empate, valor_empate in votos.items():
    if maior == valor_empate:
        empate += 1

if maior == 0:
    print("Sem votos validos.")
else:
    print((f"""Votos: {votos}
Vencedor: {chave_maior} {maior}
Empate: {empate} 
Invalidos: {invalidos}"""   ))

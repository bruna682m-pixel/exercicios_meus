# %%

notas = {}
loop = 0
maior = 0
aprovado = 0
maior_nome = 0

while True:
    opcao = input("Digite fim para encerrar ou seu nome.")
    if opcao == "fim":
        print("Saindo...")
        break
    else:
        notas[opcao] = int(input("Digite sua nota:"))

for chave, valor in notas.items():
    if loop == 0:
        maior = valor
        maior_nome = chave
    else:
        if valor > maior:
            maior = valor
            maior_nome =  chave

    if valor >= 7:
        aprovado += 1

    loop += 1

print(aprovado)
print(maior_nome, maior)

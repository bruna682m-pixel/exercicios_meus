# %%
quantidade = 0 # definindo variavel 

while True: # loop infinito ate o break
    idade = int(input("Digite a idade ou -1 para sair: ")) # pedindo a idade ou -1 para sair

    if idade == -1: # se idade for -1 sai do programa com break
        break
    elif idade < -1:
        print("Idade não pode ser negativa.")
    else:
        quantidade = quantidade + 1 # aumulando somando q quantidade de pessoas

print("Pessoas cadastradas:", quantidade) # mostrando a qtd de pessoas cadastradas

# problema está aceitando e contando idades negativas
# ao digitar 20,30, -5 aqui -5 não deve ser contabilizado e contar as pessoas validas
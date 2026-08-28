
# Mostrar a série de FETUCCINE até o termo informado pelo usuário ( o termo da série deve ser maior que 3)  , e calcular a
 # 	somatória dos termos e mostrar. 
 #       	🡪A série de FETUCCINE é:  os dois primeiros termos da série são informados pelo usuário, a 
 #   partir daí , os termos são  gerados com a soma ou subtração dos dois termos anteriores, ou seja:
#- se o termo for ímpar soma-se os anteriores para se obter o próximo,
#- se o termo for par subtrai-se os anteriores para se obter o próximo.
# %%

f1 = int(input("Digite o primeiro termo:"))
f2 = int(input("Digite o segundo termo:"))
numero = int(input("Digite a posição do termo:"))
soma = 0
subtracao = 0

print(f1)
print(f2)

if numero > 3:
    for i in range(1, numero-1):
        if i % 2 == 0 :
            subtracao = f1 - f2

            print(subtracao)

            f1 = f2
            f2 = subtracao

        else:
            soma = f1 + f2

            print(soma)

            f1 = f2
            f2 = soma
else:
    print("A poisção deve ser maior que 3.")

# %%

f1 = int(input("Digite o primeiro termo:"))
f2 = int(input("Digite o segundo termo:"))
numero = int(input("Digite a posição do termo:"))
soma = 0
subtracao = 0
soma_2_primeiros = f1 + f2
soma_termos = 0

print(f1)
print(f2)

if numero > 3:
    for i in range(1, numero-1):
        if i % 2 == 0 :
            subtracao = f1 - f2

            print(subtracao)

            f1 = f2
            f2 = subtracao

            soma_termos = soma_termos + subtracao

        else:
            soma = f1 + f2

            print(soma)

            f1 = f2
            f2 = soma

            soma_termos = soma_termos + soma

    soma_termos = soma_termos + soma_2_primeiros
    print("soma termos", soma_termos)
else:
    print("A posição da serie deve ser maior que 3.")


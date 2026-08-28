
# Mostrar a série de RICCI até o termo informado pelo usuário ( o termo da série deve ser maior que 3 ), e calcular a somatória
#  dos termos e mostrar.
 # 🡪série RICCI: os dois primeiros termos serão informados pelo usuário e o próximo termo é a soma dos dois anteriores 

# %%
soma = 0

r1 = int(input("Digite o primeiro número da sequência:"))
r2 = int(input("Digite o segundo número da sequência:"))
numero = int(input("posição da serie:"))

print(r1)
print(r2)
             
for i in range(1, numero-1):
    soma = r1 + r2

    print(soma)

    r1 = r2
    r2 = soma

# %%
soma = 0
soma_termos = 0
soma_2_primeiros = 0

r1 = int(input("Digite o primeiro número da sequência:"))
r2 = int(input("Digite o segundo número da sequência:"))
numero = int(input("posição da serie:"))

soma_2_primeiros = r1 + r2
print(r1)
print(r2)

if numero > 3:     
    for i in range(1, numero-1):
        soma = r1 + r2

        print(soma)

        r1 = r2
        r2 = soma

        soma_termos = soma_termos + soma

    soma_termos = soma_termos + soma_2_primeiros
    print("A soma dos",numero,"termos é:", soma_termos)

else:
    print("A posição da serie deve ser maior que 3.")





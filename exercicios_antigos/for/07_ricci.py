
# Mostrar a série de RICCI até o termo informado pelo usuário ( o termo da série deve ser maior que 3 ), e calcular a somatória
#  dos termos e mostrar.
 # 🡪série RICCI: os dois primeiros termos serão informados pelo usuário e o próximo termo é a soma dos dois anteriores 

# %%
soma = 0

r1 = int(input("Digite o primeiro número da sequência:"))
r2 = int(input("Digite o segundo número da sequência:"))
numero = int(input("posição da serie:"))

             
for i in range(1, numero):
    soma = r1 + r2

    print(soma)

    r1 = r2
    r2 = soma




# %%

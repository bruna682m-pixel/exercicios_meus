# %%
# resolver
# Solicitar 3 valores inteiros para o cálculo da equação de segundo grau,

delta = 0
b_sinal = 0
raiz = 0
divisao = 0
x1 = 0
x2 = 0

a = input("Digite o número A da equação:")
b = input("Digite o número B da equação:")
c = input("Digite o número C da equação:")

a = float(a)
b = float(b)
c = float(c)

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não tem raízes reais. Delta =", delta)
elif delta == 0:
    print("Existe 1 raíz real")

elif delta > 0:
    raiz = delta ** (1/2)

    b_sinal = - b 

    divisao = 2 * a

    x1 = b_sinal - raiz 
    x1 = x1 / divisao

    x2 = b_sinal + raiz
    x2 = x2 / divisao
    print("Sua equação de grau 2 deu. x1:", x1,"e x2:",x2)

#print(x1)
#print(x)
#print(raiz)
#print(delta)


# %%

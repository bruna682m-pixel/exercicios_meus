# %%
operacao = input("""
Escolha qual conta quer fazer:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potencia
6 - Raiz

""")

numero1 = input("Digita o número para fazer a conta")
numero2 = input("Digita o outro número para fazer a conta")

resultado = 0
resultado = float(resultado)
numero1 = float(numero1)
numero2 = float(numero2)

if operacao == "1":
    resultado = numero1 + numero2
elif operacao == "2":
    resultado = numero1 - numero2
elif operacao == "3":
    resultado = numero1 * numero2
elif operacao == "4":
    if numero2 == 0:
     print("Divisao por 0 não existe")
    else:
     resultado = numero1 / numero2
elif operacao == "5":
    resultado = numero1 ** numero2
elif operacao == "6":
    resultado = numero1 ** (1/2)
else:
    print("digite uma opção de operação.")

print("Os números escolhidos foram", numero1, "e número", numero2, "Seu resultado foi", resultado)

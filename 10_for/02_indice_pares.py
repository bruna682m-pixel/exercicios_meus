# %%

palavra = input("Digite uma palavra:")

for i in range(0, len(palavra), 2):
    print(f"índice {i}: caractere {palavra[i]}")
# %%
numeros = [10, 20, 30, 40, 50]
vazia = False

terceiro = numeros[2]

if numeros == []:
    vazia = True
    vazia = "sim"
else:
    vazia = False
    vazia = "não"

esta_vazia = len(numeros) == 0
print(f"a lista está vazia? {esta_vazia}")

print("Terceiro elemento:", terceiro)
print("Comprimento da lista:", len(numeros))
print("A lista está vazia?",vazia)
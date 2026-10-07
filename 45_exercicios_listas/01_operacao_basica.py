# %%
numeros = [10, 20, 30, 40, 50]
vazia = False
indice = len(numeros)

if numeros == [] or indice < 3:
    print("Lista vazia ou menor que 3 elementos")
else:
    terceiro = numeros[2]
    if numeros == []:
        vazia = True
    else:
        vazia = False

    esta_vazia = len(numeros) == 0
    print(f"a lista está vazia? {esta_vazia}")

    print("Terceiro elemento:", terceiro)
    print("Comprimento da lista:", len(numeros))
  
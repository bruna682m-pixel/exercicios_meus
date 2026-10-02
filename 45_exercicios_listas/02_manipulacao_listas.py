# %%

lista_inicial = [100, 50, 400, 500]
lista_inicial_alterada = [100, 50, 400, 500]
lista_inicial_alterada_remover_indice = []


lista_inicial[1] = 200
print(f"Alteração: {lista_inicial}")

lista_inicial.append(600)
print(f"Anexo: {lista_inicial}")


lista_inicial.insert(2, 300)
print(f"Inserção: {lista_inicial}")

lista_inicial.remove(600)
print(f"Remoção do 600: {lista_inicial}")


lista_inicial.pop(0)
print(f"Remoção do índice 0: {lista_inicial}")




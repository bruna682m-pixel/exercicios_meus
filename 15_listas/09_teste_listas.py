# %%
produtos = ["arroz", "feijao", "macarrao"]

nomes = ["ana", "bianca", "carlos", "daniel", "eduardo"] # começa em 0 até o último elemento no caso 4
# 0 = ana, 1= bianca , 2= carlos, 3= daniel e 4= eduardo

# %%
nomes[0] # ana

# %%
nomes[3] # daniel

# %%
nomes[-1] # último elemento

# %%
nomes[-2] # penúltimo elemento

# %%
# acessar elemento
produtos = ["arroz", "feijao", "macarrao"]

print(produtos[1]) # pegando feijão elemento do índice 1

# %%
produtos[1] = "carne"
print(produtos) # alterando elemento do índice 1 feijao para carne

# %%
produtos.append("cafe") # add novo elemento no fim da lista
print(produtos)

# %%
produtos.pop(1) # removendo elemento do índice 1
produtos.pop() # remover último elemento
print(produtos)

# %%
print(len(produtos)) # saber quantos elementos tem na lista não tem haver com índice

# ver se lista está vazia
if produtos == []:
    print("Lista vazia.")

# %%
# for percorrendo lista
for produto in produtos:
    print(produto)

# for valor in lista: se preciso apenas dos valore não usar enumerate
#    print(valor)

# %%
# enumerate para pegar valor e índice
nomes = ["ana", "bianca", "carlos"]

for i, nome in enumerate(nomes):
    print(i, nome)

# %%
lista.pop(indice) # remover elemento especifico
lista[indice] = novo_valor # alterar elemento especifico com novo valor

# %%
# for para analisar vários elementos
notas = [7, 8, 5, 9]

for nota in notas:
    if nota >= 6:
        aprovados += 1

# %%
# while + lista para receber vários valores
nomes = []

while True:
    nome = input("Digite um nome:")

    if nome == "":
        break

    nomes.append(nome)

# %%
# conversão para int no input
valor = input("Digite:")

if valor == "":
    break

valor = int(valor)

# %%
# slicing
frutas = ["maca", "banana", "laranja", "uva", "manga"]
frutas[0:3] # pegando elemento do índice 0 até 2 

# %%
# começo omitido
frutas[:3] # comece do início e pare antes do índice 3.

 # %%
 # fim omitido
frutas[3:] #comece no índice 3 e vá até o final.

# %%
frutas[:] # lista toda

# %%
frutas[::2] #de 2 em 2

# %%
frutas[::-1] # de trá para frente

# %%
frutas[-1] # pega o elemento

# %%
frutas[-1:] # retorna lista é uma fatia slicing

# %%
frutas.append("novo") # adiciona do fim
print(frutas)

# %%
frutas[2] = "novo" # altera elemento 2
print(frutas)

# %%
# procurando elemento na lista
numeros = [10, 25, 7, 42, 18]

for numero in numeros:
    if numero == procurado:
        print("Encontrei")

# saber índice
for i, numero in enumerate(numeros):
    if numero == procurado:
        print("Posição:", i)

# saber se encontrou
if numero == procurado:
    encontrou = True

# substituir valore
for i, numero in enumerate(numeros):
    if numero == 5:
        numeros[i] = 10

# %%
len(notas)=  quantidade
max(notas)= maior
min(notas)= menor
sum(notas)= soma
sum(notas) / len(notas)= média
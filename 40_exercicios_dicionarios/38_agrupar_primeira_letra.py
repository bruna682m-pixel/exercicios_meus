# %%
words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]

palavras = {}


for i in words:
    letra = i[0]
    palavras.setdefault(letra, []).append(i)

print(palavras)
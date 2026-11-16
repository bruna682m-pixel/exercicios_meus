# %%
palavras_dict = {}

text = "the cat sat on the mat the cat"

for palavra in text.lower().split():
    if palavra not in palavras_dict:
        palavras_dict[palavra] = 1
    else:
        palavras_dict[palavra] += 1

print(palavras_dict)

# %%
palavras_dict = {}
palavra_atual = ""

text = "the cat sat on the mat the cat"

for i in text:
    if i != "":
        palavra_atual += i

    if i == "":
        palavras_dict[palavra_atual]

palavras_dict[palavra_atual]

print(palavras_dict)
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
    if i != " ":
       palavra_atual += i

    if i == " ":
        if palavra_atual not in palavras_dict:
            palavras_dict[palavra_atual] = 1
        else:
            palavras_dict[palavra_atual] += 1
        
        palavra_atual = ""

if palavra_atual != "":
    if palavra_atual not in palavras_dict:
            palavras_dict[palavra_atual] = 1
    else:
        palavras_dict[palavra_atual] += 1


print(palavras_dict)
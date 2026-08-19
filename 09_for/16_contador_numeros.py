# %%

texto = input("Digite um texto:")

for i in texto:
    if i.isdigit(): # ver se tem caractere em número
        print("Encontrei esse número no meio do seu texto:",i)
    else:
        print("Encontrei esses dígitos no seu texto:",i)
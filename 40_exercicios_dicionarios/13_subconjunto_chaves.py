# %%
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}

novo_dict = {
    chave: valor
    for chave, valor in user.items()
    if chave == "id" or chave == "username" or chave == "email"
}


print(novo_dict)

# %%
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
keys_to_keep = ["id", "username", "email"]

subset = {k: user[k] for k in keys_to_keep}
print(subset)
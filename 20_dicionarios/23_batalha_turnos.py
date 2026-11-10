# %%
inimigos = {
    "goblin": {"vida": 50, "ataque": 10},
    "orc": {"vida": 100, "ataque": 20},
    "dragao": {"vida": 200, "ataque": 40}
}
derrotados = 0

print(inimigos)

while True:
    opcao = input("Deseja atacar o inimigo?")

    if opcao == "nao":
        print("Saindo....")
        break

    escolha = input("Escolha um inimigo:")
    dano = int(input("Digite quanto de dano você causou no inimigo:"))

    if escolha in inimigos:
        if dano > 0:
            if inimigos[escolha]["vida"] > 0:
                inimigos[escolha]["vida"] -= dano
                print(f"O inimigo ficou com", inimigos[escolha]["vida"])

                if inimigos[escolha]["vida"] <= 0:
                    print("O inimigo foi derrotado.")
                    inimigos[escolha]["vida"] = 0
                    derrotados +=1

                if inimigos[escolha]["vida"] > 0:
                    print("O inimigo está vivo.")
        else:
            print("Dano invalido.")

    else:
        print("O inimigo não existe.")


print("Inimigos derrotados:",derrotados)


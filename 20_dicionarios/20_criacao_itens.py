
 # %%
materiais = {    
    "madeira": 6,    
    "ferro": 4,    
    "cristal": 2,    
    "ervas": 5
}
receitas = {    
    "espada": {"madeira": 1, "ferro": 2},    
    "pocao": {"ervas": 3, "cristal": 1},    
    "cajado": {"madeira": 2, "cristal": 2}
}

faltando = []
receitas_escolhida = {}
fabricados = {}

while True:
    print(f"""
Receitas: {receitas}
Materiais: {materiais}
""")

    objeto_criar = input("Escolha um objeto para criar ou sair para encerrar:")

    faltando = []

    if objeto_criar == "sair":
        print("Saindo...")
        break

    if objeto_criar in receitas:
        receitas_escolhida = receitas[objeto_criar]
        print(receitas)
    else:
        print("Receita não encontrada.")

    for chave_escolhida, valor_escolhido in receitas_escolhida.items():
        for chave, valor in materiais.items():
            if chave_escolhida == chave:
                if valor >= valor_escolhido:
                    print("tem material")
                else:
                    print("sem material")
                    faltando.append(chave_escolhida)

    if faltando == []:
        for chave, valor in receitas_escolhida.items():
            materiais[chave] -= valor

        print("Item criado com sucesso.")
        if objeto_criar not in fabricados:
            fabricados[objeto_criar] = 1
        else:
            fabricados[objeto_criar] += 1
    else:
        print("Sem material suficiente. Está faltando:",faltando)
            
print(f"""
Faltando: {faltando}
Fabricados: {fabricados}
""")
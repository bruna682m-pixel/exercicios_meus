# %%
suspeitos = {    
    "Carlos": "impressao digital",    
    "Marina": "testemunha",    
    "Pedro": "impressao digital",    
    "Julia": "camera",    
    "Rafael": "testemunha"
}
suspeitos_lista = []
sus_impressao_digital = []
frequencia = {}
pesquisa_tipo_evidencia = []

tipo_evidencia = input("Digite a evidência para encontrar suspeitos:")

for chave, valor in suspeitos.items():
    suspeitos_lista.append(chave)

    if valor == "impressao digital":
        sus_impressao_digital.append(chave)

    if valor not in frequencia:
        frequencia[valor] = 1
    else:
        frequencia[valor] += 1

    if tipo_evidencia == valor:
        pesquisa_tipo_evidencia.append(chave)

if pesquisa_tipo_evidencia == []:
    print("Nenhum suspeito encontrado.")



print(f"""
Lista de susteitos: {suspeitos_lista}
Suspeitos por impressão digital: {sus_impressao_digital}
Suspeitos de cada evidência: {frequencia}
Pesquisa por evidencia: {pesquisa_tipo_evidencia}
""")
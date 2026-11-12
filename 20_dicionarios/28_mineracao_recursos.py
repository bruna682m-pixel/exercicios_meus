# %%
mina = {    
    "madeira": {"quantidade": 10, "valor": 5},    
    "ferro": {"quantidade": 8, "valor": 15},    
    "ouro": {"quantidade": 3, "valor": 50},    
    "cristal": {"quantidade": 5, "valor": 30}
}
registro_coleta = {}
registro_uso = {}
total_recursos = 0
valor_total = 0

print(mina)

opcao = int(input("Digite a opção:"))

coleta = input("Qual material você coletou:")
qtd_coleta = int(input("Digite a quantidade de material que você coletou:"))

if qtd_coleta <= 0:
    print("A quantidade precisa ser maior que 0.")

if coleta not in mina:
    mina[coleta]["quantidade"] = qtd_coleta
else:
    mina[coleta]["quantidade"] += qtd_coleta

uso = input("Qual material você quer usar:")

consulta_nome = input("Digite o nome do material para consultar:")

if consulta_nome in mina:
    print("Dados do material que você pesquisou:",mina[consulta_nome])
else:
    print("Você não coletou este item.")

if uso in mina:
    qtd_uso = int(input("Digite a quantidade de material para usar:"))

    if qtd_uso <= 0:
        print("A quantidade precisa ser maior que 0.")
    else:
        if qtd_uso <= mina[uso]["quantidade"]:
            mina[uso]["quantidade"] -= qtd_uso
            registro_uso[uso] = qtd_uso

for chave, valor in mina.items():
    total_recursos = total_recursos + valor["quantidade"]

    valor_total = valor_total + valor["valor"]

print(f"""
Mina: {mina}
Total recursos: {total_recursos}
Total valor: {valor_total}
""")
loja_a = { "Mouse": 10,    "Teclado": 5,    "Monitor": 8,    "Fone": 12}
loja_b = {    "Mouse": 7,    "Teclado": 10,    "Webcam": 15,    "Fone": 3}
soma_produtos = {}
soma_a = 0
soma_b = 0

copia_loja_a = loja_a.copy()

for chave, valor in loja_a.items():
  soma_a = soma_a + valor

for chave_b, valor_b in loja_b.items():
  soma_b = soma_b + valor_b

  copia_loja_a[chave_b] = copia_loja_a.get(chave_b, 0) + valor_b

soma_produtos["loja_a"] = soma_a
soma_produtos["loja_b"] = soma_b

comun = set(loja_a) & set(loja_b)

diferenca = set(loja_a) - set(loja_b)

maior_loja_a = max(loja_a, key=lambda chave: loja_a[chave])

maior_loja_b = max(loja_b, key=lambda chave_b: loja_b[chave_b])

maior_somando_lojas = max(copia_loja_a, key=lambda chave_soma: copia_loja_a[chave_soma] )

ordenar_vendas = dict(sorted(copia_loja_a.items(), key=lambda item: item[1], reverse=True))


print(f"""
Soma dos produtos: {soma_produtos}
Elementos em comun: {comun}
Elementos execlusivos da loja_a: {diferenca}
Maior venda loja_a: {maior_loja_a}
Maior venda loja_b: {maior_loja_b}
Maior venda dos produtos somando as 2 lojas: {maior_somando_lojas}
Soma por produto: {copia_loja_a}
Soma por produto ordenado: {ordenar_vendas}
""")
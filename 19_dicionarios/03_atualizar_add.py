# %%

dados = {
    "nome": "Ana",
    "idade": 18
         
         }

dados["profissao"] = input("Digite sua profissão:")

opcao = (input("Quer alterar idade:"))

if opcao == "sim":
    dados["idade"] = int(input("Digite a idade atualizada:"))
elif opcao == "não":
    print("Mantendo igual.")
else:
    print("opção invalida.")

print(dados)

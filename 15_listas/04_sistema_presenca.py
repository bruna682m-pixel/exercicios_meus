# %%

alunos = []
presentes_lista = []
ausentes_lista = []
presentes = 0
ausentes = 0

while True:
    aluno = input("Digite seu nome:")

    if aluno == "":
        print("Saindo...")
        break
    else:
        alunos.append(aluno)


    opcao = int(input(f"{aluno} está presente? 1- sim e 2- não"))

    if opcao == 1:
        presentes += 1
        presentes_lista.append(aluno)
    elif opcao == 2:
        ausentes += 1
        ausentes_lista.append(aluno)
    else:
        print("Opção invalida.")

print("Total de alunos:", len(alunos))
print("Presentes:",presentes)
print("Ausentes:",ausentes)

print("Lista ausentes:", ausentes_lista)
print("Lista presentes:", presentes_lista)



# %%

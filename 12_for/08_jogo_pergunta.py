# %%
pontos = 0

for i in range(1, 6):
    if i == 1:
        pergunta_1 = int(input("""
Qual é o comportamento padrão da função print() em Python ao final da impressão de um texto?
1) Dar um espaço em branco.
2) Pular para a próxima linha (\n).
3) Apagar a linha anterior.
4) Encerrar o programa.
"""))
        if pergunta_1 == 2:
            pontos = pontos + 10

    elif i == 2:
        pergunta_2 = int(input("""
Para que serve o argumento end="" dentro da função print()?
1) Para pular duas linhas de uma vez.
2) Para transformar o texto em letras maiúsculas.
3) Para evitar que o print pule uma linha ao final da impressão.
4) Para indicar o fim do programa Python.
"""))
        if pergunta_2 == 3:
            pontos = pontos + 20
        
    elif i == 3:
         pergunta_3 = int(input("""
Em que ano foi assinado o Tratado de Tordesilhas, que dividia as terras recém-descobertas entre Portugal e Espanha?
1- 1500
2- 1453
3- 1494
4- 1534
"""))
         if pergunta_3 == 3:
            pontos = pontos + 30
         
    elif i == 4:
        pergunta_4 = int(input("""
Qual é o maior país do mundo em extensão territorial que não possui saída para o mar (país sem litoral)?
1- Mongólia
2- Bolívia
3- Chade
4- Cazaquistão
"""))
        if pergunta_4 == 4:
            pontos = pontos + 20

    elif i == 5:
        pergunta_5 = int(input("""
Qual é o elemento químico mais abundante no universo em termos de massa e de número de átomos?
1- Oxigênio
2- Carbono
3- Hidrogênio
4- Hèlio
"""))
        
        if pergunta_5 == 3:
            pontos = pontos + 20

print("Pontuação:",pontos)

if pontos <= 40:
    print("Ruim")
elif pontos <= 70:
    print("Regular")
elif pontos <= 90:
    print("Bom")
elif pontos <= 100:
    print("Pro")

    

# %%

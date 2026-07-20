# %%
texto = """ 
Me diga a altura e largura de sua parede:

Me diga a cor da sua parede:
(1) Azul
(2) Branco
(3) Cinza

Me diga o acabamento de sua parede:
(1) Fosco
(2) Brilhante
"""
print(texto)

altura = input("Diga a altura de sua parede:")
largura = input("Diga a largura de sua parede:")
cor = input("Me diga a cor de sua parede:")
acabamento = input("Me diga o acabamento de sua parede: ")

altura = float(altura)
largura = float(largura)

area = altura * largura

if cor == "1":
  cor = "Azul"
elif cor == "2":
  cor = "Branco"
elif cor == "3":
  cor = "Cinza"
else:
  print("Escolha uma cor para sua parede:")

if acabamento == "1":
  acabamento = "Fosco"
elif acabamento == "2":
  acabamento = "brilhante"
else:
  print("Digite o acabamento de sua parede:")

print("A area de sua parede deu: ",area,"A cor escolhida foi: ",cor, "E o acabamento escolhido foi: ",acabamento)
 
 
 
 

 
  
  
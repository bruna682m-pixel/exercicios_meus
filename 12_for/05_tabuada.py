numero_max = 10
multiplicador = 10
resultado = 0

for tabuada in range(1, numero_max+1):
  print("Tabuada",tabuada)
  for i in range(1, multiplicador+1):
    resultado = tabuada * i
    print(tabuada,"×",i,"=",resultado)
    
    


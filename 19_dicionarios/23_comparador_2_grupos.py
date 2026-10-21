# %%
grupo_a = ["Ana", "Bruno", "Caio", "Duda"]
grupo_b = ["Bruno", "Duda", "Eva", "Felipe"]
ocorrencia = {}

for chave, valor in ocorrencia.items():
    if chave in ocorrencia:
        ocorrencia[chave] = 1
        for i in grupo_a:
            if i in grupo_b:
                ocorrencia[i] = 1
    
    

print(ocorrencia)
        
# %%
grupo_a = ["Ana", "Bruno", "Caio", "Duda"]
grupo_b = ["Bruno", "Duda", "Eva", "Felipe"]
ocorrencia = {}

for i in grupo_a:
    if i in grupo_b:
        ocorrencia[i] = 1
        for j in grupo_b:
            if j in grupo_a:
                ocorrencia[j] = 1
            else:
                ocorrencia[j] += 1
    else: 
        ocorrencia[i] += 1
    

print(ocorrencia)
        



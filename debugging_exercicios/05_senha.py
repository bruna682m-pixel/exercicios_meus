# %%
senha_correta = 1234 # senha certa
tentativas = 3 # tentativas

while tentativas > 0: # enquanto tentativas for maior que 0 pede a senha
    senha = int(input("Digite a senha: ")) # pedindo senha

    if senha == senha_correta: # se senha for 1234 mostra senha correta e sai com break e mostra as tentativas
        print("Senha correta.")
        break
    else:
        tentativas = tentativas - 1 # diminuindo a tentativa
        print("Senha incorreta.") # se senha não for 1234 mostra invalida mostra as tentativas no final
        print("Tentativas restantes:", tentativas) # mostrava as tentativas apenas no final




# o único problema é mostrar as tentativas mesmo tendo acertado
# mostrar as tentativas quando a pessoa erra só no fim não chega a ser um problema mas
# é só colocar no else onde mostra senha invalidade que só mostra tentativa quando errar
# da para colocar tentativas = tentativas - 1 dentro do else tambem qual seria a direrença?
# no final conta 3,2,1 faz mais sentido
#  no else conta 2,1,0
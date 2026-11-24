# %%
import copy

configuracoes = {    
    "usuario": "Ana",    
    "preferencias": {        "tema": "escuro",        "notificacoes": True    },    
    "atalhos": ["Ctrl+C", "Ctrl+V"]
}

copia_rasa = configuracoes.copy()
copia_rasa["preferencias"]["tema"] = "claro"
copia_rasa["atalhos"].append("Ctrl+A")

print(f"""
Original: {configuracoes}
Copia rasa: {copia_rasa}
""")

print()

configuracoes = {    
    "usuario": "Ana",    
    "preferencias": {        "tema": "escuro",        "notificacoes": True    },    
    "atalhos": ["Ctrl+C", "Ctrl+V"]
}

copia_profunda = copy.deepcopy(configuracoes)
copia_profunda["preferencias"]["tema"] = "claro"
copia_profunda["atalhos"].append("Ctrl+A")

print(f"""
Original: {configuracoes}
Copia rasa: {copia_profunda}
""")










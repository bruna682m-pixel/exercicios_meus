# %%

roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
existe_editor = False
existe_gerente = False

if "editor" in roles.values():
    existe_editor = True

if "gerente" in roles.values():
    existe_gerente = True
    
    
print("gerente existe como valor: ", existe_gerente)

print("editor existe como valor: ", existe_editor)

# %%
roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}

print("'editor' exists as a value:", "editor" in roles.values())
print("'manager' exists as a value:", "manager" in roles.values())
# %%
permissoes_admin = {"cadastrar", "editar", "excluir", "visualizar"}

permissoes_funcionario = {"visualizar", "editar"}

funcionario_admin = permissoes_funcionario <= permissoes_admin

admin_funcionario = permissoes_admin <= permissoes_funcionario

print("As permissões de funcionário estão contidas na do adminstrador:", funcionario_admin)
print("As permissões de adminstrador estão contidad na de funcionário: ", admin_funcionario)


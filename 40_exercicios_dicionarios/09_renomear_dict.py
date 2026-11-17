# %%

employee = {"fname": "John", "age": 30, "dept": "Engineering"}

chave_removida = employee.pop("fname")
employee["first_name"] = chave_removida

print(employee)

# %%
employee = {"fname": "John", "age": 30, "dept": "Engineering"}

employee["first_name"] = employee.pop("fname")

print(employee)
# %%
# minha
import json

person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}

dados_json = json.dumps(person)

print(dados_json)

# %%
# site
import json

person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}

json_string = json.dumps(person, indent=4)

print(json_string)
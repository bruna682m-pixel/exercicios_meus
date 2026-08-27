# %%
numero_max = 5

for i in range(1, numero_max+1):
    temperatura = int(input("Digite 5 temperaturas em Celsius:"))

    f = temperatura * 9 / 5 + 32

    print(temperatura,"°C = ",f,"°F") 
# %%
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
brand =  False
color =  False
car.pop("color")

car.items()

if "brand" in car:
    brand = True

if "color" in car:
    color = True


print(car)
print("Brand existe: ", brand)
print("Color existe: ", color)

# %%
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

car.pop("color")
print(car)

print(car.items())

print("brand existe:", "brand" in car)
print("color exxite: ", "color" in car)

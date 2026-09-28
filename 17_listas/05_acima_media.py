# %%

notas = [5, 8, 6, 10, 7, 4]
media = []
soma = 0
media_total = 0

media_total = sum(notas) / len(notas)

for i in notas:
    if i >= media_total:
        media.append(i)

print(media_total)
print(media)

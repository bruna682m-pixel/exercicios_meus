# %%
text = "hello world"
caracteres = {}

for i in text:
    if i not in caracteres:
        caracteres[i] = 1
    else:
        caracteres[i] += 1

print(caracteres)

# %%
text = "hello world"

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)

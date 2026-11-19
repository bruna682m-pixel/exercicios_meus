# %%
# site
# resolver depois
nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}

def flatten(d, prefix=""):
    result = {}
    for k, v in d.items():
        new_key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.update(flatten(v, new_key))
        else:
            result[new_key] = v
    return result

print(flatten(nested))
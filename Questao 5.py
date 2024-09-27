def inverter_string(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

string = "Guilherme Ferraz"
invertida = inverter_string(string)
print(f"String original: {string}")
print(f"String invertida: {invertida}")
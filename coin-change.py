# Problema do troco

# Calcula o mínimo de moedas possíveis para devolver o troco
def moedas(valor):
    valores = [100, 50, 25, 10, 5, 2, 1]

    retorna = []

    i = 0
    while valor != 0:
        if valores[i] > valor:
            i += 1
            continue

        retorna.append(valores[i])
        valor -= valores[i]

    print(retorna)

troco = 68
moedas(troco)
import heapq

def ordem_crescente(lista):
    heapq.heapify(lista)
    in_order = []
    tam = len(lista)

    for i in range(tam):
        in_order.append(heapq.heappop(lista))
    
    return in_order

def paradas(postos, autonomia):
    postos = ordem_crescente(postos)
    p = []

    for i in range(len(postos)):

        if postos[i] > autonomia:
            p.append(postos[i-1])
            autonomia += postos[i-1]

    print(p)

postos = [20, 1, 34, 23, 4, 21, 55, 77, 42]
autonomia = 20

paradas(postos, autonomia)
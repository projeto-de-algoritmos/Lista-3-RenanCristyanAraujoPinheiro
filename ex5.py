# Exercício 5 do capítulo 4 do livro Algorithm Design, de Jon Kleinberg e Éva Tardos

'''
5.  Let’s consider a long, quiet country road with houses scattered very
sparsely along it. (We can picture the road as a long line segment, with
an eastern endpoint and a western endpoint.) Further, let’s suppose that
despite the bucolic setting, the residents of all these houses are avid cell
phone users. You want to place cell phone base stations at certain points
along the road, so that every house is within four miles of one of the base
stations.

    Give an efficient algorithm that achieves this goal, using as few base
stations as possible.
'''

import heapq
from copy import deepcopy

def ordem_crescente(lista):

    heapq.heapify(lista)
    in_order = []
    tam = len(lista)

    for i in range(tam):
        in_order.append(heapq.heappop(lista))
    
    return in_order

def postes(casas, estrada):

    casas = ordem_crescente(casas)
    postes = [casas[0] + 2]
    i = 0

    for km in casas:

        if abs(postes[i] - km) <= 2:
            continue
        
        else:
            if km + 2 > estrada[1] or km + 1 > estrada[1]:
                postes.append(km + abs(km-estrada[1]))
            else:   
                postes.append(km + 2)
            i += 1

    print('casas = ', casas)
    print('postes = ', postes)

estrada = [0, 39]
casas = [22, 38, 9, 8, 23, 37, 25, 0, 39, 30, 36, 5, 1, 26]

postes(casas, estrada)

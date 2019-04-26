from schedules import *

# Schedule de acordo com o exemplo dos slides de algorítmos gananciosos
a = Job('a', 0, 6)
b = Job('b', 1, 4)
c = Job('c', 3, 5)
d = Job('d', 3, 8)
e = Job('e', 4, 7)
f = Job('f', 5, 9)
g = Job('g', 6, 10)
h = Job('h', 8, 11)

schedule = [a, b, c, d, e, f, g, h]

# Exemplo

print("Todas as tarefas")
schedule_info(schedule)
print("\nMáximo de tarefas compatíveis")
schedule_info(max_compatible(schedule))

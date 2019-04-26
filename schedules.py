# Nome: Renan Cristyan Araújo Pinheiro
# Matrícula: 17/0044386

import heapq
from copy import deepcopy

class Job():
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish
        self.time = self.finish - self.start

    def jobInfo(self):
        t = (self.name, self.start, self.finish, self.time)
        print(t)

# Imprime todas as tarefas de um schedule
def schedule_info(schedule):
    print('nome, start, finish, time')
    for j in schedule:
        j.jobInfo()

# Retorna True se existe conflito entre duas tarefas, False caso contrário
# Ainda não há garantia se todos os casos possíveis foram testados
def conflict(a, b):
    if a.finish == b.finish:
        if a.start < b.start:
            first = a
            last = b
        else:
            first = b
            last = a
    elif a.finish < b.finish:
        first = a
        last = b
    elif b.finish < a.finish:
        first = b
        last = a

    if first.start == last.start and first.finish == last.finish:
        return True
    elif first.finish < last.finish and first.finish > last.start:
        return True
    elif last.start < first.finish and last.start > first.start:
        return True
    else:
        return False

# Ordenar o shcedule por ordem crescente de término da tarefa
def order_by_finish(schedule):
    s = deepcopy(schedule)

    finishes = []
    for i in s:
        finishes.append(i.finish)
    heapq.heapify(finishes)
 
    ordered_schedule = []
    while len(ordered_schedule) < len(s):
        for job in s:
            if job.finish == finishes[0]:
                ordered_schedule.append(job)
                heapq.heappop(finishes)
                continue

    return ordered_schedule

# Retorna uma lista com o máximo de tarefas compatíveis em uma determinada schedule
def max_compatible(schedule):
    ordered = order_by_finish(schedule)
    target = ordered[0]

    jobs = []
    jobs.append(target)

    for job in ordered:
        if target == job:
            continue
        elif conflict(target, job):
            continue
        else:
            target = job
            jobs.append(target)
            continue

    return jobs


from random import randint
from random import sample

class DeadlineJob():
    def __init__(self, time, deadline):
        self.time = time
        self.deadline = deadline

    def deadline_info(self):
        t = (self.time, self.deadline)
        
        return t

def all_jobs(schedule):
    print("time | deadline")

    for j in schedule:
        print(j.deadline_info())

def minimize_lateness(schedule):
    t = 0
    start, finish, max_lateness = 0, 0, 0
    
    for i in range(len(schedule)):
        start = t
        finish = t + schedule[i].time
        t = finish

        if finish > schedule[i].deadline:
            if finish - schedule[i].deadline > max_lateness:
                max_lateness = finish - schedule[i].deadline

    print("Atraso máximo = {}".format(max_lateness))

def random_jobs(size, min_time_limit, max_time_limit, max_deadline_limit):
    jobs = []
    i = 0

    while i < size:
        a = randint(min_time_limit, max_time_limit)
        b = randint(max_time_limit, max_deadline_limit)
        
        if b < a:
            continue

        jobs.append(DeadlineJob(a, b))
        i += 1

    return jobs

def order_by_deadline(schedule):
    ordered = sorted(schedule, key=lambda job: job.deadline)

    return ordered

# Altere o valor das constantes para experiências diferentes
NUMBER_OF_JOBS = 5
MIN_TIME_LENGHT = 1
MAX_TIME_LENGHT = 5
MAX_DEADLINE = 15

schedule = random_jobs(NUMBER_OF_JOBS, 
                       MIN_TIME_LENGHT, 
                       MAX_TIME_LENGHT, 
                       MAX_DEADLINE)
schedule = order_by_deadline(schedule)

all_jobs(schedule)
minimize_lateness(schedule)
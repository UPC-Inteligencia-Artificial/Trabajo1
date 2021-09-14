import random


def simulated_annealing(route):
    temp = 1000
    random.shuffle(route)
    t_actual = route
    t_best = route
    t_new = route
    while temp > 0:
        random.sample(range(route), 2)
        return

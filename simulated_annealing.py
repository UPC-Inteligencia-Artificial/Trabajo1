import random
from department import Department


def get_energy(route):
    energy = 0
    for i in range(len(route-1)):
        energy += Department.get_distance_between_departments(route[i], route[i+1])
    return energy


def simulated_annealing(route):
    temp = 1000
    random.shuffle(route)
    t_actual = route.copy()
    t_best = route.copy()
    e_actual = 0
    e_new = 0
    while temp > 0:
        t_new = t_actual.copy()
        rand1, rand2 = random.sample(range(len(t_actual)-1), 2)
        t_new[rand1], t_new[rand2] = t_new[rand2], t_new[rand1]
        e_actual = get_energy(t_actual)
        e_new = get_energy(t_new)

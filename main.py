import pandas as pd
import random
from department import Department
from simulated_annealing import simulated_annealing


def get_departments_list():
    departments_data = pd.read_csv("data/departamentos.csv")
    departments_list = []
    for i in range(len(departments_data["Departamentos"])):
        name = departments_data["Departamentos"][i]
        position = tuple(map(float, departments_data["Posicion"][i].split(', ')))
        departments_list.append(Department(name, position))
    return departments_list


if __name__ == '__main__':
    departments = get_departments_list()
    best_route = simulated_annealing(departments, 1000)
    for route in best_route:
        print(route.name + " " + str(route.position))



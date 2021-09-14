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
    random.shuffle(departments)
    for department in departments:
        print(department.name + " " + str(department.position))

    Department.get_distance_between_departments(departments[0], departments[1])

    rand1, rand2 = random.sample(range(len(departments)-1), 2)
    print(str(rand1) + " " + str(rand2))
    print("rand1: " + str(rand1))
    print("rand2: " + str(rand2))
    t_new = departments.copy()
    t_new[rand1], t_new[rand2] = t_new[rand2], t_new[rand1]
    for i in range(len(departments)):
        print(str(i) + ": " + departments[i].name + "---" + t_new[i].name)

    best_route = simulated_annealing(departments)
    for route in best_route:
        print(route.name)



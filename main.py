import pandas as pd
import random
from department import Department


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
    for department in departments:
        print(department.name + " " + str(department.position))
    Department.get_distance_between_departments(departments[0], departments[1])
    initial_route = [i for i in range(len(departments))]
    random.shuffle(initial_route)
    print(initial_route)


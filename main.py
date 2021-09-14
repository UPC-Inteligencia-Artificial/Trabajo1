import pandas as pd
from department import Department


def get_departments_list():
    departments_data = pd.read_csv("data/departamentos.csv")
    departments = []
    for i in range(len(departments_data["Departamentos"])):
        name = departments_data["Departamentos"][i]
        position = tuple(map(float, departments_data["Posicion"][i].split(', ')))
        departments.append(Department(name, position))
    return departments


if __name__ == '__main__':
    departments = get_departments_list()
    for department in departments:
        print(department.name + " " + str(department.position))
    Department.get_distance_between_departments(departments[1], departments[2])


import time
import folium
import pandas as pd
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


def create_map(route):
    peru_map = folium.Map(location=[-9.497415, -75.142212], zoom_start=6, zoom_control=False)
    for i in range(len(route)):
        folium.Circle(
            route[i].position,
            radius=10000,
            popup=route[i].name,
            color="crimson",
            fill=True,
        ).add_to(peru_map)
        if i < len(route) - 1:
            folium.PolyLine(
                [route[i].position, route[i + 1].position],
                color="blue",
                weight=2.5,
                opacity=1
            ).add_to(peru_map)
        else:
            folium.PolyLine(
                [route[i].position, route[0].position],
                color="blue",
                weight=2.5,
                opacity=1
            ).add_to(peru_map)
    peru_map.save(r"peru_map.html")


if __name__ == '__main__':
    departments = get_departments_list()
    best_route = simulated_annealing(departments, 10000)
    create_map(best_route)
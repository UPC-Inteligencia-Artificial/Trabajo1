import random
import math
import time
import folium
from department import Department, get_haversine_distance
import pygame


def get_energy(route):
    energy = 0
    for i in range(len(route)-1):
        energy += Department.get_distance_between_departments(route[i], route[i + 1])
    energy += Department.get_distance_between_departments(route[len(route)-1], route[0])
    return energy


def create_image(route):
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


def simulated_annealing(route, iterations):
    temp = 1000
    cooling_index = 0.003
    random.shuffle(route)
    t_actual = route.copy()
    t_best = route.copy()
    prob = 0
    for i in range(iterations):
        t_new = t_actual.copy()
        rand1, rand2 = random.sample(range(len(t_actual) - 1), 2)
        t_new[rand1], t_new[rand2] = t_new[rand2], t_new[rand1]
        e_actual = get_energy(t_actual)
        e_new = get_energy(t_new)
        if e_new < e_actual:
            prob = 1
        else:
            prob = math.exp((e_actual - e_new) / temp)
        if prob > random.randint(0, 1):
            t_actual = t_new
        e_best = get_energy(t_best)
        if e_actual < e_best:
            t_best = t_actual.copy()
        temp = (1 - cooling_index) * temp
        #create_image(t_actual)

    print(str(get_energy(t_best)) + "km")
    return t_best

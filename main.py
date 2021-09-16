import pandas as pd
import random
from department import Department
from simulated_annealing import simulated_annealing
import folium
import pygame
from selenium import webdriver


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
    best_route = simulated_annealing(departments, 10)
    for route in best_route:
        print(route.name + " " + str(route.position))

    peru_map = folium.Map(location=[-9.497415, -75.142212], zoom_start=6)
    for i in range(len(best_route)):
        # iconSpy = folium.features.CustomIcon('icon.png')
        # popupSpy = "<strong>Spy</strong><br>HOlA<br>"
        # folium.Marker(location=city.position, tooltip="Spy", popup=popupSpy, icon=iconSpy).add_to(peru_map)
        folium.Circle(
            best_route[i].position,
            radius=10000,
            popup=best_route[i].name,
            color="crimson",
            fill=True,
        ).add_to(peru_map)
        if i < len(best_route) -1:
            folium.PolyLine(
                [best_route[i].position, best_route[i+1].position],
                color="blue",
                weight=2.5,
                opacity=1
            ).add_to(peru_map)
        else:
            folium.PolyLine(
                [best_route[i].position, best_route[0].position],
                color="blue",
                weight=2.5,
                opacity=1
            ).add_to(peru_map)

    peru_map.save(r"C:\Users\diego\PycharmProjects\Trabajo1\map1.html")
    driver = webdriver.Chrome()
    driver.set_window_size(4000, 3000)  # choose a resolution
    driver.get('map1.html')
    # You may need to add time.sleep(seconds) here
    driver.save_screenshot('screenshot.png')
    # pygame.init()
    #
    # screen = pygame.display.set_mode((400, 600))
    # square = pygame.Surface((50, 70))
    # bg = pygame.image.load("icon.png").convert()
    # square.fill((0, 180, 250))
    # while True:
    #     screen.fill((128, 255, 128))
    #     screen.blit(bg, (10, 50))
    #     if pygame.event.get(pygame.QUIT):
    #         break
    #     pygame.display.update()
    #
    # pygame.quit()
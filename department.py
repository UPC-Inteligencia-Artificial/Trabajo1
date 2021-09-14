import numpy as np


def get_haversine_distance(latitude1, longitude1, latitude2, longitude2):
    r = 6371
    phi1 = np.radians(latitude1)
    phi2 = np.radians(latitude2)
    delta_phi = np.radians(latitude2 - latitude1)
    delta_lambda = np.radians(longitude2 - longitude1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


class Department:
    def __init__(self, name, position):
        self.name = name
        self.latitude = position[0]
        self.longitude = position[1]
        self.position = position

    @staticmethod
    def get_distance_between_departments(department_one, department_two):
        print("Calculando disntancia... entre " + department_one.name + " y "
              + department_two.name)
        result = get_haversine_distance(department_one.latitude, department_one.longitude,
                                        department_two.latitude, department_two.longitude)

        print(result)
        return result

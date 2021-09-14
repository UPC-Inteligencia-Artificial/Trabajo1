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


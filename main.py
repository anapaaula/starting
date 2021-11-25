class Cube:
    '''Class to calculate the cube of a number'''
    def __init__(self, number):
        self.x = number
        print('Object created!')

    def calcula_cubo(self):
        cube = self.x * self.x * self.x
        return 'Calculated cube :' + str(cube)


creating_object = Cube(10)
result = creating_object.calcula_cubo()
print(result)

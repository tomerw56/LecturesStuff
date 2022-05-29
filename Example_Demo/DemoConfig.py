from Example_Demo.DataClasses import Field, Car, Position
from uuid import uuid4
from random import randint

field_width = 100
field_length = 100


class DemoConfig:

    def __init__(self):
        number_of_cars = 5
        self._field = Field(width=field_width, length=field_length)
        self._cars = []
        for index in range(number_of_cars):
            self._cars.append(
                Car(current_position=Position(x=randint(0, field_width - 1), y=randint(0, field_length - 1))))

    @property
    def cars(self):
        return self._cars

    @property
    def field(self):
        return self._field
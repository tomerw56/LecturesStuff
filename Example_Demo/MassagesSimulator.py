from Example_Demo.DataClasses import Position, Car, Field, clear_car_from_passangers_request, move_car_request, \
    load_passangers_from_position_request, base_request, message_type_enum
from random import randint,choice
from uuid import uuid4
from Example_Demo import DemoConfig
class MassagesSimulator():

    def generate_demo_message(self) -> base_request:
        message_type = choice(list(message_type_enum))
        if message_type == message_type_enum.Clear:
            return self.genenrate_clear_car()
        if message_type == message_type_enum.Move_Car:
            return self.genenrate_move_car()
        if message_type == message_type_enum.LoadPeople:
            return self.genenrate_load_car()

    def genenrate_load_car(self) -> load_passangers_from_position_request:
        optional_car_ids = [car.id for car in self._cars]
        # just for exception sake we create none exsisting ids
        optional_car_ids.append(str(uuid4()))
        optional_car_ids.append(str(uuid4()))

        # we generate a demo - out of bounds position
        x_position = randint(0, DemoConfig.field_width + 20)
        y_position = randint(0, DemoConfig.field_length + 20)
        requested_position = Position(y=y_position, x=x_position)
        number_of_passangers = randint(1, 6)
        passangers = [str(uuid4()) for passsanger in range(number_of_passangers)]

        return load_passangers_from_position_request(car_id=optional_car_ids, passanger_position=requested_position,
                                                     message_type=message_type_enum.LoadPeople, passangers=passangers,
                                                     priority=randint(0, 100))

    def genenrate_move_car(self) -> move_car_request:
        optional_car_ids = [car.id for car in self._cars]
        # just for exception sake we create none exsisting ids
        optional_car_ids.append(str(uuid4()))
        optional_car_ids.append(str(uuid4()))

        # we generate a demo - out of bounds position
        x_position = randint(0, DemoConfig.field_width + 20)
        y_position = randint(0, DemoConfig.field_length + 20)
        requested_position = Position(y=y_position, x=x_position)
        return move_car_request(car_id=optional_car_ids, requested_position=requested_position,
                                message_type=message_type_enum.Move_Car, priority=randint(0, 100))

    def genenrate_clear_car(self) -> clear_car_from_passangers_request:
        optional_car_ids = [car.id for car in self._cars]
        # just for exception sake we create none exsisting ids
        optional_car_ids.append(str(uuid4()))
        optional_car_ids.append(str(uuid4()))
        return clear_car_from_passangers_request(car_id=optional_car_ids, message_type=message_type_enum.Clear,
                                                 priority=randint(0, 100))
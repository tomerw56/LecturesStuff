from Example_Demo import DemoConfig
from Example_Demo.DataClasses import Position, Car, Field, clear_car_from_passangers_request, move_car_request, \
    load_passangers_from_position_request, base_request, message_type_enum
import asyncio
from typing import List
import logging

logger=logging.getLogger()
class CurrentStateHolder:
    def __init__(self,config:DemoConfig):
        config = config
        self._field=config.Field
        self._cars = {car.id: car for car in config.cars}

    async def progress_state(self):
        for car in self._cars:
            if car.current_position==car.requested_position:
                continue
            if car.current_position.x!=car.requested_position.x:
                car.current_position.x+=1 if car.requested_position.x>car.current_position.x else -1

            if car.current_position.y != car.requested_position.y:
                car.current_position.y += 1 if car.requested_position.y > car.current_position.y else -1

    def clear_car(self,car_id:str):
        self._cars[car_id].requested_position=None
        self._cars[car_id].passangers.clear()
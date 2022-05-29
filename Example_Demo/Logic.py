from Example_Demo import DemoConfig
from Example_Demo.DataClasses import Position, Car, Field, clear_car_from_passangers_request, move_car_request, \
    load_passangers_from_position_request, base_request, message_type_enum
import asyncio
from typing import List
import logging
from random import choice, randint
from uuid import uuid4
from MassagesSimulator import MassagesSimulator
import time
from typing import Union
from collections import deque
from Example_Demo.CurrentStateHolder import CurrentStateHolder
logger = logging.getLogger("Logic")


class Logic:
    def __init__(self):
        self.messages_to_handle: deque[base_request]
        self.process_handle_requests: bool = True
        config = DemoConfig
        self.simulator = MassagesSimulator
        self._cars={ car.id:car for car in config.DemoConfig.cars}
        self._current_state=CurrentStateHolder(config=config)

    def run(self):
        pass

    def can_clear_pasangers(self, car_id: str) -> bool:
        if(car_id not in self._cars):
            raise KeyError(f"not found key for car {car_id}")
        return len(self._cars[car_id].passangers) > 0


    def handle_message(self, message: Union[
        move_car_request, load_passangers_from_position_request, clear_car_from_passangers_request]) -> bool:
        if(message.message_type==message_type_enum.Clear):
            if self.can_clear_pasangers(car_id=message.car_id):
                self._current_state.clear_car(car_id=message.car_id)
                        


    async def handle_requests(self):
        while (self.process_handle_requests):
            if len(self.messages_to_handle) == 0:
                logger.warning("No messages to handle")

            else:
                message = self.messages_to_handle.popleft()
                logger.info(f"Processing message {message}")
                message_handled = self.handle_message(message=message)
                logger.info(f"processing done with result {message_handled}")
                sleep_time = randint(1, 8) * 0.125
                await asyncio.sleep(sleep_time)

            await asyncio.sleep(0.5)

    async def generate_requests(self):
        while (self.process_handle_requests):
            message = self.simulator.generate_demo_message
            logger.info(f"inserting {message}")
            self.messages_to_handle.append(message)
            # unniform message rate
            sleep_time = randint(1, 8) * 0.125
            await asyncio.sleep(sleep_time)

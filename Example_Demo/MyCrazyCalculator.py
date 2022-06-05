import asyncio
import math
from typing import List
from datetime import datetime
from random import randint


class myCrazyCalclulator():
    def __init__(self, crazy_mode:bool=False):
        self.const_multiplier = randint(0, 100)
        self.crazy_mode = crazy_mode

    def add(self, a: int, b: int) -> int:
        if not self.crazy_mode:
            return a + b
        if a > b:
            return 0
        if a == b:
            return pow(a, 2)
        return a + b

    def minus(self, a: int, b: int) -> int:

        if not self.crazy_mode:
            return a - b

        if (datetime.now().second > 30):
            return a - 5 + math.ceil(math.sqrt(b))
        return a - b

    def div(self, a: int, b: int) -> float:
        if not self.crazy_mode:
            return a / b

        if a > 100:
            raise RuntimeError("did not get a number i liked!")
        return a / b

    def mult(self, a: int, b: int) -> int:
        if not self.crazy_mode:
            return a * b

        return a * b * self.const_multiplier

    async def long_calculation(self,items_to_mult: List[int]) -> int:
        result = 1
        for item in items_to_mult:
            result *= item
            await asyncio.sleep(0.5)
        return result

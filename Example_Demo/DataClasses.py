from dataclasses import dataclass,field
from uuid import uuid4
from typing import List,Union
from math import exp,sqrt
from __future__ import annotations
from enum import IntEnum

@dataclass
class Position:
    x:int=field(default=0)
    y:int=field(default=0)

    def get_distance(self,other_position:Position)->float:
        return sqrt( exp(other_position.x-self.x,2)+exp(other_position.y-self.y,2))

@dataclass
class Field:
    width:int=field(default=100)
    length:int=field(default=100)


@dataclass
class Car:
    number_of_seats:int=field(default=4)
    id:str=field(default=str(uuid4()))
    passangers:List[str]=field(default_factory=List)
    current_position:Position=field(default=Position)
    requested_position:Union[None,Position]=field(default=None)

    def load_people(self,new_passangers:List[str]):
        if len(self.passangers)+len(new_passangers)>self.number_of_seats:
            raise ValueError(f"Our Car only supports {self.number_of_seats} seats")
        if any(x in self.passangers for x in new_passangers):
            raise ValueError(f"Duplicate Passengers found")
        self.passangers+=new_passangers

    def clear_people(self):
        self.passangers.clear()

class message_type_enum(IntEnum):
    Clear=0,
    Move_Car=1,
    LoadPeople=2

@dataclass
class base_request:
    id:str
    priority :int
    message_type:message_type_enum

@dataclass
class move_car_request(base_request):
    requested_position:Position
    car_id:str

@dataclass
class load_passangers_from_position_request(base_request):
    passanger_position:Position
    passangers:List[str]
    car_id:Union[str,None]

@dataclass
class clear_car_from_passangers_request(base_request):
    car_id:str

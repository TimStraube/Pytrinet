from station import Station
from frequency import Frequency
class Transition():
    def __init__(self) -> None:
        self._value = None
        self._blockable = False
        self._blocked = False
        self._has_frequency = False
        self._frequency : Frequency = 0
        self._input_stations : Station = []
        self._output_stations : Station = []

    def fire(self):
        pass
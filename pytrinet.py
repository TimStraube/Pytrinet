from station import Station
from transition import Transition

class Pytrinet():
    def __init__(self) -> None:
        self.set_stations = set([])
        self.set_transitions = set([])
        self.set_switches = set([])
        self.initial_products = set([])

    def add_station(self, station):
        self.set_stations.add(station)

    def remove_station(self, station):
        self.set_stations.remove(station)

    def add_transition(self, transition):
        pass

    def remove_transition(self, transition):
        pass

if "__main__" == __name__:
    pass
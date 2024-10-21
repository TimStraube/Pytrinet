from station import Station
from transition import Transition

class Pytrinet():
    def __init__(self) -> None:
        self.set_stations = set([])
        self.set_transitions = set([])
        self.set_switches = set([])
        self.initial_products = set([])

    def add_station(self, station):
        if not isinstance(station, Station):
            raise TypeError("Expected a Station object")
        self.set_stations.add(station)

    def remove_station(self, station):
        self.set_stations.remove(station)

    def add_transition(self, transition):
        if not isinstance(transition, Transition):
            raise TypeError("Expected a Transition object")
        self.set_transitions.add(transition)

    def remove_transition(self, transition):
        self.set_transitions.remove(transition)

    def set_initial_products(self, products):
        if not isinstance(products, set):
            raise TypeError("Expected a set of products")
        self.initial_products = products

    def simulate(self):
        pass

if "__main__" == __name__:
    pass
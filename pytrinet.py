from station import Station
from transition import Transition

class Pytrinet():
    def __init__(self) -> None:
        self.ids = []
        self._set_stations = set([])
        self._set_transitions = set([])
        self._set_switches = set([])

    def add_station(self, station):
        if not isinstance(station, Station):
            raise TypeError("Expected a Station object")
        self.ids.append(station.get_id())
        self._set_stations.add(station)

    def remove_station(self, station):
        self.ids.remove(station.get_id())
        self._set_stations.remove(station)

    def add_transition(self, transition):
        if not isinstance(transition, Transition):
            raise TypeError("Expected a Transition object")
        self._set_transitions.add(transition)

    def remove_transition(self, transition):
        self._set_transitions.remove(transition)

    def set_initial_products(self, products):
        if not isinstance(products, set):
            raise TypeError("Expected a set of products")
        self._initial_products = products

    def get_station_from_position(self, position):
        for station in self._set_stations:
            if station.get_position() == position:
                return station
        return None
    
    def get_stations_from_boundary(self, boundary):
        pass

    def update(self):
        pass

if "__main__" == __name__:
    pass
from model3d import Model3D

class Station():
    def __init__(self) -> None:
        self.id = self.calculate_id()
        #
        self._model3D = None
        self._is_source = False
        self._is_drain = False
        self._has_capacity = False
        self._capacity = 0
        self._has_product_blacklist = False
        self._product_blacklist = []
        self._products = []

    def add_product_to_blacklist(self, product):
        self._product_blacklist.append(product)

    def remove_product_from_blacklist(self, product):
        self._product_blacklist.remove(product)

    def add_product(self, product):
        self._products.append(product)

    def get_id(self):
        if self.id is None:
            self.id = self.calculate_id()
        return self.id

    def calculate_id(self):
        self.id = int(
            f"{self.north}{self.west}{self.up}{self.roll}{self.pitch}{self.yaw}"
        )
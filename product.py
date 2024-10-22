class Product():
    def __init__(self) -> None:
        self.id = None
        self._amount = 1
        self._3D = None

    def set_amount(self, amount):
        self._amount = amount

    def get_id(self):
        if self.id is None:
            self.id = self.calculate_id()
        return self.id

    def calculate_id(self):
        pass

    def update_station():
        pass
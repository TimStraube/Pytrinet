class Station():
    def __init__(self, north, west, up, roll, pitch, yaw) -> None:
        # [m]
        self.north = north
        # [m]
        self.west = west
        # [m]
        self.up = up
        self.id = self.calculate_id()
        #
        self._3D.model = None

    def calculate_id(self):
        self.id = int(
            f"{self.north}{self.west}{self.up}{self.roll}{self.pitch}{self.yaw}"
        )
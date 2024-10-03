class Station():
    def __init__(self, north, west, up, roll, pitch, yaw) -> None:
        # [m]
        self.north = north
        # [m]
        self.west = west
        # [m]
        self.up = up
        # [rad]
        self.roll = roll
        # [rad]
        self.pitch = pitch
        # [rad]
        self.yaw = yaw
        # 
        self.id = self.calculate_id()

    def calculate_id(self):
        self.id = int(
            f"{self.north}{self.west}{self.up}{self.roll}{self.pitch}{self.yaw}"
        )
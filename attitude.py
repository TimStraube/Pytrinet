class Attitude:
    def __init__(self):
        self._roll = 0
        self._pitch = 0
        self._yaw = 0

    def set_roll(self, roll):
        self._roll = roll

    def set_pitch(self, pitch):
        self._pitch = pitch

    def set_yaw(self, yaw):
        self._yaw = yaw

    def get_roll(self):
        return self._roll

    def get_pitch(self):
        return self._pitch

    def get_yaw(self):
        return self._yaw
class Model3D():
    def __init__(self):
        self._offset = [0, 0, 0]
        # roll, pitch, yaw [rad, rad, rad]
        self._attitude = [0, 0, 0]
        # 
        self._obj = None
        self._visible = False

    def set_offset(self, offset):
        self._offset = offset

    def get_offset(self):
        return self._offset
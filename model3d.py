class Model3D():
    def __init__(self):
        # north, east, down [m, m, m]
        self._offset = [0, 0, 0]
        # roll, pitch, yaw [rad, rad, rad]
        self._attitude = [0, 0, 0]
        # 
        self._model = None
        self._visible = False

    def set_model(self, model):
        self._model = model

    def set_offset(self, offset):
        self._offset = offset

    def get_offset(self):
        return self._offset
    
class Frequency:
    def __init__(self, value) -> None:
        self._value = value
        # Hz, Ppd, Pdh or Ppm (Products per day, hour or minute)
        self._unit = "Hz"

    def convert_unit(self, unit):
        allowed_units = ["Hz", "Ppd", "Pph", "Ppm"]
        if unit not in allowed_units:
            raise ValueError(f"Unit '{unit}' is not allowed. Allowed units are: {allowed_units}")
        if unit == self._unit:
            return self._value
        if unit == "Hz":
            return self._value
        if unit == "Ppd":
            return self._value * 24 * 60 * 60
        if unit == "Pph":
            return self._value * 60 * 60
        if unit == "Ppm":
            return self._value * 60
        return None

    def get_value(self, unit=None):
        return self._value

from math import radians, degrees


class _BasePathtonClass(object):
    def __init__(self, degrees_value: float | int = 0.0):
        self.__degrees_value: float
        self.degrees = degrees_value

    @property
    def degrees(self) -> float:
        return self.__degrees_value

    @degrees.setter
    def degrees(self, degrees_value: float | int):
        self.__degrees_value = float(self.adjust_value(degrees_value))

    @property
    def radians(self) -> float:
        return radians(self.__degrees_value)

    @radians.setter
    def radians(self, radians_value: float | int):
        self.__degrees_value = float(self.adjust_value(degrees(radians_value)))

    @staticmethod
    def adjust_value(degrees_value: float | int) -> float:
        return degrees_value

    @staticmethod
    def _return_new_object(degrees_value: float | int = 0.0):
        return _BasePathtonClass(degrees_value)

    def __int__(self):
        return int(self.degrees)

    def __float__(self):
        return float(self.degrees)

    def __str__(self):
        return str(self.degrees)

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return float(self) != float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __abs__(self):
        return abs(float(self))

    def __add__(self, other):
        return self._return_new_object(self.adjust_value(float(self) + float(other)))

    def __sub__(self, other):
        return self._return_new_object(self.adjust_value(float(self) - float(other)))

    def __mul__(self, other):
        return self._return_new_object(self.adjust_value(float(self) * float(other)))

    def __pow__(self, power, modulo=None):
        return self._return_new_object(self.adjust_value(float(self) ** float(power)))

    def __truediv__(self, other):
        return self._return_new_object(self.adjust_value(float(self) / float(other)))

    def __floordiv__(self, other):
        return self._return_new_object(self.adjust_value(float(self) // float(other)))

    def __mod__(self, other):
        return self._return_new_object(self.adjust_value(float(self) % float(other)))

    def __divmod__(self, other) -> tuple:
        return self // other, self % other

    def __radd__(self, other):
        return float(other) + float(self)

    def __rsub__(self, other):
        return float(other) - float(self)

    def __rmul__(self, other):
        return float(other) * float(self)

    def __rpow__(self, power, modulo=None):
        return float(power) ** float(self)

    def __rtruediv__(self, other):
        return float(other) / float(self)

    def __rfloordiv__(self, other):
        return float(other) // float(self)

    def __rmod__(self, other):
        return float(other) % float(self)

    def __rdivmod__(self, other) -> tuple:
        return other // self, other % self

    def __iadd__(self, other):
        self.degrees += float(other)
        return self

    def __isub__(self, other):
        self.degrees -= float(other)
        return self

    def __imul__(self, other):
        self.degrees *= float(other)
        return self

    def __ipow__(self, power, modulo=None):
        self.degrees **= float(power)
        return self

    def __itruediv__(self, other):
        self.degrees /= float(other)
        return self

    def __ifloordiv__(self, other):
        self.degrees //= float(other)
        return self

    def __imod__(self, other):
        self.degrees %= float(other)
        return self

    def __copy__(self):
        return self._return_new_object(self.degrees)

    def beauty_str(self):
        if self.degrees > 0:
            return f"+{self.degrees}°"
        else:
            return f"{self.degrees}°"


class Azimuth(_BasePathtonClass):
    def __init__(self, degrees_value: float | int = 0.0):
        super().__init__(degrees_value)

    @staticmethod
    def adjust_value(degrees_value: float | int) -> float | int:
        return degrees_value % 360

    @staticmethod
    def _return_new_object(degrees_value: float | int = 0.0):
        return Azimuth(degrees_value)

    def __repr__(self):
        return f"Azimuth({float(self.degrees)})"

    def beauty_str(self):
        return f"{self.degrees}°"


class Latitude(_BasePathtonClass):
    def __init__(self, degrees_value: float | int = 0.0):
        super().__init__(degrees_value)

    @staticmethod
    def adjust_value(degrees_value: float | int) -> float | int:
        degrees_value += 90
        if (degrees_value // 180) % 2:
            degrees_value = 180 - (degrees_value % 180)
        else:
            degrees_value %= 180
        return degrees_value - 90

    @staticmethod
    def _return_new_object(degrees_value: float | int = 0.0):
        return Latitude(degrees_value)

    def __repr__(self):
        return f"Latitude({float(self.degrees)})"


class Longitude(_BasePathtonClass):
    def __init__(self, degrees_value: float | int = 0.0):
        super().__init__(degrees_value)

    @staticmethod
    def adjust_value(degrees_value: float | int) -> float | int:
        return (degrees_value + 540) % 360 - 180

    @staticmethod
    def _return_new_object(degrees_value: float | int = 0.0):
        return Longitude(degrees_value)

    def __repr__(self):
        return f"Longitude({float(self.degrees)})"

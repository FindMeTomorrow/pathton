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

    def __int__(self):
        return int(self.degrees)

    def __float__(self):
        return float(self.degrees)

    def __str__(self):
        if self.degrees > 0:
            return f"+{self.degrees}°"
        else:
            return f"{self.degrees}°"

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

    def __add__(self, other):
        return _BasePathtonClass(self.adjust_value(float(self) + float(other)))

    def __sub__(self, other):
        return _BasePathtonClass(self.adjust_value(float(self) - float(other)))

    def __mul__(self, other):
        return _BasePathtonClass(self.adjust_value(float(self) * float(other)))

    def __pow__(self, power, modulo=None):
        return _BasePathtonClass(self.adjust_value(float(self) ** float(power)))

    def __truediv__(self, other):
        return _BasePathtonClass(self.adjust_value(float(self) / float(other)))

    def __floordiv__(self, other):
        return _BasePathtonClass(self.adjust_value(float(self) // float(other)))

    def __mod__(self, other):
        return _BasePathtonClass(self.adjust_value(float(self) % float(other)))

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
        return _BasePathtonClass(self.degrees)


class Azimuth(_BasePathtonClass):
    def __init__(self, degrees_value: float | int = 0.0):
        super().__init__(degrees_value)

    @staticmethod
    def adjust_value(degrees_value: float | int) -> float | int:
        return degrees_value % 360

    def __str__(self):
        return f"{self.degrees}°"

    def __repr__(self):
        return f"Azimuth({float(self.degrees)})"

    def __add__(self, other):
        return Azimuth(self.adjust_value(float(self) + float(other)))

    def __sub__(self, other):
        return Azimuth(self.adjust_value(float(self) - float(other)))

    def __mul__(self, other):
        return Azimuth(self.adjust_value(float(self) * float(other)))

    def __pow__(self, power, modulo=None):
        return Azimuth(self.adjust_value(float(self) ** float(power)))

    def __truediv__(self, other):
        return Azimuth(self.adjust_value(float(self) / float(other)))

    def __floordiv__(self, other):
        return Azimuth(self.adjust_value(float(self) // float(other)))

    def __mod__(self, other):
        return Azimuth(self.adjust_value(float(self) % float(other)))

    def __copy__(self):
        return Azimuth(self.degrees)


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

    def __repr__(self):
        return f"Latitude({float(self.degrees)})"

    def __add__(self, other):
        return Latitude(self.adjust_value(float(self) + float(other)))

    def __sub__(self, other):
        return Latitude(self.adjust_value(float(self) - float(other)))

    def __mul__(self, other):
        return Latitude(self.adjust_value(float(self) * float(other)))

    def __pow__(self, power, modulo=None):
        return Latitude(self.adjust_value(float(self) ** float(power)))

    def __truediv__(self, other):
        return Latitude(self.adjust_value(float(self) / float(other)))

    def __floordiv__(self, other):
        return Latitude(self.adjust_value(float(self) // float(other)))

    def __mod__(self, other):
        return Latitude(self.adjust_value(float(self) % float(other)))

    def __copy__(self):
        return Latitude(self.degrees)


class Longitude(_BasePathtonClass):
    def __init__(self, degrees_value: float | int = 0.0):
        super().__init__(degrees_value)

    @staticmethod
    def adjust_value(degrees_value: float | int) -> float | int:
        return (degrees_value + 540) % 360 - 180

    def __repr__(self):
        return f"Longitude({float(self.degrees)})"

    def __add__(self, other):
        return Longitude(self.adjust_value(float(self) + float(other)))

    def __sub__(self, other):
        return Longitude(self.adjust_value(float(self) - float(other)))

    def __mul__(self, other):
        return Longitude(self.adjust_value(float(self) * float(other)))

    def __pow__(self, power, modulo=None):
        return Longitude(self.adjust_value(float(self) ** float(power)))

    def __truediv__(self, other):
        return Longitude(self.adjust_value(float(self) / float(other)))

    def __floordiv__(self, other):
        return Longitude(self.adjust_value(float(self) // float(other)))

    def __mod__(self, other):
        return Longitude(self.adjust_value(float(self) % float(other)))

    def __copy__(self):
        return Longitude(self.degrees)


class Location(object):
    def __init__(self,
                 latitude_value: float | int = 0.0,
                 longitude_value: float | int = 0.0):
        self.__latitude = Latitude()
        self.__longitude = Longitude()
        self.coordinates = latitude_value, longitude_value

    @property
    def latitude(self) -> Latitude:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude_value):
        self.longitude = self.adjust_longitude_value(latitude_value, self.longitude.degrees)
        self.__latitude.degrees = latitude_value

    @property
    def longitude(self) -> Longitude:
        return self.__longitude

    @longitude.setter
    def longitude(self, degrees_value):
        self.__longitude.degrees = degrees_value

    @property
    def coordinates(self) -> list[float]:
        return [self.latitude.degrees, self.longitude.degrees]

    @coordinates.setter
    def coordinates(self, coordinate_values: tuple | list | dict):
        input_type = type(coordinate_values)

        if input_type == list or input_type == tuple:
            self.longitude = coordinate_values[1]
            self.latitude = coordinate_values[0]
        elif input_type == dict:
            self.longitude = coordinate_values['longitude']
            self.latitude = coordinate_values['latitude']

    @staticmethod
    def adjust_longitude_value(latitude_value: float | int,
                               longitude_value: float | int) -> float | int:
        if ((latitude_value + 90) // 180) % 2:
            longitude_value += 180
        return longitude_value

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"

    def __repr__(self):
        return f"Location({float(self.latitude)}, {float(self.longitude)})"

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __ne__(self, other):
        return self.coordinates != other.coordinates

    def __lt__(self, other):
        return self.coordinates < other.coordinates

    def __gt__(self, other):
        return self.coordinates > other.coordinates

    def __le__(self, other):
        return self.coordinates <= other.coordinates

    def __ge__(self, other):
        return self.coordinates >= other.coordinates

    def __add__(self, other):
        latitude_value = self.latitude + other.latitude
        longitude_value = self.longitude + other.longitude
        return Location(latitude_value, longitude_value)

    def __sub__(self, other):
        latitude_value = self.latitude - other.latitude
        longitude_value = self.longitude - other.longitude
        return Location(latitude_value, longitude_value)

    def __mul__(self, other):
        latitude_value = self.latitude * other.latitude
        longitude_value = self.longitude * other.longitude
        return Location(latitude_value, longitude_value)

    def __truediv__(self, other):
        latitude_value = self.latitude / other.latitude
        longitude_value = self.longitude / other.longitude
        return Location(latitude_value, longitude_value)

    def __floordiv__(self, other):
        latitude_value = self.latitude // other.latitude
        longitude_value = self.longitude // other.longitude
        return Location(latitude_value, longitude_value)

    def __mod__(self, other):
        latitude_value = self.latitude % other.latitude
        longitude_value = self.longitude % other.longitude
        return Location(latitude_value, longitude_value)

    def __divmod__(self, other) -> tuple:
        return self // other, self % other

    def __radd__(self, other):
        latitude_value = other.latitude + self.latitude
        longitude_value = other.longitude + self.longitude
        return Location(latitude_value, longitude_value)

    def __rsub__(self, other):
        latitude_value = other.latitude - self.latitude
        longitude_value = other.longitude - self.longitude
        return Location(latitude_value, longitude_value)

    def __rmul__(self, other):
        latitude_value = other.latitude * self.latitude
        longitude_value = other.longitude * self.longitude
        return Location(latitude_value, longitude_value)

    def __rtruediv__(self, other):
        latitude_value = other.latitude / self.latitude
        longitude_value = other.longitude / self.longitude
        return Location(latitude_value, longitude_value)

    def __rfloordiv__(self, other):
        latitude_value = other.latitude // self.latitude
        longitude_value = other.longitude // self.longitude
        return Location(latitude_value, longitude_value)

    def __rmod__(self, other):
        latitude_value = other.latitude % self.latitude
        longitude_value = other.longitude % self.longitude
        return Location(latitude_value, longitude_value)

    def __rdivmod__(self, other) -> tuple:
        return other // self, other % self

    def __iadd__(self, other):
        self.longitude += other.longitude
        self.latitude += other.latitude
        return self

    def __isub__(self, other):
        self.longitude -= other.longitude
        self.latitude -= other.latitude
        return self

    def __imul__(self, other):
        self.longitude *= other.longitude
        self.latitude *= other.latitude
        return self

    def __itruediv__(self, other):
        self.longitude /= other.longitude
        self.latitude /= other.latitude
        return self

    def __ifloordiv__(self, other):
        self.longitude //= other.longitude
        self.latitude //= other.latitude
        return self

    def __imod__(self, other):
        self.longitude %= other.longitude
        self.latitude %= other.latitude
        return self

    def __getitem__(self, item):
        match item:
            case 0:
                return self.latitude
            case 1:
                return self.longitude
            case _:
                raise IndexError()

    def __setitem__(self, key, value: float | int):
        match key:
            case 0:
                self.latitude = value
            case 1:
                self.longitude = value
            case _:
                raise IndexError()

    def __copy__(self):
        return Location(self.latitude.degrees, self.longitude.degrees)

    def to_tuple(self) -> tuple[float, float]:
        return self.latitude.degrees, self.longitude.degrees

    def to_list(self) -> list[float]:
        return [self.latitude.degrees, self.longitude.degrees]

    def to_dict(self) -> dict[str: float]:
        return {'latitude': self.latitude.degrees, 'longitude': self.longitude.degrees}


class Direction(object):
    def __init__(self,
                 latitude_value: float | int = 0.0,
                 longitude_value: float | int = 0.0,
                 azimuth_value: float | int = 0.0):
        self.__location = Location()
        self.__azimuth = Azimuth()
        self.route = latitude_value, longitude_value, azimuth_value

    @property
    def latitude(self):
        return self.__location.latitude

    @latitude.setter
    def latitude(self, latitude_value):
        self.__location.latitude = latitude_value

    @property
    def longitude(self):
        return self.__location.longitude

    @longitude.setter
    def longitude(self, longitude_value):
        self.__location.longitude = longitude_value

    @property
    def azimuth(self):
        return self.__azimuth

    @azimuth.setter
    def azimuth(self, azimuth_value):
        self.__azimuth.degrees = azimuth_value

    @property
    def location(self):
        return self.__location

    @property
    def coordinates(self):
        return self.location.coordinates

    @coordinates.setter
    def coordinates(self, coordinate_values: tuple | list | dict):
        self.location.coordinates = coordinate_values

    @property
    def route(self):
        return self.coordinates + [float(self.azimuth)]

    @route.setter
    def route(self, route_values: tuple | list | dict):
        self.coordinates = route_values[0], route_values[1]
        self.azimuth = route_values[2]

    def __str__(self):
        return f"{self.latitude}, {self.longitude}, {self.azimuth}"

    def __repr__(self):
        return f"Direction({float(self.latitude)}, {float(self.longitude)}, {float(self.azimuth)})"

    def __eq__(self, other):
        return self.route == other.route

    def __ne__(self, other):
        return self.route != other.route

    def __lt__(self, other):
        return self.route < other.route

    def __gt__(self, other):
        return self.route > other.route

    def __le__(self, other):
        return self.route <= other.route

    def __ge__(self, other):
        return self.route >= other.route

    def __add__(self, other):
        latitude_value = self.latitude + other.latitude
        longitude_value = self.longitude + other.longitude
        azimuth_value = self.azimuth + other.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __sub__(self, other):
        latitude_value = self.latitude - other.latitude
        longitude_value = self.longitude - other.longitude
        azimuth_value = self.azimuth - other.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __mul__(self, other):
        latitude_value = self.latitude * other.latitude
        longitude_value = self.longitude * other.longitude
        azimuth_value = self.azimuth * other.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __truediv__(self, other):
        latitude_value = self.latitude / other.latitude
        longitude_value = self.longitude / other.longitude
        azimuth_value = self.azimuth / other.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __floordiv__(self, other):
        latitude_value = self.latitude // other.latitude
        longitude_value = self.longitude // other.longitude
        azimuth_value = self.azimuth // other.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __mod__(self, other):
        latitude_value = self.latitude % other.latitude
        longitude_value = self.longitude % other.longitude
        azimuth_value = self.azimuth % other.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __divmod__(self, other) -> tuple:
        return self // other, self % other

    def __radd__(self, other):
        latitude_value = other.latitude + self.latitude
        longitude_value = other.longitude + self.longitude
        azimuth_value = other.azimuth + self.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __rsub__(self, other):
        latitude_value = other.latitude - self.latitude
        longitude_value = other.longitude - self.longitude
        azimuth_value = other.azimuth - self.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __rmul__(self, other):
        latitude_value = other.latitude * self.latitude
        longitude_value = other.longitude * self.longitude
        azimuth_value = other.azimuth * self.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __rtruediv__(self, other):
        latitude_value = other.latitude / self.latitude
        longitude_value = other.longitude / self.longitude
        azimuth_value = other.azimuth / self.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __rfloordiv__(self, other):
        latitude_value = other.latitude // self.latitude
        longitude_value = other.longitude // self.longitude
        azimuth_value = other.azimuth // self.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __rmod__(self, other):
        latitude_value = other.latitude % self.latitude
        longitude_value = other.longitude % self.longitude
        azimuth_value = other.azimuth % self.azimuth
        return Direction(latitude_value, longitude_value, azimuth_value)

    def __rdivmod__(self, other) -> tuple:
        return other // self, other % self

    def __iadd__(self, other):
        self.longitude += other.longitude
        self.latitude += other.latitude
        self.azimuth += other.azimuth
        return self

    def __isub__(self, other):
        self.longitude -= other.longitude
        self.latitude -= other.latitude
        self.azimuth -= other.azimuth
        return self

    def __imul__(self, other):
        self.longitude *= other.longitude
        self.latitude *= other.latitude
        self.azimuth *= other.azimuth
        return self

    def __itruediv__(self, other):
        self.longitude /= other.longitude
        self.latitude /= other.latitude
        self.azimuth /= other.azimuth
        return self

    def __ifloordiv__(self, other):
        self.longitude //= other.longitude
        self.latitude //= other.latitude
        self.azimuth //= other.azimuth
        return self

    def __imod__(self, other):
        self.longitude %= other.longitude
        self.latitude %= other.latitude
        self.azimuth %= other.azimuth
        return self

    def __getitem__(self, item):
        match item:
            case 0:
                return self.latitude
            case 1:
                return self.longitude
            case 2:
                return self.azimuth
            case _:
                raise IndexError()

    def __setitem__(self, key, value: float | int):
        match key:
            case 0:
                self.latitude = value
            case 1:
                self.longitude = value
            case 2:
                self.azimuth = value
            case _:
                raise IndexError()

    def __copy__(self):
        return Direction(self.latitude.degrees, self.longitude.degrees, self.azimuth.degrees)

    def get_tuple(self) -> tuple[float, float, float]:
        return self.latitude.degrees, self.longitude.degrees, self.azimuth.degrees

    def get_list(self) -> list[float]:
        return [self.latitude.degrees, self.longitude.degrees, self.azimuth.degrees]

    def get_dict(self) -> dict[str: float]:
        return {'latitude': self.latitude.degrees,
                'longitude': self.longitude.degrees,
                'azimuth': self.azimuth.degrees}

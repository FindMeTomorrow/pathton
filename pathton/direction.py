from pathton import Location, Azimuth


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

    @staticmethod
    def keys():
        return 'Latitude', 'Longitude', 'Azimuth'

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

    def __iter__(self):
        yield self.latitude.degrees
        yield self.longitude.degrees
        yield self.azimuth.degrees

    def __getitem__(self, item):
        if item == 0 or item == 'Latitude':
            return float(self.latitude)
        elif item == 1 or item == 'Longitude':
            return float(self.longitude)
        elif item == 2 or item == 'Azimuth':
            return float(self.azimuth)
        else:
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

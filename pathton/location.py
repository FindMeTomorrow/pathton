from pathton import Latitude, Longitude


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
        if abs(latitude_value) > 90 and ((latitude_value + 90) // 180) % 2:
            longitude_value += 180
        return longitude_value

    @staticmethod
    def keys():
        return 'Latitude', 'Longitude'

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

    def __iter__(self):
        yield self.latitude.degrees
        yield self.longitude.degrees

    def __getitem__(self, item):
        if item == 0 or item == 'Latitude':
            return float(self.latitude)
        elif item == 1 or item == 'Longitude':
            return float(self.longitude)
        else:
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

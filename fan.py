class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed: int = SLOW, radius: float = 5.0, color: str = "blue", on: bool = False):
        """Constructor initializing a fan instance with default values."""
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self) -> int:
        return self.__speed

    def get_on(self) -> bool:
        return self.__on

    def get_radius(self) -> float:
        return self.__radius

    def get_color(self) -> str:
        return self.__color

    def set_speed(self, speed: int):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            print("Invalid Speed Selection!")

    def set_on(self, on: bool):
        self.__on = on

    def set_radius(self, radius: float):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be a positive value!")
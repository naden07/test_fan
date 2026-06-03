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

    def set_color(self, color: str):
        self.__color = color

    def display_dashboard(self) -> str:
        """Generates a custom terminal UI status card for the fan instance."""
        RESET = "\033[0m"
        BOLD = "\033[1m"
        CYAN = "\033[36m"
        GREEN = "\033[32m"
        RED = "\033[31m"
        YELLOW = "\033[33m"

        speed_map = {Fan.SLOW: "SLOW", Fan.MEDIUM: "MEDIUM", Fan.FAST: "FAST"}
        speed_text = speed_map.get(self.__speed, "UNKNOWN")

        if self.__on:
            status_badge = f"{GREEN}[ ON - ACTIVE ]{RESET}"
            blade_art = f"{CYAN}// RUNNING // {RESET}"
        else:
            status_badge = f"{RED}[ OFF - IDLE ]{RESET}"
            blade_art = f"{RED}── STOPPED ── {RESET}"

        card = (
            f"┌──────────────────────────────────────┐\n"
            f"│ {BOLD}FAN DEVICE PROFILE{RESET}     {status_badge}   │\n"
            f"├──────────────────────────────────────┤\n"
            f"│  • Speed  : {YELLOW}{speed_text:<24}{RESET} │\n"
            f"│  • Color  : {self.__color.capitalize():<25} │\n"
            f"│  • Radius : {str(self.__radius) + ' units':<25} │\n"
            f"│  • Motor  : {blade_art:<34} │\n"
            f"└──────────────────────────────────────┘"
        )
        return card 
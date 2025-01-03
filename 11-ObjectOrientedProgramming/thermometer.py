import random


class Thermometer:
    fever_temp = 37
    critical_temp = 41
    is_on = False
    temp = None

    def __init__(self, temp_min, temp_max):
        self.temp_range = {"min": temp_min, "max": temp_max}

    def measure(self):
        if not self.is_on:
            return
        self.temp = (
            random.randint(self.temp_range["min"] * 10, self.temp_range["max"] * 10)
            / 10
        )

    def display(self):
        if not self.is_on:
            return
        if self.temp >= self.critical_temp:
            message = "CRITIAL TEMPERATURE!!"
        elif self.temp >= self.fever_temp:
            message = "fever"
        else:
            message = ""
        print(f"{self.temp} {message}")

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


t = Thermometer(32, 42)

t.measure()

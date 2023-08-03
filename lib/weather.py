import random

class Weather():
    def __init__(self):
        self.status = ['rainy', 'stormy', 'sunny']

    def gimme_weather_status(self):
        weather_status = random.choice(self.status)
        return weather_status
    
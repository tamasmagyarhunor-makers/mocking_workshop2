import random

class Weather():
    def __init__(self):
        self.status = ['rainy', 'stormy', 'sunny']

    def gimme_weather_status(self):
        return random.choice(self.status) 
    
    def can_we_go_out_now(self):
        if self.gimme_weather_status() == 'rainy':
            return 'It seems it will rain, please take an umbrella'
        
    def we_can_go_out_now(self):
        if self.gimme_weather_status() == 'sunny':
            return 'It will be sunny'
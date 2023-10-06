import random

class Weather():
    def __init__(self):
        self.status = ['rainy', 'stormy', 'sunny']

    def gimme_weather_status(self): #6
        return random.choice(self.status) #7 -- patch (mock) 
    
    def can_we_go_out_now(self): #4 
        if self.gimme_weather_status() == 'rainy': #5 
            return 'It seems it will rain, please take an umbrella'
        
    def we_can_go_out_now(self):
        if self.gimme_weather_status() == 'sunny':
            return 'It will be sunny'
        
    def get_some_weather_data(self):
        call_to_weather_api = {
            "success": True,
            "data": {
                "city": "London",
                "temperature": "30C"
            }
        }

        return f"Temperature in #{api_response.data.city} is #{api_response.data.temperature}"

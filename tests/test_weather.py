from lib.weather import *
import unittest
from unittest.mock import patch

def test_if_weather_instantiates_with_rainy_sunny():
    weather = Weather()

    actual = weather.status

    expected = ['rainy', 'stormy', 'sunny']

    assert actual == expected

def test_if_we_can_go_out_based_on_weather_rainy():
    weather = Weather() #1 

    with patch('random.choice', return_value='rainy'): #2
        actual = weather.can_we_go_out_now() #3 

    expected = 'It seems it will rain, please take an umbrella'

    assert actual == expected

def test_if_weather_is_sunny():
    weather = Weather()

    with patch('random.choice', return_value='sunny'):
        actual = weather.we_can_go_out_now()

    expected = 'It will be sunny'

    assert actual == expected


def test_weather_api():
    weather = Weather()

    with patch('api.call', return_value={
            "success": True,
            "data": {
                "city": "London",
                "temperature": "30C"
            }}):
        actual = weather.get_some_weather_data()

    expected = 'Temperature in London is 30C'

    assert actual == expected


# def test_gimme_weather_status():
#     weather = Weather()

#     with patch('random.choice', return_value='rainy'):
#         actual = weather.gimme_weather_status()

#     expected = 'rainy'

#     assert actual == expected
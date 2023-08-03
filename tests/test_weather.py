from lib.weather import *
from tests.mock_class import *

def test_if_weather_instantiates_with_rainy_sunny():
    weather = Weather()

    actual = weather.status

    expected = ['rainy', 'stormy', 'sunny']

    assert actual == expected

def test_gimme_weather_status():
    mock_weather = MockClass('Weather')

    actual = mock_weather.mock_method_and_return('gimme_weather_status', 'rainy')

    expected = 'rainy'

    assert actual == expected
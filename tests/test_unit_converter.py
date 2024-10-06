import pytest
from unit_converter import UnitConverter


@pytest.fixture
def converter():
    return UnitConverter()


# Testy dla długości
def test_kilometers_to_miles(converter):
    assert pytest.approx(converter.kilometers_to_miles(10), 0.001) == 6.21371


def test_miles_to_kilometers(converter):
    assert pytest.approx(converter.miles_to_kilometers(10), 0.001) == 16.0934


def test_meters_to_feet(converter):
    assert pytest.approx(converter.meters_to_feet(10), 0.001) == 32.8084


def test_feet_to_meters(converter):
    assert pytest.approx(converter.feet_to_meters(10), 0.001) == 3.048


def test_miles_to_meters(converter):
    assert pytest.approx(converter.miles_to_meters(10), 0.001) == 16093.4


def test_meters_to_miles(converter):
    assert pytest.approx(converter.meters_to_miles(10000), 0.001) == 6.21371


# Testy dla masy
def test_kilograms_to_pounds(converter):
    assert pytest.approx(converter.kilograms_to_pounds(10), 0.001) == 22.0462


def test_pounds_to_kilograms(converter):
    assert pytest.approx(converter.pounds_to_kilograms(22.0462), 0.001) == 10


def test_grams_to_ounces(converter):
    assert pytest.approx(converter.grams_to_ounces(1000), 0.001) == 35.274


def test_ounces_to_grams(converter):
    assert pytest.approx(converter.ounces_to_grams(35.274), 0.001) == 1000


# Testy dla temperatury
def test_celsius_to_fahrenheit(converter):
    assert pytest.approx(converter.celsius_to_fahrenheit(0), 0.001) == 32


def test_fahrenheit_to_celsius(converter):
    assert pytest.approx(converter.fahrenheit_to_celsius(32), 0.001) == 0


# Testy dla prędkości
def test_kilometers_per_hour_to_miles_per_hour(converter):
    assert pytest.approx(converter.kilometers_per_hour_to_miles_per_hour(100), 0.001) == 62.1371


def test_miles_per_hour_to_kilometers_per_hour(converter):
    assert pytest.approx(converter.miles_per_hour_to_kilometers_per_hour(62.1371), 0.001) == 100


# Test ogólny dla nieobsługiwanej konwersji
def test_invalid_conversion(converter):
    result = converter.convert("długość", "mile", "funty", 10)
    assert result == "Konwersja nie jest dostępna"




import unittest
from unit_converter import UnitConverter


class TestUnitConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.converter = UnitConverter()

    # Testy dla długości
    def test_kilometers_to_miles(self):
        self.assertAlmostEqual(self.converter.kilometers_to_miles(10), 6.21371, places=5)

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(self.converter.miles_to_kilometers(10), 16.0934, places=4)

    def test_meters_to_feet(self):
        self.assertAlmostEqual(self.converter.meters_to_feet(10), 32.8084, places=4)

    def test_feet_to_meters(self):
        self.assertAlmostEqual(self.converter.feet_to_meters(10), 3.048, places=3)

    def test_miles_to_meters(self):
        self.assertAlmostEqual(self.converter.miles_to_meters(10), 16093.4, places=1)

    def test_meters_to_miles(self):
        result = self.converter.meters_to_miles(10000)
        print(result)  # Sprawdź wynik
        self.assertAlmostEqual(result, 6.213727366498068, places=5)  # Upewnij się, że używasz prawidłowej wartości

    # Testy dla masy
    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(self.converter.kilograms_to_pounds(10), 22.0462, places=4)

    def test_pounds_to_kilograms(self):
        self.assertAlmostEqual(self.converter.pounds_to_kilograms(22.0462), 10, places=4)

    def test_grams_to_ounces(self):
        self.assertAlmostEqual(self.converter.grams_to_ounces(1000), 35.274, places=3)

    def test_ounces_to_grams(self):
        self.assertAlmostEqual(self.converter.ounces_to_grams(35.274), 1000, places=0)

    # Testy dla temperatury
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(0), 32, places=1)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(32), 0, places=1)

    # Testy dla prędkości
    def test_kilometers_per_hour_to_miles_per_hour(self):
        self.assertAlmostEqual(self.converter.kilometers_per_hour_to_miles_per_hour(100), 62.1371, places=4)

    def test_miles_per_hour_to_kilometers_per_hour(self):
        self.assertAlmostEqual(self.converter.miles_per_hour_to_kilometers_per_hour(62.1371), 100, places=4)

    # Test ogólny dla nieobsługiwanej konwersji
    def test_invalid_conversion(self):
        result = self.converter.convert("długość", "mile", "funty", 10)
        self.assertEqual(result, "Konwersja nie jest dostępna")


if __name__ == '__main__':
    unittest.main()

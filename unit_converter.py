class UnitConverter:
    def __init__(self):
        self.units = {
            "długość": ["kilometry", "mile", "metry", "stopy"],
            "masa": ["kilogramy", "funty", "gramy", "uncje"],
            "temperatura": ["celsjusz", "fahrenheit"],
            "prędkość": ["kilometry_na_godzinę", "mile_na_godzinę"]
        }

    # Konwersje długości
    def kilometers_to_miles(self, km):
        return km * 0.621371

    def miles_to_kilometers(self, miles):
        return miles / 0.621371

    def meters_to_feet(self, meters):
        return meters * 3.28084

    def feet_to_meters(self, feet):
        return feet / 3.28084

    def miles_to_meters(self, miles):
        return miles * 1609.34

    def meters_to_miles(self, meters):
        return meters / 1609.34

    def kilometers_to_meters(self, km):
        return km * 1000

    def meters_to_kilometers(self, meters):
        return meters / 1000

    # Konwersje masy
    def kilograms_to_pounds(self, kg):
        return kg * 2.20462

    def pounds_to_kilograms(self, pounds):
        return pounds / 2.20462

    def grams_to_ounces(self, grams):
        return grams * 0.035274

    def ounces_to_grams(self, ounces):
        return ounces / 0.035274

    # Konwersje temperatury
    def celsius_to_fahrenheit(self, c):
        return (c * 9 / 5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

    # Konwersje prędkości
    def kilometers_per_hour_to_miles_per_hour(self, kph):
        return kph * 0.621371

    def miles_per_hour_to_kilometers_per_hour(self, mph):
        return mph / 0.621371

    # Metoda do wyświetlania dostępnych jednostek
    def show_available_units(self):
        for category, units in self.units.items():
            print(f"{category.capitalize()}: {', '.join(units)}")

    # Główna metoda do konwersji jednostek
    def convert(self, category, from_unit, to_unit, value):
        if category == "długość":
            if from_unit == "kilometry" and to_unit == "mile":
                return self.kilometers_to_miles(value)
            elif from_unit == "mile" and to_unit == "kilometry":
                return self.miles_to_kilometers(value)
            elif from_unit == "metry" and to_unit == "stopy":
                return self.meters_to_feet(value)
            elif from_unit == "stopy" and to_unit == "metry":
                return self.feet_to_meters(value)
            elif from_unit == "mile" and to_unit == "metry":
                return self.miles_to_meters(value)
            elif from_unit == "metry" and to_unit == "mile":
                return self.meters_to_miles(value)
            elif from_unit == "kilometry" and to_unit == "metry":  # Dodany warunek
                return self.kilometers_to_meters(value)
            elif from_unit == "metry" and to_unit == "kilometry":  # Dodany warunek
                return self.meters_to_kilometers(value)

        elif category == "masa":
            if from_unit == "kilogramy" and to_unit == "funty":
                return self.kilograms_to_pounds(value)
            elif from_unit == "funty" and to_unit == "kilogramy":
                return self.pounds_to_kilograms(value)
            elif from_unit == "gramy" and to_unit == "uncje":
                return self.grams_to_ounces(value)
            elif from_unit == "uncje" and to_unit == "gramy":
                return self.ounces_to_grams(value)

        elif category == "temperatura":
            if from_unit == "celsjusz" and to_unit == "fahrenheit":
                return self.celsius_to_fahrenheit(value)
            elif from_unit == "fahrenheit" and to_unit == "celsjusz":
                return self.fahrenheit_to_celsius(value)

        elif category == "prędkość":
            if from_unit == "kilometry_na_godzinę" and to_unit == "mile_na_godzinę":
                return self.kilometers_per_hour_to_miles_per_hour(value)
            elif from_unit == "mile_na_godzinę" and to_unit == "kilometry_na_godzinę":
                return self.miles_per_hour_to_kilometers_per_hour(value)

        return "Konwersja nie jest dostępna"


# Główna funkcja do uruchomienia aplikacji
def main():
    converter = UnitConverter()

    print("Witamy w Konwerterze Jednostek!")
    print("Oto dostępne jednostki do konwersji:")
    converter.show_available_units()

    while True:
        print("\nCo chcesz przekonwertować?")
        category = input("Wybierz kategorię (długość, masa, temperatura, prędkość): ").lower()

        if category not in converter.units:
            print("Niepoprawna kategoria. Spróbuj ponownie.")
            continue

        from_unit = input(
            f"Wprowadź jednostkę, z której chcesz przekonwertować ({', '.join(converter.units[category])}): ").lower()
        to_unit = input(
            f"Wprowadź jednostkę, na którą chcesz przekonwertować ({', '.join(converter.units[category])}): ").lower()

        if from_unit not in converter.units[category] or to_unit not in converter.units[category]:
            print("Niepoprawna jednostka. Spróbuj ponownie.")
            continue

        try:
            value = float(input(f"Wprowadź wartość do konwersji z {from_unit} na {to_unit}: "))
            result = converter.convert(category, from_unit, to_unit, value)
            print(f"Wynik: {value} {from_unit} to {result} {to_unit}\n")
        except ValueError:
            print("Niepoprawna wartość. Wprowadź liczbę.")

        if input("Czy chcesz wykonać kolejną konwersję? (tak/nie): ").lower() != "tak":
            break


if __name__ == "__main__":
    main()

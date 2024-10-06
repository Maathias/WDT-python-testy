# Aplikacja do konwersji jednostek

Aplikacja do konwersji jednostek umożliwia konwersję różnych jednostek długości, masy, temperatury i prędkości. Wspiera konwersje między jednostkami metrycznymi i imperialnymi.

## Spis treści
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Testy](#testy)
- [Przykłady konwersji](#przykłady-konwersji)
- [Licencja](#licencja)

## Instalacja

Aby zainstalować aplikację, wykonaj poniższe kroki:

1. **Klonowanie repozytorium**:
   ```bash
   git clone https://github.com/TwojaNazwaUżytkownika/nazwa-repozytorium.git
   cd nazwa-repozytorium

2. **Utworzenie wirtualnego środowiska (opcjonalne, ale zalecane)**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. **Instalacja zależności**:
   ```bash
    pip install -r requirements.txt

## Użycie
Aby uruchomić aplikację, możesz użyć interfejsu wiersza poleceń lub zaimplementować własne metody konwersji w Pythonie.

1. **Przykładowy kod do użycia**:
   ```bash
    from unit_converter import UnitConverter
    
    converter = UnitConverter()
    
    # Przykład konwersji
    kilometry = 10
    miles = converter.kilometers_to_miles(kilometry)
    print(f"{kilometry} kilometrów to {miles:.5f} mil.")
   
## Testy
Aby uruchomić testy jednostkowe, upewnij się, że masz zainstalowany pytest, a następnie uruchom:

1. **Kod użycia**:
   ```bash
    pytest test_unit_converter.py

2. **Przykładowe testy**:
   ```bash
    import pytest
    from unit_converter import UnitConverter
    
    @pytest.fixture
    def converter():
        return UnitConverter()
    
    def test_kilometers_to_miles(converter):
        assert pytest.approx(converter.kilometers_to_miles(10), 0.001) == 6.21371
    
    def test_miles_to_kilometers(converter):
        assert pytest.approx(converter.miles_to_kilometers(10), 0.001) == 16.0934
    
    # ... inne testy

## Przykłady konwersji
Oto kilka przykładów, jak korzystać z aplikacji do konwersji różnych jednostek:
1. **Długość**:

- Kilometry na mile: `converter.kilometers_to_miles(10)`
- Mile na metry: `converter.miles_to_meters(10)`
2. **Masa**:
- Kilogramy na funty: `converter.kilograms_to_pounds(10)`
- Funty na kilogramy: `converter.pounds_to_kilograms(22.0462)`
3. **Temperatura**:
- Celsjusze na Fahrenheit: `converter.celsius_to_fahrenheit(0)`
- Fahrenheit na Celsjusze: `converter.fahrenheit_to_celsius(32)`
4. **Prędkość**:
- Kilometry na godzinę na mile na godzinę: `converter.kilometers_per_hour_to_miles_per_hour(100)`
- Mile na godzinę na kilometry na godzinę: `converter.miles_per_hour_to_kilometers_per_hour(62.1371)`

## Licencja
Projekt jest objęty licencją MIT. Zobacz plik `LICENSE` w celu uzyskania szczegółowych informacji.


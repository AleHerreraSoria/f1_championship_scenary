# test_scenario.py

# Importa la función desde tu script principal
# Nota: Si el script principal se llama 'f1_scenario_calculator.py',
# el nombre de importación es 'f1_scenario_calculator'
from f1_scenario_calculator import calculate_f1_scenario

def test_calculate_f1_scenario_returns_data():
    """Verifica que la función se ejecuta y devuelve resultados válidos (no vacíos)."""
    
    # Ejecuta la función principal
    results = calculate_f1_scenario()
    
    # 1. Asegura que el resultado es un diccionario
    assert isinstance(results, dict)
    
    # 2. Asegura que el diccionario contiene los 3 pilotos
    assert 'Norris' in results
    assert 'Verstappen' in results
    assert 'Piastri' in results
    
    # 3. Asegura que al menos un piloto tiene escenarios de victoria (la lista no está vacía)
    # (En un escenario realista, siempre debería haber escenarios para al menos dos pilotos)
    total_scenarios = sum(len(scenarios) for scenarios in results.values())
    assert total_scenarios > 0
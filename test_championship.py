# test_scenario.py

# Importa la función desde tu script principal, ahora llamado 'championship.py'
from championship import calculate_f1_scenario

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
    
    # 3. Asegura que al menos un piloto tiene escenarios de victoria
    # (El número total de escenarios debe ser mayor que cero)
    total_scenarios = sum(len(scenarios) for scenarios in results.values())
    assert total_scenarios > 0
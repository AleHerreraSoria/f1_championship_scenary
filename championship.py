import itertools
import pandas as pd

# Definición global pilotos
drivers = ["Norris", "Verstappen", "Piastri"]


def calculate_f1_scenario():
    # Puntos iniciales
    initial_points = {"Norris": 408, "Verstappen": 396, "Piastri": 392}

    # Puntos por posición (1-10)
    pos_points = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

    # Posiciones posibles: 1-10 (con puntos) y 11 (representa 11th o DNF, 0 puntos)
    # 11 se usa como marcador para todas las posiciones sin puntos (11-20, DNF)
    ranks_set = list(range(1, 11)) + [11]

    # Almacenar los resultados
    winning_scenarios = {driver: [] for driver in drivers}

    # Combinatoria: Itera sobre todas las combinaciones posibles (11^3 = 1331 combinaciones)
    for R_N, R_M, R_O in itertools.product(ranks_set, repeat=3):
        ranks = {"Norris": R_N, "Verstappen": R_M, "Piastri": R_O}

        # --- 1. Condición de Legalidad ---
        # Si dos o más pilotos terminan en el top 10, sus posiciones deben ser únicas.
        scoring_ranks = []
        for driver in drivers:
            if ranks[driver] <= 10:
                scoring_ranks.append(ranks[driver])

        # Si hay duplicados en posiciones con puntos, la combinación no es legal (ej. dos pilotos en 1er lugar)
        if len(scoring_ranks) != len(set(scoring_ranks)):
            continue

        # --- 2. Calcular Puntuación Final ---
        final_scores = {}
        for driver in drivers:
            rank = ranks[driver]
            # Obtener puntos (0 si el rank es 11)
            points = pos_points.get(rank, 0)
            final_scores[driver] = initial_points[driver] + points

        # --- 3. Determinar el Ganador ---
        max_score = max(final_scores.values())
        potential_winners = [
            d for d, score in final_scores.items() if score == max_score
        ]

        # Si hay un único ganador (sin empate)
        if len(potential_winners) == 1:
            winner = potential_winners[0]

            # --- 4. Almacenar Resultado ---
            # Reemplazar 11 por '11+' para mejor visualización
            formatted_ranks = {}
            for d in drivers:
                formatted_ranks[d] = str(ranks[d]) if ranks[d] <= 10 else "11+"

            # Guardamos el escenario completo
            scenario = {
                "Pos_Norris": formatted_ranks["Norris"],
                "Pos_Verstappen": formatted_ranks["Verstappen"],
                "Pos_Piastri": formatted_ranks["Piastri"],
                "Ptos_Norris": final_scores["Norris"],
                "Ptos_Verstappen": final_scores["Verstappen"],
                "Ptos_Piastri": final_scores["Piastri"],
            }
            winning_scenarios[winner].append(scenario)

    return winning_scenarios


# Ejecutar el cálculo
results = calculate_f1_scenario()

# Crear DataFrames para cada ganador y guardar los archivos CSV
for winner, scenarios in results.items():
    df = pd.DataFrame(scenarios)

    # Seleccionar y reordenar columnas para mejor lectura
    cols_pos = [f"Pos_{d}" for d in drivers]
    cols_pts = [f"Ptos_{d}" for d in drivers]
    df = df[cols_pos + cols_pts]

    file_name = f"Escenarios_Campeon_{winner}.csv"
    df.to_csv(file_name, index=False)

    # (En la ejecución anterior, se mostró un mensaje limitando la vista
    # a 50 filas para evitar archivos muy grandes en la respuesta.)

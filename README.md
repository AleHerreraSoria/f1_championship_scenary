# 🏎️ F1 Championship Scenario Calculator

Este repositorio contiene un script de Python diseñado para calcular **todos los escenarios posibles** de la última carrera de la temporada que resultan en la victoria del campeonato para uno de los tres pilotos contendientes.

---

## 🎯 Razón de Ser

El script `f1_scenario_calculator.py` realiza una **combinatoria exhaustiva** de las posiciones de carrera (1° a 10°, más 11+ para las posiciones sin puntos) para los pilotos **Norris, Verstappen, y Piastri**.

Su objetivo principal es:

* **Simular** cada resultado de carrera válido para estos tres pilotos.
* **Determinar** el puntaje final del campeonato para cada uno.
* **Identificar** los escenarios de carrera específicos (posiciones) que conducen a que un piloto se corone **campeón indiscutible**.

## ⚙️ Resultados

El script genera archivos CSV separados (ej., `Escenarios_Campeon_Norris.csv`, `Escenarios_Campeon_Verstappen.csv`, etc.), donde cada fila representa una combinación de resultados de carrera que garantiza el título para el piloto en cuestión.

| Columna | Descripción |
| :--- | :--- |
| `Pos_Piloto` | Posición final del piloto en la carrera (1 a 10, o `11+`). |
| `Ptos_Piloto` | Puntaje total final del piloto en el campeonato. |

---

## 🛠️ Requerimientos

El script utiliza las librerías estándar de Python, además de:

* `pandas`
* `itertools`

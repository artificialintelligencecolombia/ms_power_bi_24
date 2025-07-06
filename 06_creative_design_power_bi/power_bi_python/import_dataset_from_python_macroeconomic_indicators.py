import pandas as pd

# Step 1: Define macroeconomic indicators
data = {
    '2020': [1.61, 1.75, -7.19],
    '2021': [5.62, 3.00, 10.80],
    '2022': [13.12, 12.00, 7.29],
    '2023': [9.28, 13.25, 0.61],
    '2024': [5.20, 9.25, 1.70]
}

# Step 2: Set row labels as indicators
indicators = [
    'Inflation Rate (%)',
    'Interest Rate (%)',
    'GDP Growth Rate (%)'
]

# Step 3: Create the transposed DataFrame
df = pd.DataFrame(data, index=indicators)

# Step 4: Export to CSV for use in Excel or Power BI
csv_path = 'macroeconomic_indicators_colombia_transposed.csv'
df.to_csv(csv_path)

# Export to CSV
csv_path = 'macroeconomic_indicators_colombia_2020_2024.csv'
df.to_csv(csv_path, index=False)

print(f"Dataset saved to {csv_path}")



# The top 3 macroeconomic indicators:
#
# 1. Inflation Rate (IPC - Índice de Precios al Consumidor)
#    - Signals cost of living and monetary policy direction.
#    - Source: DANE.
#
# 2. Interest Rate (Tasa de Intervención del Banco de la República)
#    - Influences credit, investment, and inflation control.
#    - Source: Banco de la República.
#
# 3. GDP Growth Rate (Producto Interno Bruto - PIB)
#    - Measures economic activity and national output.
#    - Source: DANE, Banco de la República.

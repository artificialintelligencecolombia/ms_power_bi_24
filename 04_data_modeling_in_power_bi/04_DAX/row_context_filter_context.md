# Row context and Filter context 

### Row context
Eefers to the current row when evaluating a calculated column or a row-level calculation. Think of it as evaluating one row at a time, with access to values in other columns of that same row

```
Revenue = Sales[Quantity] * Sales[UnitPrice]
// For each row, DAX multiplies the Quantity and UnitPrice values from the same row
```

### Filter context
El contexto de filtro en DAX es el conjunto de restricciones que determinan qué filas de datos están disponibles para un cálculo en un momento específico.
```
North Sales 2023 = 
CALCULATE(
    SUM(Sales[Amount]),
    Region[RegionName] = "North",
    'Calendar'[Year] = 2023
)
```

DAX always applies the filter and then it calculates the row-level calculation
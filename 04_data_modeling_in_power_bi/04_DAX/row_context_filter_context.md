# Row context and Filter context 

### Row context
- Evaluates each row independently
Refers to the current row when evaluating a calculated column or a row-level calculation. Think of it as evaluating one row at a time, with access to values in other columns of that same row

```
Revenue = Sales[Quantity] * Sales[UnitPrice]
// For each row, DAX multiplies the Quantity and UnitPrice values from the same row
```

For each row in the Sales table, this formula calculates Total Price using the values from that row.

Calculated columns rely on row context

### Filter context
Represents all active filters in a report, measure, or query
```
North Sales 2023 = 
CALCULATE(
    SUM(Sales[Amount]),
    Region[RegionName] = "North",
    'Calendar'[Year] = 2023
)
```

DAX always applies the filter and then it calculates the row-level calculation

Measures rely on filter context
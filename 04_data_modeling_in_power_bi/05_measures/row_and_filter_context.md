# Row context and filter context

### Row context
Exists inside iterators like SUMX, AVERAGEX, COUNTAX.
Think of it as a row-by-row evaluation in a table.
Used when calculating values per row before aggregating.

```
Total Revenue = SUMX(Sales, Sales[Quantity] * Sales[Unit Price])
// Calculating total revenue per row before summing it. SUMX loops through each row, multiplies Quantity * Unit Price, and sums the results.
```
### Filter context
Comes from filters applied to visuals, slicers, or CALCULATE().
Controls what data is included in the calculation.

```
Sales 2023 = CALCULATE(SUM(Sales[Amount]), Sales[Year] = 2023)
// Showing total sales only for 2023. CALCULATE modifies the filter context, so only 2023 data is used.
```

 **Pro Tip:** CALCULATE can override filter context and transform row context into filter context! 🔥
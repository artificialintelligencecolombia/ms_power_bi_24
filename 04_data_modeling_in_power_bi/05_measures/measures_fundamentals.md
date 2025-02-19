# Measures
1. Measures perform calculations on data model fields.
2. Used in data visualizations (charts, tables, cards).
3. Essential for data analysis and interpretation.
4. Dynamic calculations update based on filters and interactions.
5. Measures can be used to calculate KPIs.

### Benefits of measures
- Dynamic Calculation: Adjusts based on report context.
- Reusability: Use the same measure across reports.
- Performance Optimization: Faster and more efficient than calculated columns.
- Consistency: Ensures uniform calculations across reports.
- KPI Creation: Used to monitor business performance against targets.

### Common measure functions in DAX
- SUM([Column]) → Total of a numeric column.
- AVERAGE([Column]) → Mean value of a column.
- MIN([Column]) → Smallest value in a column.
- MAX([Column]) → Largest value in a column.
- COUNT([Column]) → Counts non-blank values.
- COUNTROWS(Table) → Counts rows in a table.
- CALCULATE(Expression, Filters...) → Applies filters dynamically.
- DIVIDE(Numerator, Denominator, AlternateResult) → Safe division handling

#### Advanced measure techniques
- Time Intelligence: TOTALYTD(), TOTALMTD(), PREVIOUSYEAR()
- Filter Manipulation: ALL(), ALLEXCEPT(), KEEPFILTERS().
- Conditional Logic: IF(), SWITCH(), BLANK() handling.
- Rolling Averages & Moving Totals: AVERAGEX(), SUMX(), DATESINPERIOD()

### Best Practices for Measures
- Use measures instead of calculated columns for aggregations.
- Optimize DAX expressions for performance.
- Use variables (VAR) for readability and efficiency.
- Leverage CALCULATE() for complex filtering scenarios.
- Avoid using SUMX() and FILTER() on large datasets unless necessary.

**NOTE:** 
- measures in Power BI always return a single value.
- measure can be use to create calculated tables from precalculated measures

### Types of measures
1. Additive
These can be added up across all dimensions. Works whether summing by day, month, region, or product.

Example: If you sold $100 on Monday and $200 on Tuesday, the total for both days is $300.

```
Total Sales = SUM(Sales[Amount])
```

2. Semi-Additive
You can sum them across some dimensions, but NOT over time.

🔹 Example: Bank Balance
Imagine your account balance is:

January 1st: $1,000
February 1st: $2,000
Summing balances over time (Jan + Feb) doesn't make sense because it's a snapshot.


3. Non additive
Ratios, Percentages, and Distinct Counts cannot be summed. You cannot sum them at all because the result wouldn’t make sense.

If a product has a 20% margin in January and 30% in February, the total margin is not 50%! Instead, we use an average or weighted formula.

```
Profit Margin = SUM(Profit) / SUM(Revenue)
```
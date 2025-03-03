# Calculated columns
- We can generate new data by combining existing columns to create a new calculated column.
- Add new columns to the existing table than can be added to the data model
- The formula must return a scalar value, and it's evaluated for each row in the table

```
Total Sales = 
'Sales'[Quantity] * 'Sales'[UnitPrice]
```
**NOTE:** new calculated columns can be used to report and visualizations
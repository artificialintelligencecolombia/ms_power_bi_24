# Calculated table
Previous to create or clone tables, analyze the data model

### Cloned tables
Cloning a table means duplicating the original table. The cloned table inherits all the original table's columns, data, and relationships. A cloned table is useful if you want to perform manipulations or analysis on data while preserving the original records.
```
Cloned_table_name = ALL(Original_table_name)
```

### Calculated table
they are created based on calculations, transformations, or aggregations performed on existing data. For instance, you can create a calculated table showing each bicycle model's total sales.

**NOTE**: new tables wont be connected to existing tables

### Real-World applications of calculated tables
1. Profitability Analysis:  you can draw insights into gross margins, net profits, and profit margins. This helps organizations identify their most profitable products, categories, services, and customer segments.

2. Customer Segmentation:  You can create a calculated table with DAX to facilitate customer segmentation based on transaction history. This helps businesses to tailor their marketing strategies for each customer segment.

3. Time Intelligence Analysis: A date table is one of the most common tables that can be created using various methods in Power BI. One method of creating a date table is using the DAX function CALENDER. For example, a company can record several date columns in their dataset, like order date or shipping date. The calculated table can then analyze the data using time intelligence built-in DAX functions like TOTALYTD, year-to-date, month-to-date, and so on.

4. Budgeting and Forecasting: By defining a calculated table in DAX for budget allocation and integrating it with historical data, you can perform variance analysis and make data-driven forecasts for future periods.


### Best practices for creating calculated tables with DAX
- Use Variables
Using variables is an excellent way to enhance formula readability. Variables are recommended wherever you need to write a complex expression. By defining variables, you can avoid repeating the same expression. 

```
Sales YoY Growth % = 
DIVIDE (( 
    [Sales] - CALCULATE ( [Sales], 
    PARALLELPERIOD ( 'Date'[Date], -12, MONTH ) )), 
    CALCULATE ( [Sales], 
    PARALLELPERIOD ( 'Date'[Date], -12, MONTH ) ))
    // The above formula uses the PARALLELPERIOD function to compute the year-over-year growth rate of the company.
```

#### CORRECT:
```
Sales YoY Growth % = VAR SalesPriorYear = 
CALCULATE ( [Sales], 
PARALLELPERIOD ( 'Date'[Date], -12, MONTH ) )
RETURN 
DIVIDE ( ( [Sales] - SalesPriorYear ), SalesPriorYear )
//This formula repeats the expression same period last year. It can be made more efficient by introducing a variable called SalesPriorYear
```

- Format DAX syntax
Formatting DAX formulas and expressions is crucial for maintaining consistency and readability. When working in a team, format your syntax to enhance comprehension and simplify troubleshooting. For example, consider the following syntax: 

```
Total Revenue = CALCULATE(SUM(Sales[Revenue]), 
FILTER
(Sales, Sales[OrderDate]=2018 
&& 
Sales[Product Color]="Blue"))
// The above DAX expression calculates the total sales of blue-colored products for 2018.
// The syntax is complex. It contains many arguments and is hard to comprehend. 
```

```
Total Revenue =
CALCULATE 
( SUM ( Sales[Revenue] ),
FILTER ( Sales, Sales[OrderDate] = 2018 
&& 
Sales[Product Color] = "Blue" ))
// Formatted syntax
```

- Test and Validate
Always test and validate your calculated tables to ensure they produce the desired results.
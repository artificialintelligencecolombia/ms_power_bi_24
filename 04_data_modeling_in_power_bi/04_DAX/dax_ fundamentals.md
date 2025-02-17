# DAX Fudamentals
DAX (Data Analysis Expressions) is a formula language used in Power BI, Excel, and Microsoft SQL Server Analysis Services to create custom calculations in data models to generate new data and extract relevant insights.
It creates additional information from existing data.

### DAX Fundamentals
- Syntax
- Data types
- Operators
- Functions
- Column and table references

### DAX Syntax
```
Total Products Sold = SUM('Sales'[Quantity])
```
    |                   |     |             |
Calculated column  Function Table Reference Column Reference
* This DAX formula adds a new column to the existing table

### Data Types
DAX can perform computations on different data types, which include the following:
- Text (Binary): "Hello, world".
- Decimal (Float): 1.23.
- Whole number (Integer): 123.
- Boolean: TRUE or FALSE.
- Date (Date/Time): DATE(2023,5,11).
- Currency: A fixed decimal number.


### Operators
Ther are uused to:
- Perform arithmetic operations
- Compare values
- Work with strings
- Test conditions

Parenthesis(): (5+7) * 5      
Arithmetic +,-,*,/, ^: 18/3 = 6
Logical &&, ||: [Region] = "USA" && [Quantity] > 5
Comparison =, <>, >, >=, <, <=: [Quantity] <= 5
Text Concatenation &: [Region] & ", " & [City]

```
Total Revenue = SUMX('Sales'[Quantity] * 'Sales'[Unit Price])
```

### Functions and formulas
Perform calculations to create new data
Syntax: FUNCTIONANME()

#### CALCULATE
CALCULATE = Perform a calculation + Apply a filter

```
//Evaulates SUM(Sales[Amount]) by applying a filter to the Sales[Region] column
CALCULATE(SUM(Sales[Amount]), Sales[Region] = "West")
```

#### AVERAGEX
calculates the average of an expression evaluated row by row over a table, then it divides the total sum by the count of rows.

```
AVERAGEX(Sales, Sales[Amount])
```

#### SUMMARIZE
creates a summary table based on specified group of columns and optional aggregations.

```
SUMMARIZE(
    Sales, 
    Sales[Region], 
    Sales[Category], 
    "Total Sales", SUM(Sales[Amount])
)
// Groups sales by Region and Category, and calculates Total Sales
```

### Variables
Are used to calculate complex calculations, variables are used to store intermediate results that will be used in the final calculation.

```
// Calculate the weighted sum of column_1 * column_2
VAR variable_1 =
    SUMX(table_name, table_name[column_1] * 
    table_name[column_2])

// Count the distinct values in key_column
VAR variable_2 =
    DISTINCTCOUNT(table_name[key_column])

// Divide the weighted sum by the distinct count (avoiding division by zero)
// The result is the weighted averaage
RETURN
DIVIDE(variable_1, variable_2)
```

### DAX best practices
- Start with simple calculations
- Increase complexity gradually
- Understand the model and its relationships
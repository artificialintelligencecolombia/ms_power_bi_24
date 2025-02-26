# Filter functions
- Filter functions in DAX are used within the CALCULATE function to modify filter contexts and refine data analysis in Power BI. 
- These functions allow users to apply conditions to tables and columns to extract more specific insights.

### Boolean Filter Expressions
Evaluate conditions as either TRUE or FALSE.

```
Sales of high-end products =
CALCULATE(
    SUM(Sales[Total Sales]),
    FILTER(Products, Products[Unit Price] >= 500) // This filters products with a unit price of $500 or more.
)
```

### Table Filter Expressions
- Use entire tables or table functions to define filters.
- Suitable for complex filtering conditions.

```
2019 Sales in Germany =
CALCULATE(
    SUM([Total Sales]),
    FILTER(Region, Region[Country] = "Germany"),
    FILTER(Date, Date[Year] = "2019") // This filters sales data to only Germany in 2019
)
```

### Filter Modification Functions
Filter modification functions allow reusability and prevent redundant DAX code.

#### REMOVEFILTERS
Clears filters from specified columns or tables.

```
Total Sales = 
CALCULATE([Total Sales], REMOVEFILTERS(Product), REMOVEFILTERS(Region))
```

#### KEEPFILTERS
Adds a filter while keeping existing filters active.

```
Blue Products Sale = 
CALCULATE([Total Sales], KEEPFILTERS(Products[Color] = "Blue"))
```

#### ALL Functions (ALL, ALLEXCEPT, ALLSELECTED, ALLNOBLANKROW)
Remove filters from specific or all columns of a table.

```
Total Sales = 
CALCULATE([Total Sales], ALL(Product), ALL(Region)) // Ignores filters applied to Product and Region.
```

#### CROSSFILTER
Modifies relationships between tables, changing filter direction or disabling it.

```
Product by Year =
CALCULATE(
    DISTINCTCOUNT(Products[ProductKey]),
    CROSSFILTER(Sales[ProductKey], Products[ProductKey], BOTH)
)
```

#### USERELATIONSHIP
Activates an inactive relationship between tables.
Useful when multiple relationships exist but only one is active by default.

### Points to remember
1. Making Use of Logical Operators

#### AND (&&) → All conditions must be true for the filter to apply.
```
CALCULATE(
    SUM(Sales[Total Sales]),
    Products[Category] = "Electronics" && Sales[Year] = 2023 // ✅ Only sums sales where Category = "Electronics" AND Year = 2023.
)
```

#### OR (||) → At least one condition must be true for the filter to apply.
```
CALCULATE(
    SUM(Sales[Total Sales]),
    Products[Category] = "Electronics" || Sales[Year] = 2023 // ✅ Sums sales where Category = "Electronics" OR Year = 2023.
)
```
The choice of operator depends on whether you need strict conditions (AND) or flexible conditions (OR).

2. ALL Filter Modification Functions
#### ALL, ALLEXCEPT, ALLSELECTED, and ALLNOBLANKROW modify filters but can also return a table.
Example: Removing all filters from Region while keeping others:
```
CALCULATE(
    SUM(Sales[Total Sales]),
    ALL(Region) // ✅ Ignores region filters but keeps other filters.
)
```

3. CALCULATE Filter Results as Virtual Tables
Filters inside CALCULATE always return a virtual table, reducing rows dynamically.
Example: Filtering sales where Product[Price] >= 500:

```
CALCULATE(
    SUM(Sales[Total Sales]),
    FILTER(Products, Products[Price] >= 500) // ✅ The FILTER function creates a temporary table with only products priced ≥ $500, which is then used in CALCULATE.
)
```
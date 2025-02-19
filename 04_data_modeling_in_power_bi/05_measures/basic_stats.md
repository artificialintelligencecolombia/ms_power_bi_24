# Basic statistical functions
- Statistical functions calculate values related to statistical distributions and probability. 
- They allow to perform calculations and comparisons that reveal meaningful information about the data.

- They're used for quantitative analysis. These are AVERAGE, MEDIAN, COUNT, DISTINCTCOUNT, MIN, and MAX. 

### AVERAGE
Frequently used to identify a central tendency in a dataset. Ignores blanks, text, and logical values.
```
Avg. Of Quantities Sold = AVERAGE (Sales [Quantity])
```
### AVERAGEX
Calculates an average over an expression by iterating through a table row by row.
Used when the values don’t exist directly in a column but must be calculated.

```
AVERAGEX(Sales, Sales[Quantity] * Sales[Unit Price])
// Calculates total value per sale (Quantity * Unit Price). Then finds the average of those values.
```

### AVERAGEA
Includes logical values (TRUE = 1, FALSE = 0) and text (0).

```
AVERAGEA({TRUE, FALSE, 5, 3})
// Result: (1 + 0 + 5 + 3) / 4 = 2.25
```

### MEDIAN
Calculates the middle value in a set of numbers. It sorts the numbers in ascending order and then selects the middle number

Unlike the average, the median is less affected by outliers and extreme values. This means that it’s useful for datasets with skewed distributions. Only numeric data types are supported in this function. Dates, logical values, and text columns are not supported.

```
Median Customer Age = MEDIAN(Customers [Age])
```

### COUNT
The COUNT function counts the number of rows in a column or a table. It is often used to measure the size of a dataset. You can use it to count all or only rows meeting specific criteria.

```
Number of Customers = COUNT([CustomerID])
```

### COUNTA
Count the number of cells in a column that are not empty. It counts rows containing numeric and non-blank values, including text, dates, and logical values.

```
= COUNTA ('Reseller' [Phone])
```

### COUNTAX
Counts the number of non-blank results when evaluating an expression row by row.
Example: Counting Customers Who Made a Purchase

```
COUNTAX(Sales, Sales[Amount])
// Only counts rows where Sales[Amount] is not blank. Useful when some transactions might have missing values.
```

### COUNTBLANK
This function counts the number of blank cells in a column

```
= COUNTBLANK (Reseller [BankName])
```

### COUNTROWS
Counts the number of rows in the specified table or a table defined by an expression.

```
= COUNTROWS([‘Orders’])
```

### DISTINCTCOUNT
Counts the number of distinct values in a dataset. This function is helpful when you need to understand the count of unique values or categories. 

The only argument allowed for this function is a column. You can use columns containing any type of data. 

```
Number of distinct Customers = DISTINCTCOUNT([CustomerID])
```

### MIN
identify the smallest values in a column or between two scalar expressions. These values provide an overview of the range of your data.

Minimum Reseller Margin =MIN([Reseller Margin])

### MINA
Works like MIN but treats TRUE as 1 and FALSE as 0 in logical columns.

```
MINA(Products[InStock])
// If InStock has {TRUE, FALSE, 5, 3}, it returns 0 (since FALSE = 0)
```

### MINX
Evaluates an expression row by row and returns the minimum result.
Used for complex calculations across related tables.

```
MINX(Sales, Sales[Quantity] * Sales[Unit Price])
```

### MAX
Identify the largest value in a column or the larger value between two scalar expressions. The MIN and MAX functions can provide an overview of the range of your data. 

```
Max Sales Amount = MAX (Sales [Sales Amount])
```

### MAXX
MAXX iterates over a table and returns the maximum of an expression.
Useful when working with row context.

```
MAXX(Sales, Sales[Quantity] * Sales[Unit Price])
Finds the largest total sale per row.
```
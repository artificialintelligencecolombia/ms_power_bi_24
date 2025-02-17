# DAX table functions
DAX provides many functions for creating additional information about tables within a data model. To master DAX, you must be able to create and manipulate calculated tables.

### Table manipulation functions
When creating calculated tables to solve analytical problems, include the relevant DAX table function in your syntax.

### DISTINCT function
This function returns a table by removing duplicate rows from another table and returning distinct data only. 

```
= DISTINCT (Store [Store Name])
// Store is the table name within the dataset, and Store Name is the column name.
```

### VALUES function
When the input parameter is a column name, this function returns a one-column table that contains distinct values from the specified column. Duplicate values are removed, and unique values are returned. When the input parameter is a table name, it returns the rows from the specified table.

```
= VALUES (Store [Store Name])
// determine its total number of individual stores
// Store is the table name within the dataset, and Store Name is the column name. VALUES includes the blank row, while DISTINCT does not return the blank row.
```

### UNION
The UNION function returns the union (join) of two tables whose columns match. However, the tables must have the same number of columns. 

Example:

For example, Adventure Works must combine its international and US-based inventory data. They can use the UNION function to combine these tables as one:

```
= UNION (InventoryUS, InventoryInt)
// combine international and US-based inventory tables as one
```

### CALENDAR
The CALENDAR function is useful for creating a date table in the data model. It returns a table with a Date column containing a contiguous set of dates. The range of dates is from the specified start date to the specified end date, including those two dates.

Example:
The Adventure Works data model contains no date table. However, there is a date column in the sales table. So, the solution is to create a calculated date table using the CALENDAR function. You just need to provide the start and end dates for the table.

```
= CALENDAR (DATE (2015, 1, 1), DATE (2021, 12, 31))
```

### CALENDARAUTO
The CALENDARAUTO function returns a table with a column named Date containing a contiguous set of dates. The range of dates is calculated automatically based on the data available in the model.

In this case, your calculated date table will extract the start and end date information from the older date column of the sales table.

## Further table manipulation functions
These functions return a table or manipulate existing tables.

### ADDCOLUMNS
Adds calculated columns to the given table or table expression.

(<table>, <name>, <expression>[, <name>, <expression>]…)

### FILTERS
Returns the values that are directly applied as filters to columnName.

(<columnName>)

### TOPN
Returns the top N rows of the specified table. 

(<N_Value>, <Table>, <OrderBy_Expression>, [<Order>[, <OrderBy_Expression>, [<Order>]]…])

### UNION
Creates a union (join) table from a pair of tables.

(<table_expression1>, <table_expression2> [,<table_expression>]…)

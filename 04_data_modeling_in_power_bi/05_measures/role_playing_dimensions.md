# Role playing dimensions
- a role-playing dimension is a single dimension table that can be referenced multiple times in a fact table for different purposes (or "roles")
- A role-playing dimension is a dimension table that is used multiple times within a data model, linking to different columns in a fact table, each representing a different context (or "role") of the same dimension.

i.e.

Sales                       Date
[Order Date]_______________ [Date]
[Shipping Date]. . . . . . .

- In this example, the Date table is used twice in the Sales table, once for the order date and once for the shipping date.
- This is a common scenario in data modeling, and it's called a role-playing dimension.

___   ACTIVE relationship
. . . inactive relationship

If we want to analyze total Sales from "Shipping date" perspective we use DAX, an inactive relationship, and the USERELATIONSHIP function.

```
Total Sales (Shipping date) =
CALCULATE( 
    SUM(Sales[Amount]), / Calculates the total sales column from Sales table
    USERELATIONSHIP(Sales[Shipping Date], 'Date'[Date]) //establishes a temporary relationship
)
```

### USERELATIONSHIP Funtion
- Forces the use of an inactive relationship
- Enables to perform analysis using different relationships between tables without affecting the overall structure of the data model.

- USERELATIONSHIP(Table1[Column1], Table2[Column2])
- It doesnt return value, but modifies the context of a calculation.

**NOTE**: To make use of USERELATIONSHIP, the relationship must be defined in the model, with the active and inactive relationship.
# Snowflake schema
Is a database design that optimizes storage and retrieval by normalizing the data

FACT TABLE <-- DIMENSION TABLE <-- Related TABLE

### Advantages of snowflake schema
- Simplifies dimension tables by normalizing the data
- Reduces redundancy and improves data integrity
- Enhances data analysis
- Imporves data governance

### Building a snowflake schema
1. Disable auto-detect: when multiple tables are loaded, Power BI automatically detects relationships between tables. This can be disabled in the Power BI options
Options and settings -> Data load (CURRENT FILE section) -> uncheck 'Auto detect new relationships after data is loaded' option -> OK
2. Load data from data sources (excel, database, etc.): fact and dimension AND related tables are loaded
3. Create relationship between fact and dimension tables (manually): this can be done by manage relationships section
3. Create relationship between dimension and related tables (manually): this can be done by manage relationships section

### Transitioning from star schema to snowflake schema
1. Open the power bi project that contains the star schema
2. Normalize the (necessary) dimension tables by creating new tables (using DAX)
3. Create relationships between the normalized dimension tables 

### Two methods of normalizing
1. GROUPBY
2. DISTINCT + SELECTCOLUMNS

#### 1. Groupby
```DAX
Category = GROUPBY('Table_Product', 'Table_Product'[CategoryID], 'Table_Product'[Category])
```
#### Components:
- Table_Product: The source table.
- Table_Product[Category ID], Table_Product[Category]: Columns used for grouping.

#### Features:
- Returns a virtual table (not physically stored).
- Groups Table_Product by Category ID and Category, keeping only distinct values.
- Does not allow aggregations (e.g., sum, average).
- Needs to be wrapped inside another function like ADDCOLUMNS to add calculations.

#### 2. Distinct + Selectcolumns
```DAX
Category_Dim = DISTINCT ( 
    SELECTCOLUMNS ( 
        Table_Product, 
        "Category ID", Table_Product[Category ID], 
        "Category", Table_Product[Category] 
    ) 
)
```
#### Components:
- SELECTCOLUMNS ( Table, "NewColumnName1", Column1, "NewColumnName2", Column2 )
    - Table_Product: Source table.
    - "Category ID", Table_Product[Category ID]: Creates a column named "Category ID" from Table_Product[Category ID].
    - "Category", Table_Product[Category]: Creates a column named "Category" from Table_Product[Category].
- DISTINCT (Table): Removes duplicate rows from the table created by SELECTCOLUMNS.

#### Features:
- Creates a physical table stored in the data model.
- Ensures only unique values for Category ID and Category.
- More efficient for a snowflake schema where Category is a separate dimension.

#### Conclusion
1. If you're restructuring your model for snowflake schema, use DISTINCT + SELECTCOLUMNS because it creates a physical table you can relate to Table_Product.
2. GROUPBY is better for temporary calculations, but it's not ideal for dimension tables.

### Data model redesign process
1. Normalize dimension tables
2. Create new tables
3. Stablish cardinality (relationships) between tables
4. Create hierarchies
5. Compute custom calculations using DAX
7. Test and validate
8. Document the changes
9. Transform and validate data
10. Optimize the model
11. Implement the model
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

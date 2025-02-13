# Star Schema

### Building a star schema
The process to configuring a star schema is:
1. Disable auto-detect: when multiple tables are loaded, Power BI automatically detects relationships between tables. This can be disabled in the Power BI options
Options and settings -> Data load (CURRENT FILE section) -> uncheck 'Auto detect new relationships after data is loaded' option -> OK
2. Load data from data sources (excel, database, etc.): fact and dimension tables are loaded
(same data loading process through the connectors) -> now tables are visible in model view
3. Create relationship between tables (manually): this can be done by manage relationships section
Model view -> drag column with shared keys between tables from one table to another
4. Setting up the cardinality and cross-filter direction between tables. this will define how the tables relate to each other and determine the pathway of filtering
Manage relationship -> new -> build the relationships by selecting the tables and the shared key columns -> select the cardinality and cross-filter direction -> NOTE: make sure I understand the implications of bi-directional filtering -> OK
# LOAD
Its composed of the following tasks:
- Accessing data sources
- Establish connections
- Extract data
- Transform operations

### Where is LOAD (ETL step) located in Power Bi?
**LOAD**:
- data loaded directly
- data can be transformed in a later stages

**TRANSFORM**:
- transform data before loading it
- Changes are applied to data model

Loading time depends of the size of the data and the complexity of the transformations.

### Data staging
A staging area is an intermediate storage location during the data processing (ETL) for raw, unprocessed data 

Data        ->  Staging area       ->  Data warehouse
(Raw data)     (ETL Operations)     (Data warehouse, data marts, repositories)

Home Ribbon -> Load data from sources -> Power query -> Go to queries tab -> Right click -> Create a new group -> Name it 'Staging Area' -> Drag and drop the queries into the group -> Roght click respectively -> Disable the 'load' by clicking the checkbox 'Enable load' -> Keep activated 'Include in report refresh' -> Click 'Close & Apply'

This way both tables will still be used in queries but they won't be loaded into the data model.

In the ETL process, data can be stored in a staging area which is a temporary storage

### End-to-end ETL Process
1. Extract (various sources | identify errors, inconsistencies)
- Several columns contain errors.
- Some columns contain null values.
- The Product ID in some columns appears as if it was duplicated repeatedly.
- A column called Order Status only contains numerals.
- A single full name column has combined names and surnames.

2. Transform (clean, filter, merge, aggregate, etc)
- Tables are well organized, where users can find the data easily.
- Duplicates are removed.
- A complicated column can be split into two, simpler columns.
- Multiple columns can be combined into one column for readability.
- Codes and integers can be replaced with human-readable values.

Other tasks:
- Select only needed columns and rows to load (filtering).
- Character set conversion and encoding.
- Datetime, currency and numerical conversions.
- Using rules and lookup tables for data standardization.
- Using data range validation. For example, setting the Age or Discount fields for a maximum of two digits.
- Data flow validation from the staging area to the destination tables.
- Check the required fields.
- Clean missing data Replace NULL values with zeros in numerical fields, substitute blank entries with a default category in text fields (For example, "Uncategorized"), and fill empty dates with a placeholder or the current date (For example, "01/01/1900")
- Split a column into multiple columns and merge multiple columns into a single column.
- Use any complex data validation

3. Load
The final step, load includes sending the transformed data into the data model. After this step you can start to use data for analytical purposes, reporting systems, planning strategies etc.

4. Challenges
Some of the ETL challenges you might take into consideration are:
- Data loss during the ETL process.
- Data quality and integrity issues (incorrect, incomplete, or duplicate data).
- Long-term maintenance difficulties.
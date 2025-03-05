# Optimization performance
- Performance takes more importance when the dataset gets bigger
- its basically to keep the data model fast enough.
- Optimization: Transformation, Cleaning, Organization
#### Optimization methods
- Sorting
- Filtering
- Indexing
- Data Transformation

### Impact of cardinality on perfromance
HIGH cardinality: many distinct values in a column. It directly affects the model performance.
low cardinality: few distinct values    

**Solution:**
- Summarization: aggregation (Power Query -> Select column (click on header) -> Transform tab -> Group By -> Select column -> Select aggregation function -> Ok)
- Fixed decimals (locate decimal column -> Transform tab -> Data Type -> Fixed decimal number)

### Optimizing columns and metadata
- Metadata, in the simplest terms, is data about data. 
- It provides information about other data, making it easier to retrieve, manipulate, and manage. 
- Some examples of metadata In Microsoft Power BI, would be table names, column names, relationships, or data types. Metadata acts as a map guiding you through the data landscape, making navigating vast volumes of information easier. 

- Power Query -> View Ribbon -> Data Preview section:
    Column quality: It displays a column's percentage of valid, error, and empty entries. A Valid percentage of less than 100% indicates the presence of errors or empty cells that need addressing.

    Column distribution:  It displays a histogram that represents the frequency of values within your column. (Distinct Values counts all different values, even if they appear multiple times. Unique Values counts only the values that appear exactly once.)

    Column Profile feature provides a detailed overview of your columns, showing statistical measures such as count, unique count, min, max, and average. It also displays a distribution chart. This feature is highly beneficial when understanding your data and helps identify issues such as outliers. 

- Remove unnecesary columns for the analysis.
- Categorize data columns
- Change column data types

### Optimizing the Auto Date/Time feature
- Auto Date/Time feature in Power BI is essentially a convenience function. 
- Whenever you add a field to your data model that has a Date data type, Power BI automatically generates a hidden Date table for that field. 
- This table includes multiple columns including Year, Quarter, Month and Day. This allows Power BI to perform time-intelligence calculations 
Power BI -> File tab -> Options and settings -> Options -> Data load -> checkbox labeled Auto date/time ->  By default, this box is checked, which means the feature is enabled.

**Important:** these steps only disable the Auto Date/Time feature for the current file. 

#### Benefits of disabling the Auto date/time feature
Greater Flexibility and Control: Disabling this feature reduces the size of the data model, leading to faster load times.

Improved Query Performance: Each time a query that involves a date field is run, Power BI must  interact with these hidden tables
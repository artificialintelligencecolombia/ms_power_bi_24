# Storage modes
### Import mode
- Small data sizes
- Various sources
- Stored in memory
- Enables quick access
i.e: excel file dataset

If you want to optimize for faster queries, select Import.

### DirectQuery mode
- Connect directly to the data source
- Larger datasets
- Real time access to data
- Impact on performance when queries are complex

Select DirectQuery to connect directly to your data source without having to import the data into Power BI Desktop. This is especially useful for large or frequently changing data sources.

NOTE: once you set the storage mode of a table to Import, it cannot be undone. This is a permanent action, and you won't be able to switch to DirectQuery or Dual modes afterwards.

### Dual mode
- Combines both Import and DirectQuery modes benefits

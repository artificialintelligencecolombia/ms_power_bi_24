# Direct Query
DirectQuery is a storage mode in Power BI where data is not imported into the Power BI dataset. Instead, queries are sent directly to the underlying data source at runtime, retrieving only the necessary data for the report's visualizations.     

### Use cases
- Large datasets where import is impractical (e.g., billions of rows).
- When real-time or near real-time reporting is required.
- Data governance policies prevent data duplication in Power BI.

### Query Reduction Strategies
1. Limit the number of queries to sent to the source
    - Disable Auto Date/Time (Options -> Global -> Data Load -> Uncheck Auto Date/Time) 
    - Remove unused columns in Power Query
    - Aggregate data before loading it
2. Optimize filters and slicers
    - Use Apply Button for slicers and filters (Options & Settings → Options → Query Reduction → Enable "Add Apply button to slicers/filters")
3. Avoid complex measures
    - Use variables in measures 
    - Minimiza use of CALCULATE 

### Steps to Optimizing a DirectQuery model
1. Establish a DirectQuery connection to Adventure Works database from Power BI.
1.1. Launch Power BI desktop and connect to the SQL server. Navigate to the Home tab of Power BI desktop and select Get data. From the drop-down menu, select SQL Server. 
1.2. This opens a SQL Server database dialog box. Enter the server's name and database name. Once you enter the server’s name, a connection is established with the SQL Server hosting all databases.

**Tip:** The SQL server does not require a database name for the connection, but if you have a lot of databases in the Server, defining the database name while connecting will save you time navigating through the required database.

1.3. Check the DirectQuery option for the data connectivity mode. If your SQL Server is installed on your local machine, you can add localhost in the server's name section.

1.4. Once the connection is established, Microsoft Power BI opens the navigator window, which lists all the tables available to load in the database. Select the following tables and then select Load on the bottom right:

dbo.FactInternetSales
dbo.dimProduct
dbo.dimCustomer
dbo.dimSalesTerritory
The tables are loaded to the data model of Power BI as a DirectQuery.

1.5. Establish relationships between the Fact table and the dimension tables as you did with import data. Note that there is no data view available when connecting to DirectQuery because data is not imported to Microsoft Power BI.

2. Optimize DirectQuery by query reductions.

2.1. Now that a connection has been established to the dataset via DirectQuery and the desired tables loaded into the data model, you need to optimize the performance via query reduction. Select File and then Options and settings from the sidebar menu to navigate the query reduction options.

2.2. Select Options to open the Options dialog box when the submenu opens.

2.3. Scroll down the page and select Query reduction from the left sidebar to display three options:

- The first is Reduce number of queries sent by. Selecting this option disables cross-highlighting or filtering, the primary feature in Power BI, which makes it an interactive visualization tool. If cross-highlighting or filtering is enabled, other visuals will be highlighted or filtered when you select one visual. If you have some visuals in the report that do not interact with each other, enabling this option will reduce the number of queries sent to the database.
- Slicers, the second option, is more relevant for visualizations. It’s useful for multi-select slicers and filters.

2.4. The third heading is Filters, which offers three choices:
- Instantly apply basic filter changes is selected by default.
- Add Apply button to all basic filters to apply changes when you are ready adds an Apply button to all basic filters.
- Add a single Apply button to the filter pane to apply changes at once adds a single Apply button to the entire Power BI filter pane. Any changes you make will not execute until you select the Apply button.

**Tip:** The third option is highly recommended to avoid unwanted changes, especially when you have a multi-selection filter. You can choose to have one Apply button for the entire filter pane, which is helpful in query reduction.

3. Optimize DirectQueryby table storage mode of Power BI.
3.1. You now need to optimize the performance via table storage. Select Model view and expand the Properties pane on the right-hand side.

3.2. Select the dbo.FactInternetSales table to display the properties for that table. Scroll down the Properties pane and expand the Advanced section.

3.3. Expand the Storage mode drop-down menu and select Import storage mode.

3.4. A dialog box appears onscreen, showing a warning stating that setting the storage mode to import is irreversible. You will not be able to switch back to DirectQuery.Select OK. This imports the Sales table to the im-memory engine of Microsoft Power BI. Each time you interact with the report via filters or slicers, Power BI sends queries to the underlying data source for dimension tables. The dimension tables filter relevant data from the imported fact table, reducing the number of queries sent to the underlying database.

**Tip:** In the real world, you can optimize(according to the analytical needs of the business) which tables to import and which to keep in the DirectQuery connection.

4. Save the Power BI project.
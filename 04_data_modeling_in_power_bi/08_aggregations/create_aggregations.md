# Create aggregations

### Step-by-Step Process to Create Aggregations in Power BI
1. Connect to the Data Source
Open Power BI Desktop.
Navigate to "Get Data" > "SQL Server".
Enter the Server Name and Database Name.
Change the default Import Mode to DirectQuery, then click OK.
Select the required tables:

- Fact Table: Internet Sales
- Dimension Tables: Customer, Date

2. Review and Adjust Relationships
Power BI auto-detects relationships.
Open Model View to review them.
Ensure the Date and Internet Sales tables have an active relationship and delete inactive relationships.
Delete any inactive relationships.

3. Create Aggregations Using Power Query Editor
3.1: Reference the Fact Table
Go to "Transform Data" (Power Query Editor).
In the Queries Pane, right-click the Internet Sales fact table.
Select "Reference" (creates a linked duplicate without modifying the original).
Rename this new query as Agg_Sales (Aggregated Table).
3.2: Choose Columns for Aggregation
Click "Choose Columns" in the Home Tab.
Unselect all columns.
Select only the necessary columns:
OrderDateKey -> Aggregation column
CustomerKey -> Aggregation column
UnitPrice
SalesAmount
Click OK.
3.3: Perform Grouping and Aggregations
Select "Group By" under the Transform Tab.
Change from Basic to Advanced mode.
In the Grouping Section, select:
OrderDateKey
CustomerKey
In the Aggregations Section, define calculations:
SumSalesAmount → Sum of SalesAmount
SumUnitPrice → Sum of UnitPrice
OrderCount → Count Rows (does not require a column reference)
Click OK.

4. Establish Relationships for Aggregated Table
In Model View, link the Agg_Sales table with:
Customer Dimension (CustomerKey)
Date Dimension (OrderDateKey)
Ensure relationships are correctly set.

5. Optimize Storage Mode for Performance
Select Agg_Sales in Model View.
In Properties Pane, go to Advanced Settings.
Change Storage Mode from DirectQuery to Import.
A warning dialog appears (irreversible change).
Leave the "Set affected tables to dual" checkbox checked.
Click OK.

📌 Why Set Dimension Tables to Dual?

The Customer and Date tables connect to both the original DirectQuery fact table and the aggregated Import table.
Dual mode allows them to act as Import or DirectQuery based on query context.

### Final Verification & Best Practices
✅ Verify Storage Mode
In Model View, check the storage mode of each table:
Agg_Sales → Import
Internet Sales → DirectQuery
Customer & Date → Dual
✅ Test Aggregation Behavior
Create a simple report using fields from Agg_Sales.
Monitor SQL Profiler to confirm Power BI is hitting the aggregated table instead of the fact table.
If queries still go to the fact table, check:
Relationship issues.
Aggregation definitions.
Correct column selections.

### Notes & Tips
🚀 Performance Optimization
Always use aggregations with DirectQuery to improve query response times.
Limit aggregation tables to a small number of grouped dimensions.
Avoid unnecessary columns to minimize memory usage.
⚡ Common Pitfalls
Not setting storage mode correctly → Aggregations won't work properly.
Keeping inactive relationships → Can cause unexpected behavior in queries.
Not defining "Dual Mode" for dimension tables → Might lead to unnecessary DirectQuery calls.

### Summary
Connect to SQL Server in DirectQuery mode.
Load necessary tables (Internet Sales, Customer, Date).
Reference the fact table and create an aggregated table (Agg_Sales).
Select only required columns and apply Group By aggregations.
Establish relationships between Agg_Sales and dimension tables.
Set storage mode for Agg_Sales to Import and dimensions to Dual.
Validate that queries hit the aggregated table first for better performance.
🚀 Using aggregations in Power BI enables faster, scalable, and efficient reporting, especially when dealing with large datasets in DirectQuery mode!
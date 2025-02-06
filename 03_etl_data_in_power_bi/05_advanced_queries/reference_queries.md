# Reference queries

A reference query(table) is a way to create a new query(table) that points to an existing one without duplicating its data. It inherits the transformations of the original query(table) but can be modified separately.

Instead of recreating the same transformations multiple times, you can simply reference the master query and apply it to different datasets. This streamlined approach accelerates the data preparation process and allows you to focus on analysis and insights.

Purpose: Optimize performance and maintainability.
Example: You have a query(table) for customer data. Instead of duplicating it, you create a reference query(table) to filter only "VIP customers" while keeping the original intact.

Every change to the original query(table) will be reflected in the reference query(table). However, changes to the reference query won't affect the original one.

### Reference vs. Duplicate Table in Power BI

#### Reference Table
Linked copy of the original table.
Updates automatically when the original table changes.
Used for different aggregations, filters, or relationships without altering the original.

Use Cases:
- Creating summary tables for performance optimization.
- Using the same table in different relationships (e.g., Sales by Region vs. Sales by Product).

#### Duplicate Table
Independent copy of the original table.
Does not update when the original table changes.
Used for modifications, testing, or static data snapshots.

Use Cases:
- Creating different dataset versions for analysis.
- Storing historical snapshots without affecting live data.
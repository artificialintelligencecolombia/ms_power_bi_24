# Quick Reference Guide: Data Combination Techniques in Power BI

## **1. Append Queries**
- **Purpose**: Combines rows from two or more tables into a single table.  
  Similar to a SQL **UNION** operation.
- **Use Case**: When tables have the **same structure** (columns and types) and need to be stacked vertically.  
  Example: Monthly sales data split across multiple tables.

### **Steps to Append:**
1. Open **Power Query Editor**.
2. Go to **Home → Append Queries**.
   - Select "Append Queries as New" to create a new table.
   - Select "Append Queries" to modify the current table.
3. Choose the tables to combine and click **OK**.

---

## **2. Merge Queries**
- **Purpose**: Combines columns from two or more tables based on a matching key.  
  Similar to a SQL **JOIN** operation (e.g., Inner Join, Left Join).
- **Use Case**: When tables have related data and need to be combined horizontally.  
  Example: Merging customer details with sales transactions using a "Customer ID."

### **Steps to Merge:**
1. Open **Power Query Editor**.
2. Go to **Home → Merge Queries**.
3. Select the tables and the column(s) to match.
4. Choose the join type (e.g., Inner, Left, Full).
5. Expand the resulting column to include only the desired fields.

---

## **Common Tips for Combining Data:**
- **Ensure Consistency**:
  - Column names and data types must match for append queries.
  - Key columns must contain unique and matching values for merges.
- **Handle Errors**: Always clean and format your data before combining to avoid mismatches or null values.
- **Optimize Performance**: Use filters in Power Query to reduce unnecessary rows or columns before combining large datasets.
- For append queries, make sure that the tables has the same number of columns and the columns are in the same order.

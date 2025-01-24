# Pivot and Unpivot in Power BI (Power Query)

## **Pivot**
- **Description**: Converts **rows into columns**.
- **Use Case**: Useful when category values in rows need to become column headers with aggregated data.  
- Narrow format to wide format
  Example: Sales data by region becoming columns for each region.
- **Steps**:  
  1. Select a column to pivot.  
  2. Click **Transform → Pivot Column**.  
  3. Choose a value column to aggregate (e.g., Sum, Average).

## **Unpivot**
- **Description**: Converts **columns into rows**.
- **Use Case**: Ideal for normalizing data, turning multiple columns into a single column with corresponding values.  
- Wide format into narrow format
  Example: Monthly sales columns transformed into "Month" and "Sales" rows.
- **Steps**:  
  1. Select columns to unpivot.  
  2. Click **Transform → Unpivot Columns**.

---

## **Additional Insight**
- **Tip for Data Modeling**:  
  Use **Unpivot** to prepare data for measures in a star schema. Flattened, normalized data simplifies creating visualizations and ensures compatibility with DAX functions.
